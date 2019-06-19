

mkdir -p "dist"
MD_FILE="dist/book.md"
PDF_FILE="dist/book.pdf"

echo "" > ${MD_FILE}

N=0

function remove_trailing_lines() {
  sed '/./,$!d' | sed -e :a -e '/^\n*$/{$d;N;};/\n$/ba' 
}

# this is so we can use \Begin{minipage} and not have the inner
# content processed by latex. 
echo "
---
header-includes:
   - \\newcommand{\\hideFromPandoc}[1]{#1}
       \\hideFromPandoc{
           \\let\\Begin\\begin
           \\let\\End\\end
       }
---
" >> ${MD_FILE}
for f in src/*.py; do
  if [[ ${f} != "src/__init__.py" ]]; then
    echo "" >> ${MD_FILE}
    echo "\\Begin{minipage}{\\textwidth}" >> ${MD_FILE}
    echo "" >> ${MD_FILE}
    echo "Problem ${N} Source" >> ${MD_FILE}
    echo "--------" >> ${MD_FILE}

    echo "\`\`\`python" >> ${MD_FILE}
    cat ${f} | remove_trailing_lines | cat -n>> ${MD_FILE}
    echo "\`\`\`" >> ${MD_FILE}

    echo "Problem ${N} Output" >> ${MD_FILE}
    echo "--------" >> ${MD_FILE}
    echo "\`\`\`bash" >> ${MD_FILE}
    python ${f} 2>&1 | sed "s/${f/\//\\\/}/Problem ${N}/g"  | cat -n | fmt -s >> ${MD_FILE}
    echo "\`\`\`" >> ${MD_FILE}
    echo "" >> ${MD_FILE}
    echo "\\End{minipage}" >> ${MD_FILE}
    echo "" >> ${MD_FILE}

    ((N++))
  fi

done
pandoc ${MD_FILE} -o ${PDF_FILE} -V geometry:margin=1in && evince ${PDF_FILE}

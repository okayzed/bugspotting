mkdir -p "dist"
MD_FILE="dist/book.md"
PDF_FILE="dist/book.pdf"

echo "" > ${MD_FILE}

N=0
for f in src/*.py; do
  if [[ ${f} != "src/__init__.py" ]]; then
    echo "" >> ${MD_FILE}
    echo "Problem ${N} Source" >> ${MD_FILE}
    echo "--------" >> ${MD_FILE}

    echo "\`\`\`python" >> ${MD_FILE}
    cat -n ${f} | fmt -s -w 90 >> ${MD_FILE}
    echo "\`\`\`" >> ${MD_FILE}

    echo "Problem ${N} Output" >> ${MD_FILE}
    echo "--------" >> ${MD_FILE}
    echo "\`\`\`bash" >> ${MD_FILE}
    python ${f} 2>&1 | sed "s/${f/\//\\\/}/Problem ${N}/g"  | cat -n | fmt -s >> ${MD_FILE}
    echo "\`\`\`" >> ${MD_FILE}

    ((N++))
  fi

done
pandoc ${MD_FILE} -o ${PDF_FILE} -V geometry:margin=0.5in
evince ${PDF_FILE}

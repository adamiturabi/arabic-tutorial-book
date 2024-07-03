# PNG images are too large. Convert them from the PDF images to a smaller size.
cd Learn-Standard-Arabic_files/figure-latex/
for FILE in *.pdf; do
  echo "${FILE%.*}"
  echo "${FILE#*.}"
  magick -density 150 -quality 100 $FILE "${FILE%.*}.png"
  mv -f "${FILE%.*}.png" ../../docs/Learn-Standard-Arabic_files/figure-html/
done


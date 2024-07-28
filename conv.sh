# PNG images are too large. Convert them from the PDF images to a smaller size.
cd Learn-Standard-Arabic_files/figure-latex/
for FILE in *.pdf; do
  echo "${FILE%.*}"
  echo "${FILE#*.}"

  # density tune value from 100 to 150 to adjust size in html
  #magick -density 130 -quality 100 $FILE "${FILE%.*}.png"
  #mv -f "${FILE%.*}.png" ../../docs/Learn-Standard-Arabic_files/figure-html/

  dvisvgm --font-format=ttf --scale=1.45 --pdf $FILE
  mv -f "${FILE%.*}.svg" ../../docs/Learn-Standard-Arabic_files/figure-html/
done
cd ../../docs/
sed -i 's/\.png\"/.svg"/g' *.html
cd Learn-Standard-Arabic_files/figure-html/
rm *.png


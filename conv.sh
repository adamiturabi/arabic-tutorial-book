# See notes/font_scaling_and_tikzpictures.md for a history behind this script.
cd A-Learners-Grammar-of-Classical-Standard-Arabic_files/figure-html/
for FILE in *.pdf; do
  echo "${FILE%.*}"
  echo "${FILE#*.}"

  # density tune value from 100 to 150 to adjust size in html
  #magick -density 130 -quality 100 $FILE "${FILE%.*}.png"
  #mv -f "${FILE%.*}.png" ../../docs/Learn-Standard-Arabic_files/figure-html/

  dvisvgm --font-format=ttf --scale=1.2 --pdf $FILE
  mv -f "${FILE%.*}.svg" ../../docs/A-Learners-Grammar-of-Classical-Standard-Arabic_files/figure-html/
done
cd ../../docs/
#sed -i 's/\.png\"/.svg"/g' *.html
sed -i 's/embed \(src=\"[^\.]\+\)\.pdf\"/img \1.svg\"/g' *.html
cd A-Learners-Grammar-of-Classical-Standard-Arabic_files/figure-html/
rm unnamed-chunk-*.pdf


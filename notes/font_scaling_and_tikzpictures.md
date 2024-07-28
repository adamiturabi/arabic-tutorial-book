# How to handle Arabic font scaling and tikzpictures for HTML and PDF output

## Arabic vs Latin font sizes in HTML vs PDF

The Arabic font (Vazirmatn) is scaled to the same size as the Latin font (Charis) for the PDF output. This is done by having in `index.Rmd`:

```
fontfamilies:
  - name: \arabicfont
    font: Vazirmatn-Light
    options: Script=Arabic,Scale=1.0
```

But for HTML we want the Arabic font to be scaled bigger. So we have added to `mystyle.css`:

```
:lang(ar) {
  font-size: 1.2em; /* scale up Arabic font size wrt English */
  line-height: 100%;
}
```

## Tikz and post processing

Bookdown allows using tikz for pictures for both HTML and PDF. At its simplest we can add something like this in the `.Rmd` file:

````
```{r,echo=FALSE,engine='tikz', fig.ext='pdf', engine.opts = list(template = "srctex/tikz2pdf-lua.tex")}
\usetikzlibrary{decorations.text, decorations.pathreplacing}
\begin{tikzpicture}[nodes={text depth=0.25ex,text height=1.25ex}]
\path [decoration={text effects along path, 
  text=``The building is a house.'',
  text effects/.cd, 
    path from text, text along path,
    group letters, word count=\w,
    every word/.style={name=word-\w, execute at begin node=\strut}},
  decorate] (0,0);
\end{tikzpicture}
```
````

The file `srctex/tikz2pdf-lua.tex` may be the following:

```
\RequirePackage{luatex85}
\documentclass{article}
\usepackage[luatex,active,tightpage]{preview}
\usepackage{amsmath}
\usepackage{tikz}

\usepackage{fontspec} % this also loads fontspec
\defaultfontfeatures{Scale=MatchLowercase}
\defaultfontfeatures[\rmfamily]{Ligatures=TeX,Scale=1}
\setmainfont{Charis SIL}

\usetikzlibrary{matrix}
\usepackage{arabluatex}
\newfontfamily{\arabicfont}[Script=Arabic,Scale=1.0]{Vazirmatn-Light}
%\newfontfamily\arabicfont{Vazirmatn-Light}[Script=Arabic]

\begin{document}
\begin{preview}
%% TIKZ_CODE %%
\end{preview}
\end{document}
```

This will by default produce a directory `Learn-Standard-Arabic_files` with subdirectories":

+ `figure-html` containing PNG files that are automatically copied into `docs` and linked in the HTML output using `<img src="filename.png" >` tags.
+ `figure-latex` containing PDF files that are automatically used for the PDF output.

## The problem

The problems are: 

1. The PNG files are scaled too large with respect to the rest of the text.
2. The PNG files get resampled and grainy on different devices
3. The Arabic font has a 1.0 scaling in the tikz output. This is ok for the PDF output but too small for the HTML output.

To solve the first problem we can post process the PNGs using a `conv.sh` script thus:

```
# PNG images are too large. Convert them from the PDF images to a smaller size.
cd Learn-Standard-Arabic_files/figure-latex/
for FILE in *.pdf; do
  echo "${FILE%.*}"
  echo "${FILE#*.}"

  # density value 130 empirically tuned to get good scaling in HTML output
  magick -density 130 -quality 100 $FILE "${FILE%.*}.png"

  # move files into docs directory replacing the existing files
  mv -f "${FILE%.*}.png" ../../docs/Learn-Standard-Arabic_files/figure-html/
done
```

However, the second and third problems still remain. So, instead of creating PNG output for HTML, we will create a PDF output with a separate `srctex/tikz2pdf-lua-html.tex` that has a higher font scaling for the Arabic font.

Bookdown can embed this PDF figure directly into the HTML page but on some browsers it shows up with an ugly border and toolbar. There is likely a way to fix this by using a PDF viewer from CDN like PDF.js and including some code like this in `index.Rmd`:

```
bookdown::gitbook:
  css: assets/styling/style.css
  pandoc_args: ["--lua-filter=assets/styling/footnote.lua"]
  includes:
    in_header: assets/styling/style.html
    after_body: assets/styling/scripts.html
```

See https://www.bendirt.com/javascript-in-bookdown/

But for now, I am going to post process the PDF pictures that are meant for the HTML (so they are going to be in the figure-html directory) and convert them to PDFs.

First specify different templates for tikz for HTML vs PDF output and specify PDF output extension:

````
```{r,echo=FALSE,engine='tikz', fig.ext='pdf', engine.opts = list(template = if (knitr::is_html_output()) "srctex/tikz2pdf-lua-html.tex" else "srctex/tikz2pdf-lua.tex")}
````

Now add scaling to the Arabic font in `srctex/tikz2pdf-lua-html.tex`:

```
\RequirePackage{luatex85}
\documentclass{article}
\usepackage[luatex,active,tightpage]{preview}
\usepackage{amsmath}
\usepackage{tikz}

\usepackage{fontspec} % this also loads fontspec
\defaultfontfeatures{Scale=MatchLowercase}
\defaultfontfeatures[\rmfamily]{Ligatures=TeX,Scale=1}
\setmainfont{Charis SIL}

\usetikzlibrary{matrix}
\usepackage{arabluatex}
\newfontfamily{\arabicfont}[Script=Arabic,Scale=1.2]{Vazirmatn-Light} % scale up Arabic font
%\newfontfamily\arabicfont{Vazirmatn-Light}[Script=Arabic]

\begin{document}
\begin{preview}
%% TIKZ_CODE %%
\end{preview}
\end{document}
```

Then in `conv.sh` convert the PDF pictures meant for the HTML output to SVG (to maintain vector graphics) and change the tag in the HTML pages from:

```
<embed src="filename.pdf>
```

to

```
<img src="filename.svg>
```

Here is the new `conv.sh`:

```
cd Learn-Standard-Arabic_files/figure-html/
for FILE in *.pdf; do
  echo "${FILE%.*}"
  echo "${FILE#*.}"

  # --font-format is supposed to embed font but doesn't work with my version of dvisvgm yet, and also needs some work with CSS
  # scaling 1.2 empirically tuned
  dvisvgm --font-format=ttf --scale=1.2 --pdf $FILE

  # copy over svg files to docs dir
  mv -f "${FILE%.*}.svg" ../../docs/Learn-Standard-Arabic_files/figure-html/
done

# change tags from embed to img
cd ../../docs/
sed -i 's/embed \(src=\"[^\.]\+\)\.pdf\"/img \1.svg\"/g' *.html

# delete unneeded pdfs
cd Learn-Standard-Arabic_files/figure-html/
rm unnamed-chunk-*.pdf
```


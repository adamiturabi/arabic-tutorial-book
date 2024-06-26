# arabic-tutorial-book

An online book to learn Standard Arabic

# Current status

Work in progress. Not ready for study yet.
Latest version is published here: 

https://adamiturabi.github.io/arabic-tutorial-book/

Use the top menu bar to change font size, change to sepia or dark mode, and to download the PDF.

# Developer documentation

## Useful info

### Password protect static websites

https://github.com/chrissy-dev/protected-github-pages

### Deploy github pages created from bookdown

Add an empty `.nojekyll` file to the `docs` dir.

## Install software prerequisites

### For Ubuntu and derivatives

1. Tex
   ```
   sudo apt install texlive-base
   sudo apt install texlive-xetex
   sudo apt install texlive-lang-arabic
   sudo apt install texlive-fonts-extra
   ```
2. Fonts
   + In current use:
     + New Computer Modern
     + Andika: https://software.sil.org/andika/download/
     + Amiri: https://github.com/alif-type/amiri/releases/latest
     + Vazir: https://github.com/rastikerdar/vazir-font/releases/latest
   + Experimental:
     + Junicode: https://github.com/psb1558/Junicode-font/releases/tag/v1.003
     + Brill: https://brill.com/page/290?language=en
     + Scheherazade New: https://software.sil.org/scheherazade/download/
     + Gentium Plus: https://software.sil.org/gentium/download/
     + STIX Two Text: `https://github.com/stipub/stixfonts/blob/master/zipfiles/static_ttf.zip`
     + Microsoft Core Fonts:
     ```
     sudo add-apt-repository multiverse
     sudo apt update && sudo apt install ttf-mscorefonts-installer
     sudo fc-cache -f -v
     ```

3. Pandoc

   Normally, installing pandoc from the Ubuntu repos would be sufficient thus:
   ```
   sudo apt install pandoc
   ```
   But the version there is pretty old. So, go to the Pandoc project on Github and install the `.deb` from there: https://github.com/jgm/pandoc/releases
   
4. R
   ```
   sudo apt install r-base
   sudo apt install libcurl4-openssl-dev libfontconfig1-dev libssl-dev libxml2-dev
   sudo apt install libv8-dev libavfilter-dev librsvg2-dev libwebp-dev cargo libpoppler-cpp-dev libtesseract-dev libmagick++-dev libharfbuzz-dev libfribidi-dev
   ```

5. Rmarkdown and Bookdown
   1. Open R in a terminal
      ```
      sudo R
      ```
   2. In R:
      ```
      install.packages("rmarkdown", dependencies = TRUE)
      install.packages("bookdown", dependencies = TRUE)
      install.packages("kableExtra", dependencies = TRUE)
      install.packages("tidyverse", dependencies = TRUE)
      install.packages("pander", dependencies = TRUE)
      q()
      ```

### For Arch/Manjaro

1. Install fonts as in Ubuntu

2. Install the following Arch packages:  make gcc texlive-bin texlive-core texlive-latexextra texlive-fontsextra texlive-langextra pandoc r curl fontconfig openssl libxml2 pkgconf

3. Rmarkdown and Bookdown
   1. Open R in a terminal
      ```
      sudo R
      ```
   2. In R:
      ```
      install.packages("rmarkdown", dependencies = TRUE, repos='https://cloud.r-project.org/')
      install.packages("bookdown", dependencies = TRUE, repos='https://cloud.r-project.org/')
      install.packages("kableExtra", dependencies = TRUE, repos='https://cloud.r-project.org/')
      install.packages("tidyverse", dependencies = TRUE, repos='https://cloud.r-project.org/')
      install.packages("pander", dependencies = TRUE, repos='https://cloud.r-project.org/')
      q()

   There could be some errors. Don't worry about them.

## Building the book from source files

In a Linux terminal:

```
cd path-to-your-preferred-dir
git clone https://github.com/adamiturabi/arabic-tutorial-book.git
cd arabic-tutorial-book
make
```

The created files will be under the `docs` directory. Open `docs/index.html` in a browser and `docs/Learn-Standard-Arabic.pdf` in a PDF viewer.

To delete created files in order to do a clean build:

```
make clean
```



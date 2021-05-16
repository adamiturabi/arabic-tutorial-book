# arabic-tutorial-book

An online book that aims to teach Arabic.

# Install software prerequisites

(For Ubuntu and derivatives)

1. Tex
```
sudo apt install texlive-base
sudo apt install texlive-xetex
sudo apt install texlive-lang-arabic

```

2. Fonts
   + Brill: https://brill.com/page/290?language=en
   + Amiri: https://github.com/alif-type/amiri/releases/latest
   + Microsoft Core Fonts:
```
sudo add-apt-repository multiverse
sudo apt update && sudo apt install ttf-mscorefonts-installer
sudo fc-cache -f -v
```
   + Vazir (optional): https://github.com/rastikerdar/vazir-font/releases/latest

3. R
```
sudo apt install R
```

4. Rmarkdown and Bookdown
   1. Open R in a terminal
```
R
```
   2. In R:
```
install.packages("rmarkdown")
install.packages("bookdown")
q()
```

# Building the book from source files

In a Linux terminal:

```
cd path-to-your-preferred-dir
git clone https://github.com/adamiturabi/arabic-tutorial-book.git
cd arabic-tutorial-book
./buildscript
```

The created files will be under the `_book` directory. Open `_book/index.html` in a browser and `_book/_main.pdf` in a PDF viewer.

To delete created files in order to do a clean build:

```
./cleanbuild
```


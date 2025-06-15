# About

This repository contains the source files for my online book: "A Learner's Grammar of Standard Classical Arabic".
It is a work in progress. So far I have written approximately 25 chapters, with at least as many remaining.
In addition to writing the remaining chapters, I also have to add chapter exercises and vocabulary lists.
There is much editing and work needed even in the chapters already written so it is not ready for study yet.

The output (such as it is) is published here in HTML: https://adamiturabi.github.io/arabic-tutorial-book/

A PDF can be downloaded from the top menu-bar. 

The book is written in markdown produced using [Quarto](https://quarto.org/) which uses pandoc and Latex to render the output.

# To build

Install [Quarto](https://quarto.org/docs/get-started/).

Install the [Charis SIL](https://software.sil.org/charis/download/),
[Amiri](https://github.com/alif-type/amiri/releases/latest),
and [Vazirmatn](https://github.com/rastikerdar/vazirmatn/releases/tag/v33.003)
fonts.

Install Tex

For Linux:

```
sudo apt install texlive-base
sudo apt install texlive-xetex
sudo apt install texlive-lang-arabic
sudo apt install texlive-fonts-extra
sudo apt install texlive-luatex
```

For MacOS install TexLive.

Install the Python3 package `jupyter`:

```
python3 -m pip install jupyter
```

If it doesn't let you install the package in this way, then follow directions to install it in a virtual environment:

```
python3 -m venv path/to/venv
source path/to/venv/bin/activate
python3 -m pip install jupyter
```

In the above repo, within the venv just created (if applicable), 
use this command to render the HTML and PDF outputs:

```
source path/to/venv/bin/activate
./build.sh
```

## Figures

To render the tikz figures, you need Ghostscript and Dvisvgm.

Note that if you use Homebrew on MacOS to manage installation of the ghostscript utility, then, when it updates packages it will change the version number in the path and delete the old path. So then, if you don't update the `libgs` field in `_quarto.yml` to point to the new path then your figures will start to look corrupted.

There is some experimental code (currently disabled) to use Inkscape instead.
To install inkscape on Mac (without sudo):

```
brew install --cask inkscape
```

## Github pages

You might need to an empty `.nojekyll` file to the `docs` dir.


# About

This repository contains the source files for my online book: "A Learner's Grammar of Classical Standard Arabic".
It is a work in progress. So far I have written approximately 20 chapters, with at least as many remaining.
In addition to writing the remaining chapters, I also have to add chapter exercises and vocabulary lists.
There is much editing and work needed even in the chapters already written so it is not ready for study yet.

The output (such as it is) is published here in HTML: https://adamiturabi.github.io/arabic-tutorial-book/

A PDF can be downloaded from the top menu-bar. 

I am planning to port the typesetting and publishing workflow from [Bookdown](https://bookdown.org/) to [Quarto](https://quarto.org/) إن شاء الله.

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
   sudo apt install texlive-luatex
   ```
2. Fonts
   + In current use:
     + [Charis SIL](https://software.sil.org/charis/download/)
     + [Vazir](https://github.com/rastikerdar/vazir-font/releases/latest)
     + [Amiri](https://github.com/alif-type/amiri/releases/latest)
     + [Andika](https://software.sil.org/andika/download/)
   + Experimental:
     + [New Computer Modern](https://ctan.org/pkg/newcomputermodern?lang=en)
     + [DejaVu Serif](https://github.com/dejavu-fonts/dejavu-fonts)
     + [Junicode](https://github.com/psb1558/Junicode-font/releases/tag/v1.003)
     + [Brill](https://brill.com/page/290?language=en)
     + [Scheherazade New](https://software.sil.org/scheherazade/download/)
     + [Gentium Plus](https://software.sil.org/gentium/download/)
     + [STIX Two Text](https://github.com/stipub/stixfonts/blob/master/zipfiles/static_ttf.zip)
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

### For Ubuntu Docker container

1.  Install Docker Desktop.

2.  Create a dockerfile with the following contentss:

    ```
    FROM ubuntu:24.04
    RUN apt update -y
    RUN apt upgrade -y
    RUN apt install -y \
      sudo vi vim wget openssh-client git \
      texlive-base texlive-xetex texlive-lang-arabic texlive-fonts-extra texlive-luatex \
      r-base libcurl4-openssl-dev libfontconfig1-dev libssl-dev libxml2-dev \
      libv8-dev libavfilter-dev librsvg2-dev libwebp-dev cargo libpoppler-cpp-dev \
      libtesseract-dev libmagick++-dev libharfbuzz-dev libfribidi-dev
    ```
    
3.  Navigate to directory that has dockerfile, and build an image:
    
    ```
    docker build -t ubuntu-arabic-book-dev-image-20240831 .
    ```

    The image name (after `-t`) can be anything you choose.

    This will take a while.

4.  Verify that the image exists. In your terminal, run `docker images`. It should show something like:

    ```
    REPOSITORY                              TAG       IMAGE ID       CREATED         SIZE
    ubuntu-arabic-book-dev-image-20240831   latest    47a614803fad   2 minutes ago   4.93GB
    ```

5.  Build a container from the image and launch the bash shell in it:

    ```
    docker run -it --name=ubuntu-arabic-book-dev-cont ubuntu-arabic-book-dev-image-20240831 /bin/bash
    ```
    
    The container name (after `--name=`) may be anything you choose.
    
6.  You are now in the container. Create a sudo user (`myusername` is a placeholder) and go through the steps to add a password:

    ```
    sudo adduser myusername
    ```

    Give sudo access:

    ```
    sudo usermod -aG sudo myusername
    ```

    Switch to user:

    ```
    sudo su - myusername
    ```
7.  Try stopping and restarting container.
    
    To stop the container, you can simply exit (possibly multiple times) from bash until you reach the host (MacOS) terminal from where you ran `docker run ...`.
    
    Your container still exists and its data is persistent.

    Check to list containers using `docker ps -a`. It should show:

    ```
    CONTAINER ID   IMAGE                                   COMMAND       CREATED          STATUS                     PORTS     NAMES
    a8a04f9c5710   ubuntu-arabic-book-dev-image-20240831   "/bin/bash"   38 minutes ago   Exited (0) 2 minutes ago             ubuntu-arabic-book-dev-cont
    ```

    Now restart the container using the command:

    ```
    docker start ubuntu-arabic-book-dev-cont
    ```

    Now relaunch bash:

    ```
    docker exec -it ubuntu-arabic-book-dev-cont /bin/bash
    ```

8.  Install additional packages:

    Pandoc (get latest, and for your container's architecture):
    ```
    wget https://github.com/jgm/pandoc/releases/download/3.3/pandoc-3.3-1-amd64.deb
    sudo dpkg -i pandoc-3.3-1-amd64.deb
    ```

9.  Install R packages, as in Ubuntu install above.

10. Generate SSH key for Github

    ```
    ssh-keygen -t ed25519 -C "<github email>"
    ```

    Open `~/.ssh/id_ed25519.pub` and copy to clipboard. Add new SSH to your Github account and paste this there.

11. Install fonts:

    Varirmatn:

    ```
    cd
    mkdir vazirmatn
    cd vazirmatn
    wget https://github.com/rastikerdar/vazirmatn/releases/download/v33.003/vazirmatn-v33.003.zip
    unzip vazirmatn-v33.003.zip
    cp fonts/ttf/*.ttf ~/.fonts
    ```

    Amiri:

    ```
    cd
    mkdir amiri
    cd amiri
    wget https://github.com/aliftype/amiri/releases/download/1.000/Amiri-1.000.zip
    unzip Amiri-1.000.zip
    cp Amiri-1.000/*.ttf ~/.fonts
    ```

    Charis SIL

    ```
    cd
    mkdir charis
    cd charis
    wget https://software.sil.org/downloads/r/charis/CharisSIL-6.200.zip
    unzip CharisSIL-6.200.zip
    cp CharisSIL-6.200/*.ttf ~/.fonts
    ```
    
To copy files from the container to the host, use this command:

```
docker cp <containerId>:/file/path/within/container /host/path/target
```

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



#!/usr/local/bin/bash
mkdir -p srcqmd_backup
cp srcqmd/*.qmd srcqmd_backup/
perl -i -pe's/;([#\w]+);/[$1]{.term}/g' srcqmd/*.qmd

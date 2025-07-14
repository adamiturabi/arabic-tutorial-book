#!/usr/local/bin/bash
rm -rf content/*
touch content/refs.qmd
cp srcqmd/*.qmd content
quarto render --profile makepdf
quarto render --profile makehtml
mv pdf_out_dir/*.pdf docs/
rmdir pdf_out_dir


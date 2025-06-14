#!/usr/local/bin/bash
quarto render --profile makepdf
quarto render --profile makehtml
mv pdf_out_dir/*.pdf docs/
rmdir pdf_out_dir


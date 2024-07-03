all:
	Rscript compilebook.R
	touch docs/.nojekyll
	rm -rf Learn-Standard-Arabic_files
clean:
	Rscript clean.R
	rm -f *.log
	rm -rf _bookdown_files
	rm -f _bookdown.yml

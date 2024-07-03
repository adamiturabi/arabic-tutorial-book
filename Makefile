all:
	Rscript compilebook.R
	touch docs/.nojekyll
	bash conv.sh
clean:
	Rscript clean.R
	rm -f *.log
	rm -rf _bookdown_files
	rm -f _bookdown.yml

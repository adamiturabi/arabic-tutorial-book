all:
	Rscript compilebook.R
clean:
	Rscript clean.R
	rm -f *.log
	rm -rf _bookdown_files
	rm -f _bookdown.yml

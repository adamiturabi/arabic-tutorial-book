all:
	Rscript compilebook.R
clean:
	Rscript clean.R
	rm *.log

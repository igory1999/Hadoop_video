PDFLATEX=`which pdflatex`
VIEW=`which xpdf`
name=Introduction

all:	cleanall $(name).pdf view

Introduction.pdf: $(name).tex Introduction.tex 
	$(PDFLATEX) $(name)
	$(PDFLATEX) $(name)
	$(PDFLATEX) $(name)
	$(PDFLATEX) $(name)
view: $(name).pdf
	$(VIEW) -z page -geometry 1920x1080 -fullscreen $(name).pdf

clean: 
	rm -f *.toc *.snm *.out *.nav *.log *.aux *.vrb *~ *.pdfpc

cleanall: clean
	rm -rf *.pdf

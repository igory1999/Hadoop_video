PDFLATEX=`which pdflatex`
VIEW=`which xpdf`
name=Spark

all:	cleanall $(name).pdf view

Spark.pdf: $(name).tex Introduction.tex Conclusion.tex RDD.tex SQL.tex ML.tex BD.tex Streaming.tex SharedVariables.tex midway.tex references.tex login.tex git.tex
	$(PDFLATEX) $(name)
	$(PDFLATEX) $(name)
	$(PDFLATEX) $(name)
	$(PDFLATEX) $(name)
	mv $(name).pdf ../
view: $(name).pdf
	$(VIEW) -z page -geometry 1920x1080 -fullscreen ../$(name).pdf

clean: 
	rm -f *.toc *.snm *.out *.nav *.log *.aux *.vrb *~ *.pdfpc

cleanall: clean
	rm -rf ../*.pdf

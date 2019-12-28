name=study


all: cleanall ${name}.pdf view

${name}.pdf: ${name}.tex
	/usr/bin/pdflatex ${name}
	/usr/bin/pdflatex ${name}
	/usr/bin/pdflatex ${name}
	/usr/bin/pdflatex ${name}

view: ${name}.pdf
	xpdf -fullscreen ${name}.pdf

clean:
	rm -f *.toc *.snm *.out *.nav *.log *.aux *.vrb *~

cleanall: clean
	rm -rf *.pdf

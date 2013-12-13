.PHONY: all pdf ps dvi

all:
	@xelatex report.tex
	@bibtex report.aux
	@xelatex report.tex
	@xelatex report.tex

clean:
	rm -f *.ps *.dvi *.pdf *.aux *.log *.bbl *.blg *.out

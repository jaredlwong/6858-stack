.PHONY: all pdf ps dvi

all:
	xelatex report.tex

clean:
	rm -f *.ps *.dvi *.pdf *.aux *.log

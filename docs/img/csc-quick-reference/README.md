---
search:
  boost: 0.1
---

# CSC Quick Reference

Contact: @attesillanpaa @JMuff22 @joonas-somero

This folder contains the current version of the "CSC Quick Reference" As well as old copies. There is a Word doc file as well as a LaTeX file to produce the document. Old copies are kept but this may change in the future.

## Source file in repository

The LaTeX source file can be found in the repository, under _[docs/img/csc-quick-reference/](https://github.com/CSCfi/csc-user-guide/tree/master/docs/img/csc-quick-reference)_.

## Building LaTeX file

Simply `latexmk -pdf --shell-escape "csc-quick-reference.tex"`. Latexmk ships with most tex distributions (TeXLive and MiKTeX) and is a wrapper Perl script to run `pdflatex` or your LaTeX distribution the correct number of times. It makes formatting much easier. It is currently maintained at: https://personal.psu.edu/~jcc8/software/latexmk/.

## Word Doc

Open the Word doc (`.docx`) in Microsoft Word, edit and save as pdf.

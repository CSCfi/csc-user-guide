# CSC Quick Reference

Contact: @attesillanpaa @JMuff22 @joonas-somero

This folder contains the current version of the "CSC Quick Reference" As well as old copies. There is a word doc file as well as a latex file to produce the document. Old copies are kept but this may change in the future. 

## Building latex file

Simply `latexmk -pdf --shell-escape "csc-quick-reference.tex"`. Latexmk ships with most tex distributions (TeXLive and MiKTeX) and is a wrapper perl script to run `pdflatex` or your latex distribution the correct number of times. It makes formatting much easier. It is currently maintained at: https://personal.psu.edu/~jcc8/software/latexmk/. 

## Word Doc

Open the word doc (`.docx`) in Microsoft word, edit and save as pdf. 
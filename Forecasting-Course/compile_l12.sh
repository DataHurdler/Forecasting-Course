#!/bin/bash
cd "C:/Users/87152137/Documents/GitHub/claude-code-test/Slides"
export TEXINPUTS="../Preambles;;"
export BIBINPUTS="../;;"
xelatex -interaction=nonstopmode Lecture12_Capstone.tex
bibtex Lecture12_Capstone
xelatex -interaction=nonstopmode Lecture12_Capstone.tex
xelatex -interaction=nonstopmode Lecture12_Capstone.tex

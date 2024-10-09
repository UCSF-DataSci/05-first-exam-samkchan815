#!/bin/bash

mkdir -p data
mkdir -p scripts
mkdir -p results

touch scripts/generate_fasta.py
touch scripts/dna_operations.py
touch scripts/find_cutsites.py

touch results/cutsite_summary.txt

touch data/random_sequence.fasta

echo "This project contains three directories: data, scripts, and results" > README.md
echo "" >> README.md
echo "The Scripts folder has 3 files" >> README.md
echo "    generate_fasta.py, dna_operations.py, find_cutsites.py" >> README.md
echo "The results folder has a text file called cutsite_summary.txt" >> README.md
echo "The data folder has a fasta file named random_sequence.fasta" >> README.md

chmod +x setup_project.sh
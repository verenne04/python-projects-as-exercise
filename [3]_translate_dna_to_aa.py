# Ask the user for a file containing a DNA sequence (such as example file
# dna_seq_raw.txt ). However, the file is corrupted and contains errors, meaning that
# some characters are not valid nucleotides. Moreover, rather than being well organized,
# Your task is to:
#     - fix the sequence by eliminating the wrong characters;
#     - translate it into peptides (sequences of amino acids, use the termination
#         characters, translated to  _  as interruption to split them);
#     - store the peptides in a new FASTA file with a name obtained by replacing the
#         extension of the input file with  fasta , adding a name for each peptide, based
#         on position. 
# To facilitate your task, you're given a file  dna_to_aa.csv
# containing the correspondence between codons and amino acids.  _  is the
# termination character. Also assume no problems will arise in accessing files.

import csv

DIR = 'files/'
DNA_TO_AA_FILE = DIR + 'dna_to_aa.csv'
DNA_TO_AA_SEP = ';'

CODONSIZE = 3
ALLOWED = 'ATCG'

EXTSEP = '.'
OUTEXT = '.fasta'
AADELIM = '_'

def loadSeqFromFile(fname):
    content = ''
    with open(fname, 'r') as fin:
        for line in fin:
            line = line.strip()
            content += line
    return content

def createDict(fname, sep):
    dict = {}
    with open(fname, 'r') as fin:
        myreader = csv.reader(fin, delimiter=sep)
        for row in myreader:
            dict[row[0]] = row[1]
    return dict

def translateSeq(seq, table):
    size = len(seq)
    protein = ''
    idx = 0
    while idx < size:
        codon = ''
        codonsize = 0
        while codonsize < CODONSIZE and idx < size:
            if seq[idx] in ALLOWED:
                codon += seq[idx]
                codonsize += 1
            idx += 1
        aminoacid = table[codon]
        protein += aminoacid
    return protein

def createFileName(src):
    start = src.rfind(EXTSEP) 
    fname = src[0:start] + OUTEXT
    return fname

def savePeptides(fname, pepseq, sep):
    with open(fname, 'w') as fout:
        pepseq = pepseq.strip(sep)
        lst = pepseq.split(sep)

        np = 1
        for elem in lst:
            if elem != '':
                fout.write(f'>peptide {np}\n')
                fout.write(f'{elem}\n')
            np += 1

# MAIN FLOW
f_name = input('Provide name of a DNA sequence file: ')

# load DNA sequence from file
dnaseq = loadSeqFromFile(f_name)

# create dictionary for dna 2 aa conversion
dna_to_aa = createDict(DNA_TO_AA_FILE, DNA_TO_AA_SEP)

# fix and translate the sequence
prot_out = translateSeq(dnaseq, dna_to_aa)

# create fasta file
fasta_name = createFileName(f_name)
savePeptides(fasta_name, prot_out, AADELIM)



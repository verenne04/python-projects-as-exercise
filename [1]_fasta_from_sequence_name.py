def getOpenFileUser(fname, mode):
    try:
        fin = open(fname, mode)
    except:
        print(f'Error accessing file: {fname}')
        ok = False
        while not ok:
            try:
                fname = input('Provide a new name: ')
                fin = open(fname, mode)
                ok = True
            except:
                print(f'Error accessing file: {fname}')
    return fin

def readFile(fin):
    data = fin.readlines()
    return data

# main flow
# acquire file names:
f_seq = input('Provide name of sequence file: ')
data_seq = getOpenFileUser(f_seq, 'r')

f_names = input('Provide name of names file: ')
data_names = getOpenFileUser(f_names, 'r')

f_fasta = input('Provide name for fasta file: ')
data_fasta = getOpenFileUser(f_fasta, 'w')

seqs = readFile(data_seq)
names = readFile(data_names)

i = 0
for pep in seqs:
    pep = pep.strip()
    data_fasta.write(pep + ' -- ' + names[i])
    i += 1

data_seq.close()
data_names.close()
data_fasta.close()

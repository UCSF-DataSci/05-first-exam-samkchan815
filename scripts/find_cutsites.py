import argparse

def readFasta (file):
    ''' Read FastA record and return the sequence header/sequence'''
    header = ''
    sequence = ''
    
    with open(file, 'r') as fileH: # read through file
        
        header = ''
        sequence = ''
        
        # skip to first fasta header
        line = fileH.readline()
        while not line.startswith('>') :
            line = fileH.readline()
        header = line[1:].rstrip() # save the header

        for line in fileH: # read through each line in file
            if line.startswith ('>'): # check header
                yield header,sequence
                header = line[1:].rstrip()
                sequence = ''
            else :
                sequence += ''.join(line.rstrip().split()).upper() # add lines to sequence

    yield header,sequence


def find_cuts(file, dna):
    '''Find all positions of dna cut in fasta file sequence.'''
    sites = []
    for _, sequence in readFasta(file) : # read in FASTA file
        seq = sequence.strip()

        cutIndex = dna.index('|') # save location of cut to get sequence index
        cut = dna.replace('|', '') # remove cut marker
        
        cutLength = len(cut) # save length of cut sequence

        for i in range(0, len(seq)-cutLength+1): # loop through sequence sliding window
            curr = seq[i:i+cutLength] 
            if curr == cut: # check if current and cut are the same
                sites.append(i+cutIndex) # append to list
    return sites

def find_pairs(sitesList):
    '''Find all pairs between 80-120 kbp away from cut site'''
    pairsList = [] # initialize list
    for i in range(0, len(sitesList)): # loop through list of cut sites
        for j in range(i+1, len(sitesList)): # cross reference with following cut sites
            if ((sitesList[j] - sitesList[i]) >= 80000) and ((sitesList[j] - sitesList[i]) <= 120000):
                pairsList.append((sitesList[i], sitesList[j])) # if between 80-120 kbp away, append pair to list

    return pairsList

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str, help="Input Fasta file")
    parser.add_argument("sequence", type=str, help="Sequence to search for")
    args = parser.parse_args()

    cuts = find_cuts(args.input, args.sequence) # find list of cuts
    pairs = find_pairs(cuts) # find distance pairs

    outputFile = '/mnt/c/Users/wammi/OneDrive/Desktop/datasci217/05-first-exam-samkchan815/results/cutsite_summary.txt'

    # output results in output file
    with open(outputFile, 'w') as file:
        file.write(f'Analyzing cut site: {args.sequence}\n')
        file.write(f'Total cut sites found: {len(cuts)}\n')
        file.write(f'Cut site pairs 80-120 kbp apart: {len(pairs)}\n')
        file.write(f'First 5 pairs:\n')
        
        for i in range(0, 5):
            file.write(f'{i+1}. {pairs[i][0]} - {pairs[i][1]}\n')

    file.close()



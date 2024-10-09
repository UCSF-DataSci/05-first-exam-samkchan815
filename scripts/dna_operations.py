import argparse
compDict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'} #dictionary used to find complement

def complement(seq):
    compSeq = '' 
    for i in seq:
        if i in compDict:
            compSeq += compDict[i] #take the complement

    return compSeq

def reverse(seq):
    revSeq = seq[::-1]
    return revSeq

def reverse_complement(seq):
    compSeq = '' 
    revCompSeq = ''
    for i in seq:
        if i in compDict:
            compSeq += compDict[i] #take the complement
    revCompSeq = compSeq[::-1] #reverse the complement sequence
    return revCompSeq

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str, help="Input DNA sequence")
    args = parser.parse_args()
     
    seq = str(args.input)
    comp = complement(seq)
    rev = reverse(seq)
    revComp = reverse_complement(seq)

    print("Original sequence: ", seq)
    print("Complement: ", comp)
    print("Reverse: ", rev)
    print("Reverse complement: ", revComp)
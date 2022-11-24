#Anya Wilkinson

testsequence = "ACGTACGTACGT"

aminoacids = {"UUU":"Phenylalanine", "UUC":"Phenylalanine", "UUA":"Leucine", "UUG":"Leucine", "UCU":"Serine", "UCC":"Serine", "UCA":"Serine", "UCG":"Serine", "UAU":"Tyrosine", "UAC":"Tyrosine", 'UAA':'STOP', 'UAG':'STOP', 'UGU':'Cysteine', 'UGC':'Cysteine','UGA':'STOP', 'UGG':'Tryptophan', 'CUU':'Leucine', 'CUC':'Leucine', 'CUA':'Leucine', 'CUG':'Leucine', 'CCU':'Proline', 'CCC':'Proline', 'CCA':'Proline', 'CCG':'Proline', 'CAU':'Histidine', 'CAC':'Histidine', 'CAA':'Glutamine', 'CAG':'Glutamine', 'CGU':'Arginine', 'CGC':'Arginine', 'CGA':'Arginine', 'CGG':'Arginine', 'AUU':'Isoleucine', 'AUC':'Isoleucine', 'AUA':'Isoleucine', 'AUG':'Methionine', 'ACU':'Threonine', 'ACC':'Threonine', 'ACA':'Threonine', 'ACG':'Threonine', 'AUU':'Asparagine', 'AUC':'Asparagine', 'AAA':'Lysine', 'AAG':'Lysine', 'AGU':'Serine', 'AGC':'Serine', 'AGA':'Arginine', 'AGG':'Arginine', 'GUU':'Valine', 'GUC':'Valine', 'GUA':'Valine', 'GUG':'Valine', 'GCU':'Alanine', 'GCC':'Alanine', 'GCA':'Alanine', 'GCG':'Alanine', 'GAU':'Aspartic Acid', 'GAC':'Aspartic Acid', 'GAA':'Glutamic Acid', 'GAG':'Glutamic Acid', 'GGU':'Glycine', 'GGC':'Glycine', 'GGA':'Glycine', 'GGG':'Glycine'}
aminoSLC = {'Isoleucine':'I', 'Leucine':'L', 'Valine':'V', 'Phenylalanine':'F', 'Methionine':'M', 'Cysteine':'C', 'Alanine':'A', 'Glycine':'G', 'Proline':'P', 'Threonine':'T', 'Serine':'S', 'Tyrosine':'Y', 'Tryptophan':'W', 'Glutamine':'Q', 'Asparagine':'N', 'Histidine':'H', 'Glutamic acid':'E', 'Aspartic acid':'D', 'Lysine':'K', 'Arginine':'R', 'STOP':'Stop'}
nucleotides = ['A', 'C', 'G', 'T']
nucleotidecount = {'A':0, 'C':0, 'G':0, 'T':0}
compliment = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

def basicanalysis(sequence):
    #length
    length = len(sequence)
    print("BP count:", length, "nucleotides")
    #nucleotide count
    for char in sequence:
        if char in nucleotides: #sometimes N is included if the base in unknown
            nucleotidecount[char] += 1
    print("Nucleotide count:", nucleotidecount)
    #GC%
    G = nucleotidecount.get('G')
    C = nucleotidecount.get('C')
    GC = G + C
    proportion = (GC / length)*100
    print("GC%:", proportion, "%")
    return length, nucleotidecount, GC
    
def complimentarysequence(sequence):
    #give complementary DNA sequence
    newseq = ""
    for char in sequence:
        newseq = newseq + compliment[char]
    print("Complimentary sequence:", newseq)
    return newseq    

def rnatemplate(sequence):
    #return the corresponding RNA sequence to the DNA
    #requires knowledge on if the DNA is template or coding
    #same as complimentarysequence but uses uracil instead of thymine
    rnaseq = ""
    strand = input("Is this DNA sequence the template or coding strand? If you aren't sure, write 'coding'.")
    strand.lower()
    if strand == "coding":
        for char in sequence:
            if char == 'A':
                rnaseq = rnaseq + 'U'
            if char == 'T':
                rnaseq = rnaseq + 'A'
            if char == 'G':
                rnaseq = rnaseq + 'C'
            if char == 'C':
                rnaseq = rnaseq + 'G'
    if strand == "template":
        for char in sequence:
            if char == 'T':
                rnaseq = rnaseq + 'U'
            else:
                rnaseq = rnaseq + char
    print("mRNA sequence from", strand, "strand:", rnaseq)
    return rnaseq
    
def translation(sequence):
    #rna to amino acid
    #must run rnatemplate first
    position1 = [sequence[i:i+3] for i in range(0, len(sequence),3)] #https://stackoverflow.com/questions/9475241/split-string-every-nth-character
    sequence2 = sequence[1:]
    position2 = [sequence2[i:i+3] for i in range(0, len(sequence2),3)]
    sequence3 = sequence[2:]
    position3 = [sequence3[i:i+3] for i in range(0, len(sequence3),3)]
    #the positions are to keep track of the different possible starting positions, from the 0-2 character of the rna string
    '''
    while index < (len(sequence)):
        
        if index < (len(sequence)-2):
            if sequence[index] + sequence[index+1] + sequence[index+2] in aminoacids:
                output = output + double_vowels.get((string[index] + string[index+1]))
                output = output + '-'
                index = index + 2
    '''                
    #position 1
    aminotranslation1 = []
    for codon in position1:
        if codon in aminoacids:
            aminotranslation1.append(aminoacids[codon])
        else:
            aminotranslation1.append('_')
    #[sequence[i:i+3] for i in range(0, len(sequence),3)] #https://stackoverflow.com/questions/9475241/split-string-every-nth-character

    print(position1)
    print(position2)
    print(position3)
    print(aminotranslation1)
    
    pass
    return aminotranslation1

def aminoSLC(sequence):
    SLC = ""
    for acid in aminotranslation1:
        SLC = SLC + aminoSLC[acid]        
    return SLC

sequence = input("Enter a DNA sequence.")
sequence = sequence.upper()
#basicanalysis(sequence)
#testing changes to see how github works
x= rnatemplate(sequence)
#complimentarysequence(sequence)
y= translation(x)
#aminoSLC(y)

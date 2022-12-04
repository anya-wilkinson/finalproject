#Anya Wilkinson

testsequence = "ACGTACGTACGT"

aminoacids = {"UUU":"Phenylalanine", "UUC":"Phenylalanine", "UUA":"Leucine", "UUG":"Leucine", "UCU":"Serine", "UCC":"Serine", "UCA":"Serine", "UCG":"Serine", "UAU":"Tyrosine", "UAC":"Tyrosine", 'UAA':'STOP', 'UAG':'STOP', 'UGU':'Cysteine', 'UGC':'Cysteine','UGA':'STOP', 'UGG':'Tryptophan', 'CUU':'Leucine', 'CUC':'Leucine', 'CUA':'Leucine', 'CUG':'Leucine', 'CCU':'Proline', 'CCC':'Proline', 'CCA':'Proline', 'CCG':'Proline', 'CAU':'Histidine', 'CAC':'Histidine', 'CAA':'Glutamine', 'CAG':'Glutamine', 'CGU':'Arginine', 'CGC':'Arginine', 'CGA':'Arginine', 'CGG':'Arginine', 'AUU':'Isoleucine', 'AUC':'Isoleucine', 'AUA':'Isoleucine', 'AUG':'Methionine', 'ACU':'Threonine', 'ACC':'Threonine', 'ACA':'Threonine', 'ACG':'Threonine', 'AUU':'Asparagine', 'AUC':'Asparagine', 'AAA':'Lysine', 'AAG':'Lysine', 'AGU':'Serine', 'AGC':'Serine', 'AGA':'Arginine', 'AGG':'Arginine', 'GUU':'Valine', 'GUC':'Valine', 'GUA':'Valine', 'GUG':'Valine', 'GCU':'Alanine', 'GCC':'Alanine', 'GCA':'Alanine', 'GCG':'Alanine', 'GAU':'Aspartic Acid', 'GAC':'Aspartic Acid', 'GAA':'Glutamic Acid', 'GAG':'Glutamic Acid', 'GGU':'Glycine', 'GGC':'Glycine', 'GGA':'Glycine', 'GGG':'Glycine'}
aminoSLC = {'Isoleucine':'I', 'Leucine':'L', 'Valine':'V', 'Phenylalanine':'F', 'Methionine':'M', 'Cysteine':'C', 'Alanine':'A', 'Glycine':'G', 'Proline':'P', 'Threonine':'T', 'Serine':'S', 'Tyrosine':'Y', 'Tryptophan':'W', 'Glutamine':'Q', 'Asparagine':'N', 'Histidine':'H', 'Glutamic Acid':'E', 'Aspartic Acid':'D', 'Lysine':'K', 'Arginine':'R', 'STOP':'Stop', '_':'_'}
nucleotides = ['A', 'C', 'G', 'T']
compliment = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

def basicanalysis(sequence):
    #length
    length = len(sequence)
    #print("BP count:", length, "nucleotides")
    #nucleotide count
    nucleotidecount = {'A':0, 'C':0, 'G':0, 'T':0}
    for char in sequence:
        if char in nucleotides: #sometimes N is included if the base in unknown
            nucleotidecount[char] += 1
    #print("Nucleotide count:", nucleotidecount)
    #GC%
    G = nucleotidecount.get('G')
    C = nucleotidecount.get('C')
    GC = G + C
    proportion = (GC / length)*100
    #print("GC%:", proportion, "%")
    return length, nucleotidecount, GC
    
def complimentarysequence(sequence):
    #give complementary DNA sequence
    newseq = ""
    for char in sequence:
        if char in compliment:
            newseq = newseq + compliment[char]
    #print("Complimentary sequence:", newseq)
    return newseq    

def rnatemplate(sequence, strand):
    #return the corresponding mRNA sequence to the DNA
    #requires knowledge on if the DNA is template or coding
    #same as complimentarysequence but uses uracil instead of thymine
    rnaseq = ""
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
    #print("mRNA sequence from", strand, "strand:", rnaseq)
    return rnaseq
    
def translation(sequence):
    #rna to amino acid
    #must run rnatemplate first
    position1 = [sequence[i:i+3] for i in range(0, len(sequence),3)] #https://stackoverflow.com/questions/9475241/split-string-every-nth-character
    sequence2 = sequence[1:]
    position2 = [sequence2[i:i+3] for i in range(0, len(sequence2),3)]
    sequence3 = sequence[2:]
    position3 = [sequence3[i:i+3] for i in range(0, len(sequence3),3)]
    #the positions are to keep track of the different possible starting positions, from the 0-2 character of the rna string.
    #this is because when sequencing the DNA, you don't know where the codons are supposed to be starting from / what position they are in to be read. 
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
    #position 2
    aminotranslation2 = []
    for codon in position2:
        if codon in aminoacids:
            aminotranslation2.append(aminoacids[codon])
        else:
            aminotranslation2.append('_')
    #position 3
    aminotranslation3 = []
    for codon in position3:
        if codon in aminoacids:
            aminotranslation3.append(aminoacids[codon])
        else:
            aminotranslation3.append('_')

    #to pick which position to use:
    #note to self: here try to read the stuff to see if any of the three reads have a start codon (met) or stop codon
    #maybe just return that one as the most likely but still return all three ???
    #use my PLH data to test which reads are the most successful most of the time

    x = acidtoSLC(aminotranslation1)
    y = acidtoSLC(aminotranslation2)
    z = acidtoSLC(aminotranslation3)
    
    if 'Stop' in z and 'Stop' in y:
        finalaminotranslation = x
    elif 'Stop' in z and 'Stop' in x:
        finalaminotranslation = y
    elif 'Stop' in x and 'Stop' in y:
        finalaminotranslation = z
    else:
        if 'Stop' in z:
            finalaminotranslation = [x,y]
        elif 'Stop' in y:
            finalaminotranslation = [x,z]
        elif 'Stop' in x:
            finalaminotranslation = [y,z]
        else:
            finalaminotranslation = [x,y,z]
    #print(finalaminotranslation)
    return finalaminotranslation

def acidtoSLC(sequence):
    SLC = ""
    for acid in sequence:
        SLC = SLC + aminoSLC[acid]        
    #print(SLC)
    return SLC



'''
sequence = input("Enter a DNA sequence.")
#reference = input("Enter the given amino acid SLC for testing the function.")
sequence = sequence.upper()
basicanalysis(sequence)
complimentarysequence(sequence)
x= rnatemplate(sequence)
print(reference)
translation(x)
'''

########################
#nonfunction and the actual stuff starts here

data = open("PythonSampleDNA.csv.csv", 'r') 
sample = data.readlines()

output = open("PythonSampleOutput.csv.csv", 'w')

#create a header for the file here
output.write("Original Sequence,Length,Adenine,Cytosine,Guanine,Thymine,GC,Complimentary DNA Seq, mRNA, Amino Acid, AA Possibility 2 (if applicable), AA Possibility 3 (if applicable)")
output.write('\n')
print("Welcome to DNASA, the DNA Sequence Analyzer!")
strand = input("Are your DNA sequences template or coding strands? If unsure, write 'template'.")
print("Analyzing in progress...")

for seq in sample[:]:
    seq = seq[:-8] #get rid of the PLH label that i added to keep track of my sample DNA data

    #run analysis and assign it to variables, also making everything a str so it can be written in a file
    l, m, n = basicanalysis(seq)
    o = complimentarysequence(seq)
    p = rnatemplate(seq, strand)
    q = translation(p)
    l = str(l)
    m = (str(m))[1:-1]
    n = str(n) + "%"
    q = str(q)

    #writing the analysis in the file
    output.write(seq)
    output.write(',')
    output.write(l)
    output.write(',')
    output.write(m)
    output.write(',')
    output.write(n)
    output.write(',')
    output.write(o)
    output.write(',')
    output.write(p)
    output.write(',')
    output.write(q)

    #new line to seperate for each DNA sequence
    output.write('\n')

print("Thank you for using DNASA. Your DNA Analysis is ready in your chosen output file.")
    
output.close()
data.close()




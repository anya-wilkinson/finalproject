
#Anya Wilkinson

testsequence = "ACGTACGTACGT"

aminoacids = {}
aminoSLC = {'isoleucine':'I', 'Leucine':'L', 'Valine':'V', 'Phenylalanine':'F', 'Methionine':'M', 'Cysteine':'C', 'Alanine':'A', 'Glycine':'G', 'Proline':'P', 'Threonine':'T', 'Serine':'S', 'Tyrosine':'Y', 'Tryptophan':'W', 'Glutamine':'Q', 'Asparagine':'N', 'Histidine':'H', 'Glutamic acid':'E', 'Aspartic acid':'D', 'Lysine':'K', 'Arginine':'R', 'Stop':'Stop'}
nucleotides = ['A', 'C', 'G', 'T']
nucleotidecount = {'A':0, 'C':0, 'G':0, 'T':0}
compliment = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

def basicanalysis(sequence):
    #length
    length = len(sequence)
    print("BP count:", length, "nucleotides")
    #nucleotide count
    for char in sequence:
        if char in nucleotides:
            nucleotidecount[char] += 1
    print("Nucleotide count:", nucleotidecount)
    #GC%
    G = nucleotidecount.get('G')
    C = nucleotidecount.get('C')
    GC = G + C
    proportion = (GC / length)*100
    print("GC%:", proportion, "%")
    
def complimentarysequence(sequence):
    #give complementary DNA sequence
    pass    
    
def translation(sequence):
    #dna to amino acid
    pass


#basicanalysis("AGGTGTTGGATTCAAAGCTGGTGTCAAGGATTACCGATTGACCTATTACACCCCCGAATACAAGACCAAAGATACCGACATCTTGGCAGCCTTCCGGATGACCCCACAACCCGGGGTACCAGCTGAGGAAGCCGGAGCTGCGGTAGCTGCGGAATCCTCCACGGGTA")
#testing changes to see how github works

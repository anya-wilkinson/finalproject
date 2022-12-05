# finalproject
DNASA: DNA Sequence Analyzer

The purpose of DNASA is to complete the first steps of DNA analysis for a researcher. 
It takes in a file of DNA sequences, analyzes all of the sequences in the file, and then writes a new file with that information.

The analysis elements included are: length of the sequence, the count of each nucleotide, the proportion of guanine-cytosine (GC) content, the complimentary DNA sequence, the corresponding mRNA sequence, and an amino acid translator. 

The mRNA piece requires input from the user on if the DNA sequences in the file are template or coding strands, since that affects what the mRNA code is supposed to be. 

The amino acid translator uses the mRNA sequence and reads the sequence in three characters at a time (a codon, which is composed of three nucleotides), finding the corresponding amino acid, and adding that to a string. 
Since there are three possible reads for an amino acid (starting the sequence at position 1, 2, or 3 in codon, which is unknown for this level of analysis), this function returns up to three possible amino acid sequences. 
If a 'stop' codon is included in any of the amino acid chains, that chain is not included in the written file since it can be ruled out as an unlikely option for the actual amino acid chain. 
This gives the researcher the more likely amino acid sequences, usually 1 or 2 but occasoinally 3 possibilities. 
This piece was the most difficult part of the analysis. Determining the correct amino acid chain isn't really capable through this kind of code, and would require outside sources or background knowledge of the proteins / what the amino acid chain is supposed to be. I tried a few different ways of choosing the best sequence. Most of the sample DNA I had had an amino acid code only using the first read, but there were a couple where this didn't work, which I why I then had to add the second and third reads. I have no way of knowing which is the correct one, so I thought the the next best option would be to only return the more likely reads; or rather, removing the least likely reads. So, I decided that any with a 'stop' codon were less likely to be the correct amino acid for a given DNA strand, and that would be the determining factor to uninclude it from the final results.

Originally, DNASA was going to connect to an outside database called BLAST (from NIH/NCBI), but that ended up being outside of my capabilities and also required a lot of other modules for python that I didn't know how to use. I had trouble locating an updated or usable API for BLAST, and also all of the documentation I could track down was in other coding languages (like perl???). 
To make up for this, I added the file reading and writing capabilities to DNASA. I had to learn how to write files, since we didn't practice that much in class, and we had focused on file reading. 

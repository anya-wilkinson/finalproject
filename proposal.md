# Proposal

## What will (likely) be the title of your project?

DNA Sequence Analyzer (DNASA)

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

A program that takes in a DNA sequence and does some of the sequence analysis for the researcher. It will include the basic stats for DNA analysis and possibly some more complicated analysis on origin.

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

DNASA is inspired by biological research I did last year and our Hawaiian lab. I worked with many DNA sequences and fragments and had to analyze them for my project in multiple ways, and most of that had to be done manually. My goal for this is to accomplish what I had to manually do for all my sequences. It will take in a DNA sequence and find the length of the sequence, the nucleotide counts, the GC% (G and C pair together, so you get a sense of the proportion of GC to AT), and the translation into the amino acid sequence. If possible, I want to use an API to connect to the NIH database and return the most likely source of the DNA (genus or species).

## If planning to combine 1051's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to 1051, and which aspect(s) would relate to the other course?

TODO, if applicable (n/a)

## If planning to collaborate with 1 or 2 classmates for the final project, list their names, email addresses, and the names of their assigned TAs below.

TODO, if applicable (mostly n/a, but I will be learning how to use API's from my sister (tajwilk@terpmail.umd.edu). she won't be making any of the project's code though)

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

the basic DNA analysis: length, nucleotide count, GC%. if i can't figure out the harder stuff then i will find more analysis features to add.

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

the amino acid translation (this is not as simple as the hawaiian translator because you don't know the starting position in the amino acid code (three nucleotides), unlike the hawaiian word which starts at the first character. you have to make three translations (for each possible starting position) and then figure out which is the most likely to be correct.) also, maybe reading my files for the DNA sequences instead of just inputting a single sequence.

### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

using BLAST (NIH database) API to find the most likely genera and species for the sequence. (this was the goal of my project last year and the majority of the manual analysis I had to do.) if this doesn't work out i may try to expand on the file reading piece,  take in a bunch of sequences at once, and then write a new file that includes each sequence and the analysis results instead of just returning/printing the results of a single sequence.

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

the basic features should be pretty easy and will be my starting place. the "better" features should be okay as well, with some trial and error on the amino-acid part. i expect that will take me a good bit of time, and i want to do that before trying to do the "best" pieces. to achieve the "best" outcome I need to learn what exactly an API is and how to use it. my sister (student at UMD) suggested this part of my project and said she would show me how to use APIs, but i will also research them too. if the API stuff is too complicated or i really just don't understand it, then i will pivot to focus on file reading and writing and making a program that takes in many sequences for analysis.

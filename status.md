# Status Report

#### Your name

Anya Wilkinson

#### Your section leader's name

Xinwen Zhang

#### Project title

DNASA (DNA Sequence Analyzer)

***

Short answers for the below questions suffice. If you want to alter your plan for your project (and obtain approval for the same), be sure to email your section leader directly!

#### What have you done for your project so far?

i have completed the basic analysis function, complementary sequence func, DNA to mRNA func, and I have a working version of the amino acid translation function, as well as an amino acid names to single letter code (slc) func.

#### What have you not done for your project yet?

i have to refine the amino acid translator to try and distinguish between the three possible reads of the DNA sequence. since the BLAST/API stuff isn't working i may also add file reading or writing.

#### What problems, if any, have you encountered?

i was going to use the API of an online tool/database from NIH called BLAST to try and analyze the DNA to return a specific organism or genus or soemthing, but once I looked more into it i found that their API is deprecated. they mostly want researchers to connect it to the cloud or just stick to the website, and all of the instructions and examples I found are in other coding languages, but nothing with python or any new version of an API, so it's outside my capabilities. 
i'm also having trouble trying to figure out how to choose which amino acid translation is the correct one. my current plan is to run my program using DNA sequences that I already have because I have the amino acids for that too, so I can try to see which of the reads is the most likely or most common. i may have to return all three possibilities if i can't figure out which is correct. there isn't a set rule for it, so it's not really something i can easily code to do, because it just depends on what's right or not.
i forgot that to go from DNA to amino acids you have to find the mRNA first, so I added an mRNA translation function that runs before the amino acid translation.
as i was making the mRNA function, i also realized i hadn't considered whether the input DNA was the coding strand or the temple strand (this affects mRNA as it is the compliment of the coding strand but almost exactly the same as the temple strand (just with uracil) and thus would affect the amino acids too). there isn't a way to differentiate coding vs temple based on the DNA sequence alone, so i decided to make it up to the researcher to input whether it was coding or template.

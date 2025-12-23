#project title:DNA to Protein Translator with Codon Awareness
from Bio import SeqIO
def translate_sequence(seq):
    # TRIM SEQUENCE TO FULL CODONS-
    trimmed_len = len(seq)- (len(seq)%3)
    seq = seq[:trimmed_len]

    frames = []
    for i in range(3):
        protein = seq[i:].translate(to_stop = True)
        frames.append(protein)
    return frames
for record in SeqIO.parse(r"C:\Users\Amit Sahu\Desktop\git_projects\biopython_projects\biopython3\data\sample_sequences.fasta","fasta"):
    dna = record.seq
    print("SEQUENCE ID: ",record.id)
    print("DNA: ",dna)
    frames = translate_sequence(dna)
    for i ,protein in enumerate(frames , start=1):
        print(f"frame{i} Protein:",protein)
    print("-"*40)
                          

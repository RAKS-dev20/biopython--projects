with open("data.fasta", "w") as f:
    f.write(""">seq1_human_gene
ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG

>seq2_mouse_gene
ATGCGTACGTAGCTAGCTAGCTAGCTAACG

>seq3_bacterial_gene
ATGACGACGACGTTAGCGTAGCTAGGCTAA

>seq4_viral_gene
ATGTTTGGGAAACCCGGGTTTAA
""")
print("FASTA file 'data.fasta' created with sample sequences.")
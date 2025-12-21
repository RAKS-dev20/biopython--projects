dna = input("enter your DNA sequence: ").upper()
count = {"A": dna.count("A"),"T":dna.count("T"),"G":dna.count("G"),"C":dna.count("C")}
print(count)
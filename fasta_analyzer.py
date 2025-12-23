

from Bio import SeqIO

input_fasta = "data.fasta"
output_file = "analysis_report.txt"

total_sequences = 0
with open(output_file,"w") as output:
  output.write("Sequence_ID\tLength\tGC_content(%)\tAC_content(%)\n")
  for record in SeqIO.parse(input_fasta,"fasta"):
      total_sequences += 1
      seq_length = len(record.seq)
      gc_conent = (record.seq.count("G")+record.seq.count("C"))/seq_length*100

      output.write(f"{record.id}\t{seq_length}\t{gc_conent:.2f}\n")
  print("Total sequence analysed:",total_sequences)
  print("Results saved in analysis_report.txt")
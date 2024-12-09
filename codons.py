def create_codon_dict(file_path):
  file= open(file_path)
  rows= file.readlines()
  file.close()
  codon_dict={}
  for row in rows:
    row= row.strip().split('\t')
    codon= row[0]
    amino_acid= row[2]
    codon_dict[codon]= amino_acid
  return codon_dict

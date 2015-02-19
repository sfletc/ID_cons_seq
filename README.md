# ID_cons_seq
Identifies ultra-conserved regions of a set length in multiple sequences (eg. viral or bacterial genomes).  Used for identification of artificial microRNA target sites, and to ensure minimal off-target effects

Usage:

No command line parser - run in iPython

%run id_cons_seq.py

longest_com_seq(input_seq_fasta_file_name, target_length)

Example output:

longest_com_seq('input.fa', 23)

Max conserved seq. len. = 14 nt

1 seqs identified of length 23 are present in 27 reference sequences:

Seq = ATGCGCTATGCATGCGCTCATCG

Reference = >1 at position [4665]
Reference = >2 at position [9761]
Reference = >3 at position [9210]
Reference = >4 at position [9995]
Reference = >5 at position [3441]

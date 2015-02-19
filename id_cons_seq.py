import get_ref
"""
Set conserved region sequence length (ie. 21nt)
Script returns all sequences of that length that
appear in all provided refernce sequences, 
along with their positions in each

Default window length = 21
"""

def get_sub_seqs(ref_file, window):
	seq_lib = {}
	cons_seq = []

	pos = 0



	ref_seq = get_ref.get_ref_f_strand(ref_file)

	for header,seq in ref_seq.iteritems():

		pos = 0
		while pos < (len(seq)-window):  #fix this so stops in correct place
			sub_seq = seq[pos:pos+window]

			if sub_seq not in seq_lib:

				seq_lib[sub_seq]={header:[pos]}
			elif header in seq_lib[sub_seq]:
				seq_lib[sub_seq][header].append(pos)
			elif sub_seq in seq_lib and header not in seq_lib[sub_seq]:
				seq_lib[sub_seq][header] = [pos]
			elif complement(sub_seq) in seq_lib and header not in seq_lib[sub_seq]:
				seq_lib[sub_seq][header] = [pos]
			else:
				pass
			pos +=1

	for sub_seq, occurences in seq_lib.iteritems():
		if len (occurences) == len (ref_seq):
			cons_seq.append((sub_seq,occurences))
	return cons_seq

# def get_most_sub_seqs(ref_file, window, portion):
# 	seq_lib = {}
# 	cons_seq = []

# 	pos = 0



# 	ref_seq = get_ref.get_ref_f_strand(ref_file)

# 	for header,seq in ref_seq.iteritems():
# 		pos = 0
# 		while pos < (len(seq)-window):  #fix this so stops in correct place
# 			sub_seq = seq[pos:pos+window]

# 			if sub_seq not in seq_lib:

# 				seq_lib[sub_seq]={header:[pos]}
# 			elif header in seq_lib[sub_seq]:
# 				seq_lib[sub_seq][header].append(pos)
# 			elif sub_seq in seq_lib and header not in seq_lib[sub_seq]:
# 				seq_lib[sub_seq][header] = [pos]
# 			elif complement(sub_seq) in seq_lib and header not in seq_lib[sub_seq]:
# 				seq_lib[sub_seq][header] = [pos]
# 			else:
# 				pass
# 			pos +=1

# 	for sub_seq, occurences in seq_lib.iteritems():

# 		if float(len(occurences)) / len(ref_seq) > portion:
# 			cons_seq.append((sub_seq,occurences))
# 	return cons_seq

def get_most_sub_seqs(ref_file, window=21):
	seq_lib = {}
	cons_seq = []

	pos = 0



	ref_seq = get_ref.get_ref_f_strand(ref_file)

	for header,seq in ref_seq.iteritems():
		pos = 0
		while pos < (len(seq)-window):  #fix this so stops in correct place
			sub_seq = seq[pos:pos+window]

			if sub_seq not in seq_lib:

				seq_lib[sub_seq]={header:[pos]}
			elif header in seq_lib[sub_seq]:
				seq_lib[sub_seq][header].append(pos)
			elif sub_seq in seq_lib and header not in seq_lib[sub_seq]:
				seq_lib[sub_seq][header] = [pos]
			elif complement(sub_seq) in seq_lib and header not in seq_lib[sub_seq]:
				seq_lib[sub_seq][header] = [pos]
			else:
				pass
			pos +=1
	cons_seq=[(0,{1:2})]
	set_length = 1
	for sub_seq, occurences in seq_lib.iteritems():

		if len(occurences) > len(cons_seq[0][1]):

			cons_seq=[(sub_seq,occurences)]
			set_length = len(occurences)
		
		elif len(occurences) == set_length and set_length > 1:
			cons_seq.append((sub_seq,occurences)) 


	return cons_seq


def longest_com_seq(ref_seq, window = 21):
	max_len = 1
	i=1
	stop_iterating = 25
	
	for i in range(stop_iterating):
		cons_seqs = get_sub_seqs(ref_seq,i)

		if len(cons_seqs) != 0:
			max_len = i
			i+=1
			best_cons_seqs = cons_seqs
		else:
			
			break
	# most_max_len = 1
	# i=1
	# stop_iterating = 25
	
	# for i in range(stop_iterating):
	# 	cons_seqs = get_most_sub_seqs(ref_seq,i, portion)

	# 	if len(cons_seqs) != 0:
	# 		most_max_len = i
	# 		i+=1
	# 		most_cons_seqs = cons_seqs
	# 	else:
			
	# 		break
	refs_covered=[]
	best_cons_seqs = get_most_sub_seqs(ref_seq,window)
	print '\nMax conserved seq. len. = {0} nt'.format(max_len)
	print '\n{0} seqs identified of length {1} are present in {2} reference sequences:'.format(len(best_cons_seqs ), window, len(best_cons_seqs[0][1]))
	for seq in best_cons_seqs:
		print "\nSeq = {0}\n".format(seq[0])
		for key,value in seq[1].iteritems():
			print "Reference = {0} at position {1}".format(key,value)
			if key not in refs_covered:

				refs_covered.append(key)
	print '\nCovering {0} reference sequences'.format(len(refs_covered))
	# print 'Seq. len. = {0} nt conserved in {1} percent of sequences'\
	# .format(most_max_len,(portion * 100))



def complement(sequence):
    """Provides the complement in the 5' - 3' direction

    Assumption: reference consists of A, G, C, T only

    complement(str) --> str
    """
    d = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return DNA(''.join(d[c] if c in d else c for c in reversed(self)))


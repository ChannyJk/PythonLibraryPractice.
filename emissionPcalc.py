import sys

tot_seq_len = 0
aa_count = {}
aa_list = ['G', 'A', 'V', 'C', 'P', 'L', 'I', 'M', 'W',
           'F', 'K', 'R', 'H', 'S', 'T', 'Y', 'N', 'Q', 'D', 'E']

with open(sys.argv[1]) as READ:
    for line in READ:
        tot_seq_len += len(line.strip())
        
        for Nu in line.strip():
            if Nu not in aa_count:
                aa_count[Nu] = 0
            else: 
                aa_count[Nu] += 1

f = open(sys.argv[1][:-4] + '_aa_freq.txt', 'w')

for aa in aa_list:
    freq = aa_count[aa] / tot_seq_len
    f.write('{0}:{1}\n'.format(aa, freq))

f.close()





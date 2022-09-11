import numpy as np 
import pandas as pd 

my_Arr = np.zeros((2,20))
columns_name = ['G', 'A', 'V', 'C', 'P', 'L', 'I', 'M', 'W','F', 'K', 'R', 'H', 
                'S', 'T', 'Y', 'N', 'Q', 'D', 'E']
index_name = ['S', 'T']
Emi_P = pd.DataFrame(my_Arr, columns = columns_name, index = index_name)

re_s = open('soluble_sequences_aa_freq.txt', 'r')

for line in re_s:
    aa_ = line.split(':')[0].strip()
    Emi_P.at['S',aa_] = float(line.split(':')[1].strip())

re_t = open('transmembrane_sequences_aa_freq.txt', 'r')

for line in re_t:
    aa_ = line.split(':')[0].strip()
    Emi_P.at['T',aa_] = float(line.split(':')[1].strip())

f = open('state_sequences_state_freq.txt', 'r')
trs_dict = {}

for line in f:
    if 'S' == line.split(':')[0].strip() :
        S_beginP = line.split(':')[1].strip()
    elif 'T' == line.split(':')[0].strip():
        T_beginP = line.split(':')[1].strip()
    elif len(line.split(':')[0].strip()) == 2:
        trs_dict[line.split(':')[0].strip()] = float(line.split(':')[1].strip())

seq_input = input('INSERT Polypeptide Sequence : ')
viterbi_begin = 1.0

state_path = {'S' : viterbi_begin * float(S_beginP) * Emi_P.at['S',seq_input[0]],
              'T' : viterbi_begin * float(T_beginP) * Emi_P.at['T',seq_input[0]]}

possible_state = ['S', 'T']

for i in range(1, len(seq_input)):
    kv = list(state_path.items())
    state_path.clear()
    for j in possible_state:
        left_ = kv[0][1] * trs_dict[kv[0][0][-1]+j] * Emi_P.at[j, seq_input[i]]
        right_ = kv[1][1] * trs_dict[kv[1][0][-1]+j] * Emi_P.at[j, seq_input[i]]
        if left_ > right_:
            state_path[kv[0][0]+j] = left_
        else:
            state_path[kv[1][0]+j] = right_

t = open('viterbi_statepath.txt', 'w')

kv = list(state_path.items())
if kv[0][1] > kv[1][1]:
    t.write('The Hidden State Path is : {0}'.format(kv[0][0]))
else:
    t.write('The Hidden State Path is : {0}'.format(kv[1][0]))


re_s.close()
re_t.close()
f.close()
t.close()

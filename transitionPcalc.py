import sys

tot_seq_len = 0
SN_count = 0
TN_count = 0
Transition_Matrix = {}
state_count = {}


with open(sys.argv[1]) as READ:
    for line in READ:
        tot_seq_len += len(line.strip())

        for st in line:
            if st not in state_count:
                state_count[st] = 0
            else:
                state_count[st] += 1

        for pos in range(0, len(line.strip())-1):
            fr = line.strip()[pos:pos+2]
            if fr not in Transition_Matrix:
                Transition_Matrix[fr] = 0
            else:
                Transition_Matrix[fr] += 1

            if fr[0] == 'S':
                SN_count += 1
            else: 
                TN_count += 1

f = open(sys.argv[1][:-4] + '_state_freq.txt', 'w')

Transition_Matrix['TT'] /= state_count['T']
Transition_Matrix['TS'] /= state_count['T']
Transition_Matrix['SS'] /= state_count['S']
Transition_Matrix['ST'] /= state_count['S']

S_freq = state_count['S'] / tot_seq_len
T_freq = state_count['T'] / tot_seq_len 
f.write('{0}:{1}\n'.format('S', S_freq))
f.write('{0}:{1}\n'.format('T', T_freq))
f.write('{0}:{1}\n'.format('TT', Transition_Matrix['TT']))
f.write('{0}:{1}\n'.format('TS', Transition_Matrix['TS']))
f.write('{0}:{1}\n'.format('SS', Transition_Matrix['SS']))
f.write('{0}:{1}\n'.format('ST', Transition_Matrix['ST']))

f.close()

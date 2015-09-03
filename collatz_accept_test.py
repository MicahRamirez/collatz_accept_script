import random 

f = open('./bad_numbers.txt', 'r')
bad_map = {}

for line in f:
    b_num = int(line.strip('\n'))
    bad_map[b_num] = 0

f.close()

#file_write = open('./acceptance_test.txt','w')


#where n is an integer
def cycle_length(n):
    cyc_len = 0
    while(n > 1):
        if(n % 2 == 0):
            n = n >> 1
        else:
            n = (n << 1) + n + 1
        cyc_len += 1
    return cyc_len

#preferred input is where n < k
#determines the max cycle length in a range
def range_cyc_length(n , k ):
    if n > k:
        swap = n
        n = k
        k = swap
    max_cyc = 0
    #k + 1 because need inclusive
    for i in range(n, k + 1):
        cur_cyc = cycle_length(i)
        if(max_cyc < cur_cyc):
            max_cyc = cur_cyc
    return max_cyc

collatz_in = open('./XMR73-RunCollatz.in', 'w')
collatz_out = open('./XMR73-RunCollatz.out','w')

for i in range(0, 150):
    n = random.randint(0, 1000000)
    k = random.randint(0, 1000000)
    while(n in bad_map):
        n = random.randint(0, 1000000)

    while(k in bad_map):
        k = random.randint(0, 1000000)

    max_cycl_length = range_cyc_length(n, k)
    write_in = str(n) + ' ' + str(k) + '\n'
    collatz_in.write(write_in)
    write_out = str(n) + ' ' + str(k) + ' ' + str(max_cycl_length) + '\n'
    collatz_out.write(write_out)

collatz_in.close()
collatz_out.close()




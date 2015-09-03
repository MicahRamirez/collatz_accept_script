import random 

f = open('./bad_numbers.txt', 'r')
bad_map = {}

for line in f:
    b_num = int(line.strip('\n'))
    bad_map[b_num] = 0

f.close()

#file_write = open('./acceptance_test.txt','w')

#lazy cache
cyc_cache = {}
bad_list = list(bad_map.keys())
bad_list.sort()

#where n is an integer
def cycle_length(n):
    init_num = n
    cyc_len = 0
    while(n > 1):
        if(n % 2 == 0):
            n = n >> 1
        else:
            n = (n << 1) + n + 1
        cyc_len += 1
    cyc_cache[init_num] = cyc_len
    return cyc_len

#preferred input is where n < k
#determines the max cycle length in a range
#pre n < k
def range_cyc_length(n , k ):
    assert n < k
    max_cyc = 0
    #k + 1 because need inclusive
    for i in range(n, k + 1):
        if i in cyc_cache:
            cur_cyc = cyc_cache[i]
        else: 
            cur_cyc = cycle_length(i)
        if(max_cyc < cur_cyc):
            max_cyc = cur_cyc
    return max_cyc

def check_bad_in_range(start, fin):
    assert start < fin

    for bad_number in bad_list:
        if bad_number > start and bad_number < fin:
            print("RIP")
            return bad_number - 1
    return 0

collatz_in = open('./XMR73-RunCollatz.in', 'w')
collatz_out = open('./XMR73-RunCollatz.out','w')
write_in = ""
write_out = ""

for i in range(0, 10):
    n = random.randint(0, 1000000)
    k = random.randint(0, 1000000)

    while(n in bad_map):
        n = random.randint(0, 1000000)

    while(k in bad_map):
        k = random.randint(0, 1000000)

    if n > k:
        swap = n
        n = k
        k = swap
    #returns a nonzero number if there is a "bad num" in range
    shortened_k = check_bad_in_range(n, k)

    if shortened_k != 0:
        k = shortened_k

    max_cycl_length = range_cyc_length(n, k)
    write_in += str(n) + ' ' + str(k) + '\n'
    write_out += str(n) + ' ' + str(k) + ' ' + str(max_cycl_length) + '\n'

collatz_in.write(write_in)
collatz_out.write(write_out)

collatz_in.close()
collatz_out.close()




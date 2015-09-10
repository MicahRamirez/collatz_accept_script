import random 

f = open('./bad_numbers.txt', 'r')
#data structs
bad_map = {}

for line in f:
    b_num = int(line.strip('\n'))
    bad_map[b_num] = 0

f.close()

file_write = open('./acceptance_test.txt','w')

#lazy cache
cyc_cache = {}
bad_list = list(bad_map.keys())
map_to_blist = {}
bad_list.sort()

#associate the "bad number" with its' respective index in a sorted list
for i in range(0, len(bad_list)):
    map_to_blist[bad_list[i]] = i

#where n is an integer
def cycle_length(n):
    init_num = n
    cyc_len = 1
    while(n > 1):
        if(n in cyc_cache):
            #minus one to offset the init cyc length of 1 for both this and in cache
            cyc_cache[init_num] = cyc_len + cyc_cache[n] - 1
            return cyc_cache[init_num]
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
    #check the range from start to fin for bad numbers
    for i in range(start, fin + 1):
        if i in bad_map:
            start = i + 1
            bad_idx = map_to_blist[i]
            next_bad_num = bad_list[bad_idx + 1]
            fin = random.randint(start, next_bad_num)

    return (start, fin)

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
    #unpack the tuple
    n, k = check_bad_in_range(n, k)

    max_cycl_length = range_cyc_length(n, k)
    write_in += str(n) + ' ' + str(k) + '\n'
    write_out += str(n) + ' ' + str(k) + ' ' + str(max_cycl_length) + '\n'

collatz_in.write(write_in)
collatz_out.write(write_out)

collatz_in.close()
collatz_out.close()




from bitarray import bitarray
from bitarray.util import urandom
from util import count_ones
import random

class Chromosome:

    def __init__(self, data = None):
        if data is None:
            data = urandom(40)
        self.data = data

    def two_point(self, second_p):

        # random a and b within l
        # resulting in segments 0,1,2
        # 1st child flips segment 1
        # 2nd child flips segment 0 and 2
        first_p = self.data
        n = len(first_p)

        a = random.randint(0,39)
        b = random.randint(0,39)
        # ensure a != b
        while a == b:
            b = random.randint(0,39)
        # ensure a < b
        if a > b:
            temp = a
            a = b
            b = temp
        # ensure first segments exists
        seg1_1p = bitarray()
        seg1_2p = bitarray()
        if a > 0:
            seg1_1p = first_p[0:a]
            seg1_2p = second_p[0:a]
        # second segments
        seg2_1p = first_p[a:b+1]
        seg2_2p = second_p[a:b+1]
        # ensure third segments exists
        seg3_1p = bitarray()
        seg3_2p = bitarray()
        if b < n-1:
            seg3_1p = first_p[b:n]
            seg3_2p = second_p[b:n]

        first_c = seg1_1p.to01() + seg2_2p.to01() + seg3_1p.to01()
        second_c = seg1_2p.to01() + seg2_1p.to01() + seg3_2p.to01()
        return [[first_p, second_p], [bitarray(first_c), bitarray(second_c)]]


    def uniform(self, second_p):
        
        # for each bit, randomly (!)flip
        first_p = self.data
        n = len(first_p)
        
        first_c = bitarray()
        second_c = bitarray()

        # crossover
        for i in range(0, n):
            rnd = random.random()
            if round(rnd) == 1:
                first_c.append(first_p[i])
                second_c.append(second_p[i])
            else:
                first_c.append(second_p[i])
                second_c.append(first_p[i])

        return [[first_p, second_p], [first_c, second_c]]

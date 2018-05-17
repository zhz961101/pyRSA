#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time

MAX_SIZE = 1000

p_arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
         41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# def getPrime():
#     for i in range(2, MAX_SIZE):
#         if(isPrime(i)):
#             Primes.append(i)


def randInt(min, max, isNot=-1):
    res = int(random.random() * (max - min)) + min
    return res if res is not isNot else randInt(min, max, isNot)


def isEven(num):
    return not num & 1


def isOdd(num):
    return not isEven(num)


def fastMulMod(a, b, m):
    res = a * b - int(float(a) / m * b + 0.5) * m
    return res + m if res < 0 else res
# a%b = a - (a/b)*b
# a*b%m


def fastPowMod(a, p, m):
    res = 1
    while p is not 0:
        if isOdd(p):
            res = fastMulMod(res, a, m)
        a = fastMulMod(a, a, m)
        p >>= 1
    return res

# a^p%m


def fastMod(a, m):
    res = a - round(a / m) * m
    return res + m if res < 0 else res
# 负优化，了解一下
# a%b = a - round(a/b)*b


def rough_test(num):
    for m in p_arr:
        # if fastMod(num, m) is 0:
        if num % m is 0:
            return False
    return None


def _mr(testNum, confidence=8):
    if testNum < 2:
        return False
    if testNum in p_arr:
        return True
    if rough_test(testNum) is False:
        return False
    for i in range(confidence):
        test_rand = randInt(2, testNum - 1)
        # test_rand = random.choice(p_arr)
        tempN = testNum
        while tempN is not 0:
            # if test_rand ** (tempN - 1) % tempN is 1:
            if pow(test_rand, tempN - 1, tempN) is 1:
                # if fastPowMod(test_rand, tempN - 1, tempN) is 1:
                # if testNum % 2 is not 0:
                if isOdd(testNum):
                    return True
            else:
                return False
            tempN >>= 1
    return False


def Fermat(testNum):
    if testNum < 2:
        return False
    if testNum in p_arr:
        return True
    if rough_test(testNum) is False:
        return False
    test_rand = randInt(2, testNum - 1)
    # if test_rand ** (testNum - 1) % testNum is 1:
    if pow(test_rand, testNum - 1, testNum) is 1:
        return True
    return False


def getLongPrimes(SIZE=64):
    # print("1" + "0" * (SIZE - 1)," to ","9" * SIZE)
    while True:
        test_rand = random.getrandbits(SIZE)
        if _mr(test_rand):
            return test_rand


def _test_getPrimeArr(testSize):
    start = time.clock()
    p_res = []
    for i in range(testSize):
        if _mr(i, 20):
            p_res.append(i)
    print(p_res)
    end = time.clock()
    _mrtime = end - start

    start = time.clock()
    p_res2 = []
    for i in range(testSize):
        if Fermat(i):
            p_res2.append(i)
    print(p_res2)
    end = time.clock()
    fermattime = end - start

    print(_mrtime, fermattime, float(_mrtime) / fermattime)

    print([val for val in p_res if val not in p_res2])
    print([val for val in p_res2 if val not in p_res])


if __name__ == '__main__':
    print ("testing millerRabin.py")
    _test_getPrimeArr(1000)
    print ("long primes:" + str(getLongPrimes(32)))

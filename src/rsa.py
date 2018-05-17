#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mR import getLongPrimes
import random

# base func  Euclid...
def _gcd(a, b):
    return b if a is 0 else _gcd(b % a, a)


def ext_gcd(a, b):
    if b is 0:
        return (1, 0, a)
    x, y, gcd = ext_gcd(b, a % b)
    x, y = y, x - int(a / b) * y
    return x, y, gcd


def _mul_inverse_modulo(a, m):
    x, y, gcd = ext_gcd(a, m)
    if gcd is 1:
        return x % m
    else:
        return None


def get_pubE(phi):
    while True:
        e = random.randint(1, phi)
        if _gcd(e, phi) is 1:
            return e


class RSA:
    pubKey = 0
    prvKey = 0
    modulus = 0
    bitWindow_len = 8

    def __init__(self, SIZE=64):
        self.modulus, self.pubKey, self.prvKey = self.newKeys(SIZE + 1)
        self.bitWindow_len = int(SIZE / 4)
        print("self.bitWindow_len", self.bitWindow_len)

    @staticmethod
    def newKeys(size=64):
        q = getLongPrimes(size)
        p = getLongPrimes(size)
        while q is p:
            p = getLongPrimes(size)
        modulus = p * q
        phi = (q - 1) * (p - 1)
        phi = (q - 1) * (p - 1)
        prvKey = None
        while prvKey is None:
            pubKey = get_pubE(phi)
            prvKey = _mul_inverse_modulo(pubKey, phi)
        return modulus, pubKey, prvKey

    def encrypt_num(self, num):
        return pow(num, self.pubKey, self.modulus)

    def decrypt_num(self, num):
        return pow(num, self.prvKey, self.modulus)

    def encrypt_ascii(self, plain):
        bins = [ord(s) for s in plain]
        res = []
        for b in bins:
            res.append(self.encrypt_num(b))
        return " ".join(str(num) for num in res)

    def decrypt_ascii(self, cipher):
        cipher_list = cipher.split(" ")
        bins = []
        for c in cipher_list:
            bins.append(self.decrypt_num(int(c)))
        return "".join(chr(bin) for bin in bins)

    @staticmethod
    def split_BinsByLen(bins_, _length=8):
        import re
        split_re_str = ".{0}".format("{1," + str(_length) + "}")
        reversed_split = re.findall(re.compile(split_re_str), bins_[::-1])
        return [bin_[::-1] for bin_ in reversed_split][::-1]

    @staticmethod
    def bytes2longNum(bytes_l):
        bins_ = "".join("{:0>8}".format(bin(bytes)[2:]) for bytes in bytes_l)
        return int(bins_, 2)

    @staticmethod
    def long2Bytes(longnum):
        bins_ = RSA.split_binsByByte(bin(longnum)[2:])
        return [int(bin_, 2) for bin_ in bins_]

    def _crypt_bytes(self, bytes_l, key_):
        LongDEC = RSA.bytes2longNum(bytes_l)
        despose_ = pow(LongDEC, key_, self.modulus)
        BIN_l = RSA.split_BinsByLen(bin(despose_)[2:])
        code_l = [int(bin, 2) for bin in BIN_l]
        return code_l

    def crypt_bFile(self, filename, _key):
        res = []
        with open(filename, "rb") as f:
            bytes_l = list(f.read(self.bitWindow_len))
            while len(bytes_l):
                res += self._crypt_bytes(bytes_l, _key)
                bytes_l = list(f.read(self.bitWindow_len))
        return res

    def encrypt_bFile(self, filename):
        return self.crypt_bFile(filename, self.pubKey)

    def decrypt_bFile(self, filename):
        return self.crypt_bFile(filename, self.prvKey)

    @staticmethod
    def dump(filename, data):
        try:
            handle = open(filename, 'wb')
            handle.write(bytes(data))
            handle.close()
            print ('Save as to: ' + str(filename))
        except BaseException as e:
            print (e)

    @staticmethod
    def load(filename):
        res = None
        try:
            handle = open(filename, 'rb')
            res = handle.read()
            handle.close()
        except BaseException as e:
            print (e)
        return res

    def showKey(self):
        print (self.pubKey, self.prvKey, self.modulus)


if __name__ == '__main__':
    plaintext = "FUCK YOU MATHEMATICS!!!\nIt doest look like anything to me!"
    filename = "../run.py"
    # base func test #################
    # print(_gcd(11,242))
    #
    # Usage
    good_rsa = RSA(64)
    good_rsa.showKey()
    # base test #################
    encode = good_rsa.encrypt_ascii(plaintext)
    decode = good_rsa.decrypt_ascii(encode)
    print(encode)
    print(decode)
    print(len(encode) / len(decode))

    # binary file test #################
    encode = good_rsa.encrypt_bFile(filename)
    src = list(good_rsa.load(filename))
    print("src:", src)
    print(len(src), len(encode))
    print("encode:", encode)
    good_rsa.dump("run.encode.pack", encode)
    decode = good_rsa.decrypt_bFile("run.encode.pack")
    print("decode:", decode)
    good_rsa.dump("run.decode.py", decode)

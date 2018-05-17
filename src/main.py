#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from .rsa import RSA

__Author__ = "Sanshi_zhzer"
__Version__ = "0.1b"

Benner = "\t<author> : {author}\n\t<version> : {version}".format(
    author=__Author__, version=__Version__)


def print_usage():
    global Benner

    print("Benner:")
    print(Benner)
    print("Usage:")
    print("\n#encode String\n -t or -text <Key_Size=64> <plain_text> <option3?>:")
    print(
        "\tReturn a random generated RSA object and encryption result, RSA obj includes {public_key prime part, private_key prime part, modulus}")
    print("\n#encode File\n -f or -file <Key_Size=64> <plain_filename> <cipher_filename> <Decrypt_filename> <option5?>:")
    print("\tThe same return a RSA obj, and then the encryption result will save according to <cipher_filename>.")
    print("\n#new a Rsa\n -n or -newRsa <Key_Size=64>:")
    print(
        "\tReturn a random generated RSA object, includes {public_key prime part, private_key prime part, modulus}")
    print("\n#Encrypt\n -e or -encode <private_key> <modulus> <filename> <option4?>:")
    print("\tEncrypted <filename> file.")
    print("\n#Decrypt\n -d or -decode <public_key> <modulus> <filename> <option4?>:")
    print("\tDecrypt Plaintext <filename> file.")
    print("\nexample：")
    print("\t-file run.py run_cipher.dat")
    print("\t-file 128 run.py run_cipher.dat")
    print("\t-text 32 Well if you can't tell, does it matter?")
    print("\t-text 64 hello?")
    print("\t-newRsa 128")


def main():
    _argv = sys.argv[1:]
    cmd = _argv[0]
    option = _argv[1:]
    keylen = 64
    if option[0].isdigit():
        keylen = int(option[0])
        option = option[1:]

    if cmd in ["-t", "-text"]:
        plaintext = " ".join(option)
        _rsa = RSA(keylen)
        _rsa.showKey()
        encode = _rsa.encrypt_ascii(plaintext)
        print("$ py: encryption result:\n", encode)
    elif cmd in ["-f", "-file"]:
        infn = option[0]
        outfn = option[1]
        _rsa = RSA(keylen)
        _rsa.showKey()
        encode = _rsa.encrypt_bFile(infn)
        print("$ py: Encrypted file =>")
        _rsa.dump(outfn, encode)
        if len(option) is 3:
            defn = option[2]
            decode = _rsa.decrypt_bFile(outfn)
            print("$ py: Decrypted file =>")
            _rsa.dump(defn, decode)
    elif cmd in ["-h", "-help"]:
        print_usage()
    else:
        print_usage()

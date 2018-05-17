#!/usr/bin/env python
# -*- coding: utf-8 -*-

__Author__ = "Sanshi_zhzer"
__Version__ = "0.1b"

Benner = "\t<author> : {author}\n\t<version> : {version}".format(
    author=__Author__, version=__Version__)


def print_usage():
    global Benner

    print("Benner:")
    print(Benner)
    print("Usage:")
    print("\n#new a Rsa\n -n or -newRsa <Key_Size=64>:")
    print("\tReturn a random generated RSA object, includes {public_key prime part, private_key prime part, modulus}")
    print("\n#Encrypt\n -d or -decode <private_key> <modulus> <filename> <option4?>:")
    print("\tEncrypted <filename> file.")
    print("\n#Decrypt\n -e or -encode <public_key> <modulus> <filename> <option4?>:")
    print("\tDecrypt Plaintext <filename> file.")
    print("\n#encode String\n -t or -text <Key_Size=64> <plain_text> <option3?>:")
    print(
        "\tReturn a random generated RSA object and encryption result, RSA obj includes {public_key prime part, private_key prime part, modulus}")
    print("\n#encode File\n -f or -file <plain_filename> <cipher_filename> <Key_Size=64> <option4?>:")
    print("\tThe same return a RSA obj, and then the encryption result will save according to <cipher_filename>.")
    print("\nexample：")
    print("\t-file run.py run_cipher.dat 128")
    print("\t-text 32 Well if you can't tell, does it matter?")
    print("\t-text 64 hello?")
    print("\t-newRsa 128")


def main():
    print_usage()

CS411 Project: RSA Encryption
=============================
Matthew Stagg 3/7/2016
----------------------

### To Use:
This program requires python 2.x (NOT 3.x!) to function properly. Python is a cross-platform dynamic scripting language. Python can be found here: https://www.python.org/downloads/

### What It Does:
This is an implementation of the RSA encryption algorithm written in python. It utilizes two random 32-bit prime factors to generate a private key. The public key is always 65535.This program will take as input any ASCII string and encrypt it into a list of numbers. These numbers will then be decrypted back into the original ASCII character using the private key. It also includes integrated testing functionality.
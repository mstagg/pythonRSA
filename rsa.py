import math
from random import randint

# rsa.py
# Matthew Stagg
# 3/5/2016

# Class used to encrypt/decrypt strings

BITWIDTH = 32			# Width of prime factors sued to generate private key
PUBLIC_KEY = 65535		# Public key

class RSA(object):
	
	# Constructor
	def __init__(self):
		self.primePair = {}
		self.modValue = 0
		self.publicKey = PUBLIC_KEY
		self.privateKey = 0
		
		done = False
		while(done == False):
			self.generatePrimePair()
			self.generateModValue()
			pk = self.generatePrivateKey()
			if(pk != -1):
				done = True
				self.privateKey = pk
		
	# Euclid's algorithm to find greatest common denominator
	def gcd(self, m, n):
		while True:
			# Divide m by n and let r be remainder
			r = m % n
			# If r is 0, n is the answer
			# If r is not 0, set m to equal n and n to equal r and repeat
			if(r < 1):
				return n
			else:
				m = n
				n = r
	
	# Determines modulus inverse of %(a, b)
	def invMod(self, a, b):
		t = 0
		nt = 1
		r = b
		nr = a % b
		
		if(b < 0):
			b = -b
		else:
			b = b
			
		if(a < 0):
			a = b - (-a % b)
		else:
			a = a
		
		while(nr != 0):
			q = r / nr
			
			tmp = nt
			nt = t - (q * nt)
			t = tmp
			
			tmp = nr
			nr = r - (q * nr)
			r = tmp
		
		if(r > 1):
			return -1
			
		if(t < 0):
			t = t + b
		else:
			t = t
			
		return t
	
	# Check is number is prime or not	
	def isPrime(self, n):
		if n == 2:
			return True
		if n % 2 == 0 or n <= 1:
			return False

		sqr = int(math.sqrt(n)) + 1

		for divisor in range(3, sqr, 2):
			if n % divisor == 0:
				return False
		return True
		
	# Generates two random prime numbers so that p > q and p != q	
	def generatePrimePair(self):
		p = 0
		q = 0
		done = False
		
		while(done == False):
			p = randint(1, 2**BITWIDTH)
			if(self.isPrime(p)):
				done = True
				
		done = False
		while(done == False):
			q = randint(1, p - 1)
			if(self.isPrime(q)):
				done = True
		
		self.primePair["p"] = p
		self.primePair["q"] = q
	
	# Gets modulus value for encryption/dencryption
	def generateModValue(self):
		self.modValue = self.primePair["p"] * self.primePair["q"]
		
	def pqTotient(self):
		return (self.primePair["p"] - 1) * (self.primePair["q"] - 1)
		
	def generatePrivateKey(self):
		return self.invMod(self.publicKey, self.pqTotient())
		
	def powMod(self, base, exponent, mod):
		y = 1 % mod
		while(exponent > 0):
			if((exponent & 1) > 0):
				y = (base * y) % mod
			exponent = exponent >> 1
			base = (base * base) % mod
		return y
		
	# ENCRYPT: (message ^ publicKey) % modulus = encrypted char
	def encrypt(self, s):
		strList = list(s)
		for i in range(0, len(strList)):
			ascii = self.powMod(ord(strList[i]), self.publicKey, self.modValue)
			strList[i] = ascii
		return strList	
		
	# DECRYPT: (encryptedMsg ^ secretKey) % modulus = decrypted char
	def decrypt(self, l):
		for i in range(0, len(l)):
			ascii = self.powMod(l[i], self.privateKey, self.modValue)
			l[i] = str(unichr(ascii))
		return "".join(l)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
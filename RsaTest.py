from random import randint
from rsa import RSA

# RsaTest.py
# Matthew Stagg
# 3/5/2016

# Class used to test core function of RSA class
# Uses pre-tested and varified outcomes to prove that each function works as intended

class RsaTest(object):

	# Constructor
	# Populates all verified outcomes
	def __init__(self):
		self.publicKey = 65535
		self.privateKey = 14440774790529487
		self.modValue = 15725236647914011
		self.message = "Indiana"
		self.verifiedResults = [6203455842774329L, 10449696731316258L, 10444098371056832L, 13641245043391240L, 7463814312856899L, 10449696731316258L, 7463814312856899L]
		
	# Runs each tests and displays status of each
	def run(self):
		self.rsa = RSA()
		
		if(self.testGCD() == False):
			print("\nGCD TEST FAILED!")
			return
		else:
			print("\nGCD TEST PASSED!")
			
		if(self.testInvMod() == False):
			print("MODULAR INVERSE TEST FAILED!")
			return
		else:
			print("MODULAR INVERSE TEST PASSED!")	
			
		if(self.testIsPrime() == False):
			print("PRIMALITY TEST FAILED!")
			return
		else:
			print("PRIMALITY TEST PASSED!")	
			
		if(self.testGeneratePrimePair() == False):
			print("PRIME PAIR GENERATION TEST FAILED!")
			return
		else:
			print("PRIME PAIR GENERATION TEST PASSED!")	
			
		if(self.testEncryption() == False):
			print("ENCRYPTION TEST FAILED!")
			return
		else:
			print("ENCRYPTION TEST PASSED!")
			
		if(self.testDecryption() == False):
			print("DECRYPTION TEST FAILED!")
			return
		else:
			print("DECRYPTION TEST PASSED!")
		
	# Runs three tests to ensure Greatest COmmon Denominator functions properly
	def testGCD(self):
		if(self.rsa.gcd(12, 40) != 4):
			return False
		if(self.rsa.gcd(100, 1000) != 100):
			return False
		if(self.rsa.gcd(44, 99) != 11):
			return False
		return True
		
	# Runs three tests to verify that inverse modulus works properly
	def testInvMod(self):
		if(self.rsa.invMod(12, 35) != 3):
			return False
		if(self.rsa.invMod(111, 1321) != 1202):
			return False
		if(self.rsa.invMod(45, 91) != 89):
			return False
		return True
	
	# Runs three tests to verify primality function works correctly 	
	def testIsPrime(self):
		if(self.rsa.isPrime(1255567) != True):
			return False
		if(self.rsa.isPrime(7) != True):
			return False
		if(self.rsa.isPrime(7233) != False):
			return False
		return True
	
	# Verifies that a random prime pair is generated so that p > q and p != q	
	def testGeneratePrimePair(self):
		self.rsa.generatePrimePair()
		a = self.rsa.primePair["p"]
		b = self.rsa.primePair["q"]
		if(self.rsa.isPrime(a) == False):
			return False
		if(self.rsa.isPrime(b) == False):
			return False
		if(b >= a):
			return False
		return True
	
	# Verifies that the encryption algorithm works correctly
	def testEncryption(self):
		self.rsa.publicKey = self.publicKey
		self.rsa.privateKey = self.privateKey
		self.rsa.modValue = self.modValue
		if(self.rsa.encrypt(self.message) != self.verifiedResults):
			return False
		return True
	
	# Verifies that the decryption algorithm works correctly	
	def testDecryption(self):
		self.rsa.publicKey = self.publicKey
		self.rsa.privateKey = self.privateKey
		self.rsa.modValue = self.modValue
		if(self.rsa.decrypt(self.verifiedResults) != self.message):
			return False
		return True
				
				
				
				
				
				
				
				
				
				
				
				
				
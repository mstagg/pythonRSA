from rsa import RSA
from RsaTest import RsaTest

# cs411_stagg.py
# By: Matthew Stagg
# 3/7/2016

# Simple CLI tool to test RSA alogorithm implementation

# Main Function
def main():
	print("\nRSA Encryption Algorithm")
	print("------------------------")
	print("Written By: Matthew Stagg")
	print("On: 3/7/2016")
	while(True):
		print("\n\t1. About")
		print("\t2. Run Tests")
		print("\t3. RSA Demonstration")
		print("\t4. Quit")
		choice = raw_input("\tOption: ")
		
		if(choice == "1"):
			about()
		elif(choice == "2"):
			runTests()
		elif(choice == "3"):
			demonstration()
		elif(choice == "4"):
			break
		else:
			print("Invalid Input. Please try again.")

# Prints information about the program
def about():
	print("\n\tThis is an implementation of the RSA encryption algorithm written in python. It utilizes two random 32-bit prime factors to generate a private key. The public key is always 65535.")
	print("\tThis program will take as input any ASCII string and encrypt it into a list of numbers. These numbers will then be decrypted back into the original ASCII character using the private key.")
	
# Tests core functionality of RSA implementation
def runTests():
	test = RsaTest()
	test.run()
	
# Walks user through RSA implementation
def demonstration():
	wire = RSA()

	print("\nThis program will now walk you through the encryption process...")
	input = raw_input("Please enter a string to encrypt: ")
	
	print("\nYou entered '%s'." % (input))
	print("Your public key is: %d" % (wire.publicKey))
	print("Your private key is: %d" % (wire.privateKey))
	print("Your modulus value is: %d" % (wire.modValue))
	raw_input("Press any key to see how encryption works...")
	
	print("\nTo encrypt a string, allow X to equal the ASCII value of a given character. Then use the following formula:")
	print("EncryptedASCII = (X ^ PublicKey) % ModulusValue")
	print("This results in each character being encrypted as follows:")
	encryptedCharacters = wire.encrypt(input)
	for i in range(0, len(encryptedCharacters)):
		print("\t%s: %d" % (input[i], encryptedCharacters[i]))
	raw_input("Press any key to see how decryption works...")
	
	print("\nTo decrypt a string, allow X to equal the encrypted value of a given character. Then use the following formula:")
	print("DecryptedASCII = (X ^ PrivateKey) % ModulusValue")
	print("\nWhen decrypted, the output should be the same as your initial input!")
	print("%s is your original string!" % (wire.decrypt(encryptedCharacters)))
	
main()
	
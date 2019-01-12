#check whether number is prime
def isPrime(number):
	divisor = 2
	while divisor <= number / 2:
		if number % divisor == 0:
			#if true, number is not prime
			return False #numer is not a prime
		divisor += 1

	return True # number is prime

def printPrimeNumbers(numberOfPrimes):
	NUMBER_OF_PRIMES = 50
	NUMBER_OF_PRIMES_PER_LINE = 10
	count = 0
	number = 2
	#Repeadtly find prime numbers
	while count < numberOfPrimes:
		#print the prime number and increase the count
		if isPrime(number):
			count += 1 #increase the count

			print(number,end=" ")
			if count % NUMBER_OF_PRIMES_PER_LINE == 0:
				#print the number and advance to the next line
				print()

			#Check id the next number is prime
		number += 1
def main():
	print("the first 50 numbers are")
	printPrimeNumbers(50)

main()
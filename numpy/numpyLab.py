import numpy

print '--------------------------------------------'
lenght = input("Please enter numers count: ")
a = numpy.arange(lenght)
sum_squares = numpy.sum(a ** 2) 
square_sum = a.sum() ** 2
print 'Square sum ', square_sum, 'Sum of squares ', sum_squares 

print '--------------------------------------------'

P = input("Please enter prime number index: ")

LIM = 10 ** 6
N = 10 ** 9
primes = []
p = 2


def check_primes(a, p):
   a = a[a % p != 0]

   return a

for i in xrange(3, N, LIM):
   a = numpy.arange(i, i + LIM, 2)

   while len(primes) < P:
      a = check_primes(a, p)
      primes.append(p)

      p = a[0]

print 'The %dth prime is ' % P, primes[P-1]
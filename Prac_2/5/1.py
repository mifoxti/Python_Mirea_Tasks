def ham_dist_naive(num1, num2):
    return bin(num1 ^ num2).count('1')


ham_dist = lambda num1, num2: bin(num1 ^ num2).count('1')

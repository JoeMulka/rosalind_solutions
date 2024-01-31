test_n = 81
test_k = 8

# Find P(n, k) % 1,000,000
# The permuation equation is given by P(n, k) = n! / (n - k)!
# For large N and K, the numerator can become very large, exceeding the allowable size of an int in python
# Modulo multiplication is commutative, so we can separate the factorial into chunks, and take the modulo every time the product exceeds the modulo
# Which is the same as taking the modulo after every multiplication
# We can't do a separate modulo for the numerator and denominator, as modulo on fractions is not the same as modulo on the numerator and denominator separately
# So we factor out the equation into n * (n - 1) * ... * (n - k + 1), as the rest cancels with the denominator

num_multiplier = test_n - 1
result = test_n
while num_multiplier > test_n - test_k:
    result *= num_multiplier
    num_multiplier -= 1
    result %= 1000000
print(result)

# A prime number is one whose only factors (numbers that multiply to get it)
# are 1 and itself. Every number can be written as a unique prime
# factorization, which is the set of prime numbers that multiply to get it.

# For example, the prime factorization of 13,195 is 5 * 7 * 13 * 29, where it
# is important that 5, 7, 13, and 29 are all prime numbers.

# Your goal is to find all of the prime factors of the number 600,851,475,143.

# As a final answer, print out the largest prime factor. See 'answers.txt' for
# how I expect your final output to be formatted.

# Tips:
# - Find all the regular factors of our number before worrying about which
#   ones are prime.
# - Use a loop with range() to check numbers less than our value to find
#   factors.
# - Your loop will only have to go up to the square root of the value (or
#   the closest integer to it), not all the way up to value. 
# - Use remainder (%) to check if a number is a factor.
# - After finding your factors, check which ones are prime by starting at
#   the smallest values and working your way up.

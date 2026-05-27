# Type Content here...
# Input
start = int(input())
end = int(input())

# Function to check prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Find and print primes
found = False
for num in range(start, end + 1):
    if is_prime(num):
        print(num)
        found = True

if not found:
    print("No primes")
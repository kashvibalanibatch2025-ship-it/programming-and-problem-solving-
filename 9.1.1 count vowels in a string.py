# Type Content here...
# Input
text = input()

# Define vowels
vowels = "aeiouAEIOU"

# Count vowels
count = 0
for ch in text:
    if ch in vowels:
        count += 1

# Output
print(count)

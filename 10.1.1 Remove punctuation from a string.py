# Type Content here...
# Input
text = input()

# Remove punctuation
result = ""
for ch in text:
    if ch.isalnum() or ch == " ":
        result += ch

# Output
print(result)
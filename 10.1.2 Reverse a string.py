def reverse_string(s):
	# Write the code...
    # Reverse the string using slicing
    return s[::-1]

user_input = input("Enter a string: ")
result = reverse_string(user_input)
print(f"Original String: {user_input}")
print(f"Reversed String: {result}")
codes = int(input())


total_codes = 0
for char in range(codes):
    current_char = input()
    current_code = ord(current_char)
    total_codes += current_code

print(f"The sum equals: {total_codes}")

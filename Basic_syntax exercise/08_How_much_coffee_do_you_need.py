
coffee_needed = 0
lower_case = ["dog", "cat", "movie", "coding"] # creating a list
upper_case = str(lower_case).upper()
command = input()

while command != "END":
    if command in lower_case:
        coffee_needed += 1
    elif command in upper_case:
        coffee_needed += 2
    command = input()
if coffee_needed > 5:
    print("You need extra sleep")
else:
    print(coffee_needed)




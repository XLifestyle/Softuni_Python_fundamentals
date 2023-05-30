character_start_index = int(input())
character_end_index = int(input())

chracters_total = ""

for ascii_value in range(character_start_index, character_end_index + 1):
    print(chr(ascii_value), end=" ")
    
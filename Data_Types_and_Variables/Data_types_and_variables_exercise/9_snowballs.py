snowballs = int(input())

max_weight = 0
max_time = 0
max_quality = 0
max_value = 0
best_snowball = 0

for snowball in range(snowballs):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    current_snowball_value = (weight / time_needed) ** quality
    if current_snowball_value > max_value:
        max_weight = weight
        max_time = time_needed
        max_quality = quality
        max_value = current_snowball_value
    if current_snowball_value == max_value:
        best_snowball = snowball
print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")


quantity_of_decorations = int(input())
days_until_christmas = int(input())
ornament_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights = 15

spirit_points = 0
total_price = 0

for days in range(1, days_until_christmas + 1):
    if days % 11 == 0:
        quantity_of_decorations += 2
    if days % 2 == 0:
        total_price += ornament_price * quantity_of_decorations
        spirit_points += 5

    if days % 5 == 0:
        total_price += tree_lights * quantity_of_decorations
        spirit_points += 17
        if days % 3 == 0:
            spirit_points += 30

    if days % 3 == 0:
        total_price += (tree_skirt_price * quantity_of_decorations) + (tree_garland_price * quantity_of_decorations)
        spirit_points += 13

    if days % 10 == 0:
        spirit_points -= 20
        total_price += 5 + 3 + 15
if days_until_christmas % 10 == 0:
    spirit_points -= 30

print(f" Total cost: {total_price}")
print(f" Total spirit: {spirit_points}")




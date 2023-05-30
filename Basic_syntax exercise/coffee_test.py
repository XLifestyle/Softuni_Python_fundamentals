coffees = 0

while True:
    event = input()

    if event == "END":
        break
    lower_event = event.lower()
    if lower_event != "coding" or lower_event != "dog" or lower_event != "cat" or lower_event != "movie":
        continue
    if event.islower():
        coffees += 1
    elif event.isupper():
        coffees += 2
    else:
        continue

    if coffees > 5:
        print("You need extra sleep")
        break

print(coffees)

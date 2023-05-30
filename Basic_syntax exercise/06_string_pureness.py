number = int(input())


for i in range(number):
    string = input()
    if "," in string or "." in string or "_" in string:
        print(string, "is not pure!")
    else:
        print(string, "is pure.")

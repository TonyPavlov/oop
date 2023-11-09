def fuct(arg1):
    if arg1 % 2 == 0:
        print("Парне")
    else: 
        print("Непарне")

arg1 = int(input())

result = fuct(arg1)
print(f"{arg1} - {result}")

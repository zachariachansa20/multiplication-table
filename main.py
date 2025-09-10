number =int(input("Enter a number: "))
print(f"multiplication table for {number}:")
for i in range(1,13):
    print(f"{i} * {number} = {number * i}")

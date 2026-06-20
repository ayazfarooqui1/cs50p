name = input("What's Your Name? ")
print("Hello,", name +"!", sep=" ")
print(f"Hello, {name}" + "!")

name = input("What's Your Name? ").strip().title()
print("Hello,", name + "!")

x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x + y)

print(f"{z:,}")
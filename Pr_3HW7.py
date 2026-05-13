# Table generation using while loop

m = 0
j = int(input("Which number table:\n"))

while m <= 10:
    print(f"{j} x {m} = {m*j}")
    m = m + 1
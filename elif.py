x= range(30)
for y in x:
    if y % 4 ==0:
        print(f"{y} is divisible by 4")
    elif y % 5 ==0:
        print(f"{y} is divisible by 5")
    elif y % 7 ==0:
        print(f"{y} is divisible by 7")
    else:     
        print(f"{y} is divisible by 4,5 or 7")
        
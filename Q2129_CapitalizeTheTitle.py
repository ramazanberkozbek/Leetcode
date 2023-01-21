def capitalizeTitle(x: str) -> str:
    x = x.split(" ")
    y = ""

    for i in range(len(x)):
        if len(x[i]) <= 2:
            x[i] = x[i].lower()
        else: x[i] = x[i].title()
        if i != len(x)-1:
            y += x[i] + " "
        else: y += x[i]
    
    return y

print(capitalizeTitle("united states of america"))
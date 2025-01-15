arr = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

arr = list(map(lambda x: f"{x[0].upper()}, {x[1]}", arr))
for i in arr:
    print(i)
print("welcome to abc shop")
print("we have following items:")
print("1.wheat $75/kg\n 2.rice $55/kg\n 3.maize $70/kg\n4.jowar 50/kg")
item=int(input("select from above list"))
quantity=float(input("how much quantity did you want"))
if item==1:
    price=75*quantity
    print(price)
elif item==2:
    price=55*quantity
    print(price)
elif item==3:
    price=70*quantity
    print(price)
elif item2==4:
    price=50*quantity
    print(price)
else:
    print("invalid selection")

lista = [1,2,3,4,5,6,7,8,9]

for item in lista:
    print(f"Tabuada de {item} \n")

    tabuada= item
    for i in range(0,11):
        print(f"{tabuada} x {i} = {tabuada * i}")
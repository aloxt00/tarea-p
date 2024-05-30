import random 
le =int(input("¿cuantas letras nesesitas?"))
letras = ["A","B", "C","D", "E","F","G","H","I", "J", "K", "L","M","N", "O", "P","Q","R","S","T", "U", "V", "W", "X", "Y", "Z","@","#"]
contra = ""
for i in range(le):
    R = random.randint(0,27)
    contra+=letras[R]
print(contra)
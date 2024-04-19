planetas=list()
planetas=["Mercurio","Venus","Tierra","Marte","Jupiter","Saturno"]
print(planetas)
planetas.append("Urano")
planetas.append("Neptuno")

p=planetas.pop()
print(p)

pa=planetas.pop(0)
print(pa)

planetas.insert(0,pa)

lunas= ["Luna","Ceres", "Deimos","Phonos"]
print(lunas)
print(lunas[1])
print(lunas[3])
lunas.append("Europa")
lunas.append("Ganymedes")
lunas.append("Calisto")
lunas.append("Io")
lunas.append("Titan")
print(lunas)

print(lunas[0:3])
print(lunas[::3])        
moons=lunas
print (f"lunas: {lunas}") #Lo que está entre llaves es una variable
print (f"moons: {moons}")
moons.append("Triton")
print (f"lunas: {lunas}")
print (f"moons: {moons}")
print(f"lunas id:{id(lunas)}")
print(f"moons id:{id(moons)}")
print(moons is lunas)
moons=lunas.copy() #Para trabajar con una copia de la lista
moons.append("Oberon")
print (f"lunas: {id(lunas)}")
print (f"moons: {id(moons)}")
print(moons is lunas)
planetas_sw=["Hoth", "Tatooine", "Naboo", "Endor", "Yavin", "Coruscant"]
planetas.extend(planetas_sw)
print(planetas)
planetas.sort()
print(planetas)
lista_lunas=[lunas, planetas_sw]        
print(lista_lunas)
print(lista_lunas[1][0])#Cuando tenemos una lista dentro de otra lista, se utilizan dos corchetes para primero referenciar la lista dentro de la lista y luego el elemento dentro de la lista seleccionada.
for i,luna in enumerate(lunas):
    print(i,luna)
print(lunas.index("Titan"))
A=[]
B=[]
for i in range(0,10):
    A.append(i)
print(A)
for i in range(0,10):
    if i%2==0:
        B.append(i)
print(B)
print("---------------------------------")
#Compresión de listas
A=[i for i in range(0,10)]
B=[i for i in range(0,10) if i%2==0]
print(f"A: {A}")
print(f"B: {B}")
squares=[i**2 for i in range(0,10)]
print(f"Squares:{squares}")
pi=3.141592
print(f"pi:{pi:.2f}")
#Para acceder a un diccionario dentro de un diccionario se utilizan dos corchetes
minas={"IM": "Ingenieria de Minas", "IME": "Ingenieria de Minas y Metalurgica", "IME": "Ingeniería Mecánica de Suelos"}
print(minas)
ingenieria={"ISI":"Ingeniería de Sistemas de Información", "ISS": "Ingenieria Industrial y Sistemas","IME": "Ingeniería Mecatrónica"}
print(ingenieria)
facultad={"ingenieria": ingenieria, "minas": minas}
print(facultad["ingenieria"]["IME"])
print(f"IME: {facultad["minas"]["IME"]}")
print("---------------------------------")
if "civil" in facultad:
    print(facultad["civil"])
else:
    print("No existe la carrera")
try:
    print(facultad["civil"])
except:
    print("No existe la carrera de civil")

if "civil" not in facultad:
    facultad["civil"]={"IC:Ingenieria Civil"}
print(facultad["civil"])
caden="El caballo corre por el campo"
diccionario={}
for i in caden:
    if i in diccionario:
        diccionario[i]+=1
    else:
        diccionario[i]=1
print(diccionario)
for k,v in diccionario.items():
    print(f"{k}:{v}")
print("---------------------------------")
diccionario_ordenado=sorted(diccionario.items(), key=lambda item:item[1], reverse=True)
print(diccionario_ordenado)
print("---------------------------------")
diccionario_ordenado=dict(diccionario_ordenado)
for k,v in diccionario_ordenado.items():
    print(f"{k}:{v}")

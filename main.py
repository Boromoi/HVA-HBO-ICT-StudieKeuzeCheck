#Maak de variables aan
naam = str
raw_geboortejaar = str
geboortejaar = int

naam = input("Hoi wat is jou naam?" + "\n" + "Mijn naam is: ")
#Check of er nummers in de naam zitten en als dat zo is stop
#if any(char.isdigit() for char in naam):
#    print("Gebruik geen nummers in je naam alsjeblieft.")
#else: 
raw_geboortejaar = input("In welk jaar ben je geboren?" + "\n" + "Ik ben geboren in: ")
#Dit veranderd de string input naar een integer
geboortejaar = int(raw_geboortejaar)

print(type(naam))
print("Dit is naam" + naam)
print(type(raw_geboortejaar))
print("Dit is raw_geboortejaar" + raw_geboortejaar)
print(type(geboortejaar))
print("Dit is geboortejaar" + geboortejaar)
#importeer datetime, zodat het in de code gebruikt kan worden
import datetime

#Maak de variables aan
naam = str
raw_geboortejaar = str
geboortejaar = int
huidigeJaar = datetime.datetime.now().year
leeftijd = int
venusLeeftijd = int

naam = input("Hoi wat is jou naam?" + "\n" + "Mijn naam is: ")
#Check of er nummers in de naam zitten en als dat zo is stop
#if any(char.isdigit() for char in naam):
#    print("Gebruik geen nummers in je naam alsjeblieft.")
#else: 
raw_geboortejaar = input("In welk jaar ben je geboren "  + naam + "?\n" + "Ik ben geboren in: ")
#Dit veranderd de string input naar een integer
geboortejaar = int(raw_geboortejaar)
#Hier reken ik de leeftijd uit door het huidigejaar - het geboortejaar te doen. En de waarde daarvan verander ik weer terug, naar een string.
leeftijd = str(huidigeJaar - geboortejaar)
print("Beste " + naam + ", jou leeftijd is nu " + leeftijd + " jaar.")
#Reken venusLeeftijd uit door de leeftijd in een int te veranderen
#Aarde heeft 365 dagen in een jaar en Venus heeft 225 dagen in een jaar, dus is het 62% sneller. Vandaar gebruikt is de berekening leeftijd * 1.62
leeftijd = int(leeftijd)
venusLeeftijd = int(leeftijd * 1.62)
print("En je leeftijd is dan " + str(venusLeeftijd) + " in Venusjaren.")

print("\n" + str(type(naam)))
print("Dit is naam " + naam)
print(type(raw_geboortejaar))
print("Dit is raw_geboortejaar " + raw_geboortejaar)
print(type(geboortejaar))
print(geboortejaar)
print(type(huidigeJaar))
print(huidigeJaar)
print(leeftijd)
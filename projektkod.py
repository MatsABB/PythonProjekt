import numpy                                       #Importera en randomiser
from gtts import gTTS                              #Importerar talsyntes
import os
import playsound

Vänster = bool                                     #Definerar alla variablerna
slutresultat = 0
fortsätt= False

Rymdpartiet = {                                    #Dictionary för varje parti
    "namn": "Rymdpartiet",
    "Vänster": True,
    "Block": "Småpartierna",
    "min": 3,
    "max": 12
}
Partikelpartiet = {
    "namn": "Partikelpartiet",
    "Vänster": True,
    "Block": "Småpartierna",
    "min": 2,
    "max": 8
}
Strumppartiet = {
    "namn": "Strumppartiet",
    "Vänster": False,
    "Block": "Småpartierna",
    "min": 8,
    "max": 18
}
Gamlasossepartiet = {
    "namn": "Sjörövarpartiet",
    "Vänster": False,
    "Block": "Småpartierna",
    "min": 3,
    "max": 12
}
Extremisterna = {
    "namn": "Extremisterna",
    "Vänster": False,
    "Block": "Oljeblocket",
    "min": 3,
    "max": 6
}
Klimatdemokraterna = {
    "namn": "Klimatdemokraterna",
    "Vänster": True,
    "Block": "Oljeblocket",
    "min": 12,
    "max": 22
}
Framtidspartiet = {
    "namn": "Framtidspartiet",
    "Vänster": False,
    "Block": "Oljeblocket",
    "min": 12,
    "max": 18
}
Kommunisterna = {
    "namn": "Kommunisterna",
    "Vänster": True,
    "Block": "Inget",
    "min": 20,
    "max": 34
}
 
partier = [                                       #Listar alla parti dictionarys i samma lista
    Rymdpartiet,
    Partikelpartiet,
    Strumppartiet,
    Gamlasossepartiet,
    Extremisterna,
    Klimatdemokraterna,
    Framtidspartiet,
    Kommunisterna
]

while fortsätt == False:                                                                          #While-loop mot "valfusk"
     for allap in partier:                                                                        #Slumpar loopen
        resultat = numpy.random.randint(high= allap["max"],low= allap["min"])                      #Slumpat resultat för varje parti utifrån möjliga utfall
        slutresultat = slutresultat + resultat                                                    #Alla partiers resultat sammanlagt
        allap["resultat"] = resultat 
        print("Antalet som röstade på",allap["namn"],"var", allap["resultat"],"%")                #Skriver ut resultatet
     if slutresultat>100:                                                                         #Om "valfusk" skulle uppstått startas loopen om och tar bot det som är skrivet i terminalen
        slutresultat = 0     
        print("\r")
     else:
        break                                                                                       #Avslutar loopen vid godkänt resultat
print("\n")
for resultat in partier:                                                                            #Loop som räknar om resultatet så att procenten blir mellan partierna och inte med de som inte röstat
    if slutresultat<100:
        omräkning = int(resultat["resultat"]/slutresultat*100)                                      #formeln för omräkningen
        print(resultat["namn"], "fick då bland partierna",omräkning,"%")                            #utprintningen av omräkningen

    else: 
        break

print("Det var",slutresultat,"% av befolkningen som röstade", end=" ")                              #skriver ut valdeltaagendet
tts = gTTS(text="Det var"+str(slutresultat)+"% av befolkningen som röstade", lang='sv')             #informationen talsyntesen ska säga samt på vilket språk
tts.save("say.mp3") 
playsound.playsound('say.mp3', True)                                                                #ger info till datorn att spela upp ljudfilen som skapats
os.remove("say.mp3")
if slutresultat<100:                                                                                #förklarar omräkningen i terminalen om den sker
    print("och därmed omräkningen av %")
    
        

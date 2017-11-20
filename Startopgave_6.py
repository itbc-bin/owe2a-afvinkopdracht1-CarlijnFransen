# Naam: Carlijn Fransen 
# Datum: 
# Versie:

# Voel je vrij om de variabelen/functies andere namen te geven als je die logischer vind.

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.



def main():

    #= "alpaca.fasta" # Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand

    sentinel = False
    while sentinel == False:
        try:
            bestand = input('Geef een bestandsnaam: ')
            bestand = open(bestand)
            headers, seqs = lees_inhoud(bestand)
            sentinel = True
        except FileNotFoundError:
            print(' Zorg dat het bestand aanwezig is in de juiste map.')
        
                
                


            
        """
        Hier onder vind je de aanroep van de lees_inhoud functie, die gebruikt maakt van de bestand variabele als argument.
        De resultaten van de functie, de lijst met headers en de lijst met sequenties, sla je op deze manier op in twee losse resultaten.
        """
     
    
    zoekwoord = input("Geef een zoekwoord op: ")
    
    x = 0
    sequentie = ''
    try:
        for line in headers:
            if zoekwoord in line:
                print(headers[x])
                print('\n')
                print(seqs[x])
                print('\n')
                sequentie = seqs[x]
                print(is_dna(sequentie))
                knipt(sequentie)
                print('\n')
                print(40 * '-')
            else:
                x += 1

        else:
            raise TypeError:
        except TypeError:
            print('uw zoekwoord ' ,zoekwoord, ' is niet gevonden.')

    
    
    
     


    

    # schrijf hier de rest van de code nodig om de aanroepen te doen
    
    
def lees_inhoud(bestand):
    #bestand = open.readline('alpaca.fasta')
    
    headers = []
    seqs = []
    seq=''

    for line in bestand:
        if '>'  in line:
            line = line.replace('\n','')
            headers.append(line)
            if len(seq) != 0:
                seq += ' '
        
        else:
            line = line.replace('\n','')
            seq += line

    seqs = seq.split(' ')    

    
                
            #controle +tovegorn seq aan seqs
    #else:
            #line = line.strip()
            
    #laatste seq in seqs opslaan

    #print(headers)
    
    #print(seqs)
    
    """
    Schrijf hier je eigen code die het bestand inleest en deze splitst in headers en sequenties.
    Lever twee lijsten op:
        - headers = [] met daarin alle headers
        - seqs = [] met daarin alle sequenties behorend bij de headers
    Hieronder vind je de return nodig om deze twee lijsten op te leveren
    """
     
    return headers, seqs


def is_dna(sequentie):

    #global bestand
    

      
    A = (sequentie.count('A'))
    T = (sequentie.count('T'))
    C = (sequentie.count('C'))
    G = (sequentie.count('G'))
    N = (sequentie.count('N'))
    DNA = A+T+C+G+N


    if DNA == len(sequentie):
       # print('True')
        return True
        
    else:
       # print('False')
        return False    

    """
    Deze functie bepaald of de sequentie (een element uit seqs) DNA is.
    Indien ja, return True
    Zo niet, return False
    """
    

def knipt(sequentie):
    #print('test')
    bestand = open('enzymen.txt')
    enzymen = []
    for line in bestand:
        combi = line.strip().split(' ')
        combi[1] = combi[1].replace('^' , '')

        enzymen.append(combi)
        
    for x in enzymen:
        if x[1] in sequentie:
            print(x[0], ' knipt wel in sequentie')
        else :
            print(x[0], ' knipt niet in sequentie')
        
##        for y in range(0, len(sequentie)):
##            if sequentie[y: y+len(x[1])] == x[1]:
               
                  
    """
    Bij deze functie kan je een deel van de code die je de afgelopen 2 afvinkopdrachten geschreven hebt herbruiken

    Deze functie bepaald of een restrictie enzym in de sequentie (een element uit seqs) knipt.
    Hiervoor mag je kiezen wat je returnt, of wellicht wil je alleen maar printjes maken.
    """
    
main()

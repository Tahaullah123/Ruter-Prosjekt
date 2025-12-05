def funksjon_uten_parameter_og_returverdi():
    print("Her skjer det noe")
    
def funksjon_med_parameter_og_uten_returverdi(taimot, annet):
    print(taimot)
    
def funksjon_med_returverdi_uten_parameter():
    return "En string jeg sender tilbake"

def med_begge_deler(tall1, tall2):
    return tall1 + tall2

sum = med_begge_deler(23, 11)

print (sum)

antall = 0

def økAntall():
    antall += 1 

def print_en_setning():
    print(f"Dette er min setning nummer {antall}")
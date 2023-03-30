# Main file for code

from unidecode import unidecode

import Verbos
import Frases_Comunes

# Get the word(s) the user wants to translate.
user_input = input("Introduzca una palabra: ")

# Remove any and all accents ("tildes") from the word(s) the user searched. 
sin_tildes = unidecode(user_input)

# Make all letters in the user's search lowercase.
search = sin_tildes.lower()


print("\nTranslation(s)/Traduccion(es):") # Header for the output


# Conditional statements to search through all dictionaries for the user's search word(s):
 
if search in Verbos.verbos:
   print("(v) " + Verbos.verbos[search])
elif search in Verbos.verbs:
    print("(v) " + Verbos.verbs[search])
elif search in Frases_Comunes.frases:
   print(Frases_Comunes.frases[search])
else:
   print("Palabra no encontrada.")
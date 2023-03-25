# Main file for code

import Verbos
import Frases_Comunes

user_input = input("Introduzca una palabra: ")

search = user_input.lower()

print("\nTranslation(s)/Traduccion(es):")

if search in Verbos.verbos:
   print("(v) " + Verbos.verbos[search])
if search in Verbos.verbs:
    print("(v) " + Verbos.verbs[search])
if search in Frases_Comunes.frases:
   print(Frases_Comunes.frases[search])
else:
   print("Palabra no encontrada.")
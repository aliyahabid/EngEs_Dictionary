# Verbos

# Create additional dictionaries for second, third, and fourth translations of words. Alternatively,
# create any solution for words like "iron" that are both verbs and nouns.

# Dale un like, sentarse, gustar vs gustarse, cepillarse, ducharse, entrevista de trabajo,
# suscribete, en tu mismo, quisiera, saltar anuncio, rostro, dejar, permitir, pedir, siguiente, seguir, charlar,
# , peinar, dale la pena, extrana, raro, lentamente, abrazar, chismear, peinandote

# Reorder the verbs in alphabetical order to prevent duplicates.

verbos = \
    {"abrazar": "to hug",
     "arreglar": "to fix", 
     "bailar": "to dance",
     "beber": "to drink",
     "besar": "to kiss",
     "calmar": "to calm",
     "cocinar": "to cook",
     "conocer": "to know or to meet",
     "cortar": "to cut",
     "cubrir": "to cover",
     "curar": "to cure",
     "dar": "to give",
     "dejar": "to allow",
     "dormir": "to sleep",
     "estar": "to be",
     "ir": "to go",
     "lavar": "to wash",
     "lavarse": "to wash oneself",
     "limpiar": "to clean",
     "pedir": "to ask or request",
     "peinar": "to comb",
     "perder": "to lose",
     "pintar": "to paint",
     "planchar": "to iron",
     "poder": "can or be able to",
     "poner": "to put",
     "preguntar": "to ask",
     "saber": "to know",
     "seguir": "to follow",
     "sentir": "to feel",
     "ser": "to be",
     "tener": "to have",
     "tocar": "to touch or to play (an instrument)",
     "tomar": "to take or to drink",
     "venir": "to come"}

def search_verbos():
 key = input("Introduzca una palabra: ")
 if key in verbos:
   print("Translation: " + verbos[key])
 else:
   print("Palabra no encontrada.")

search_verbos()

verbs = \
    {"calm": "calmar",
     "come": "venir",
     "cook": "concinar", 
     "dance": "bailar",
     "drink": "tomar o beber",
     "give": "dar",
     "go": "ir",
     "have": "tener",
     "iron": "planchar",
     "know": "saber",
     "meet": "conocer o reuinir"}

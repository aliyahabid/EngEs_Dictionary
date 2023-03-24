# Verbos

# Create additional dictionaries for second, third, and fourth translations of words. Alternatively,
# create any solution for words like "iron" that are both verbs and nouns.

# Dale un like, sentarse, gustar vs gustarse, cepillarse, ducharse, entrevista de trabajo,
# suscribete, en tu mismo, quisiera, saltar anuncio, rostro, dejar, permitir, pedir, siguiente, seguir, charlar,
# , peinar, dale la pena, extrana, raro, lentamente, abrazar, chismear, peinandote

verbos = \
    {"bailar": "to dance",
     "cocinar": "to cook",
     "saber": "to know",
     "conocer": "to know or to meet",
     "beber": "to drink",
     "tomar": "to take or to drink",
     "ir": "to go",
     "venir": "to come",
     "calmar": "to calm",
     "dar": "to give",
     "tener": "to have",
     "planchar": "to iron",
     "tocar": "to touch or to play (an instrument)",
     "poder": "can or be able to",
     "ser": "to be",
     "estar": "to be",
     "sentir": "to feel",
     "lavar": "to wash",
     "lavarse": "to wash oneself",
     "limpiar": "to clean",
     "cubrir": "to cover",
     "dejar": "to allow",
     "seguir": "to follow",
     "curar": "to cure",
     "abrazar": "to hug",
     "besar": "to kiss",
     "poner": "to put",
     "pintar": "to paint",
     "perder": "to lose",
     "pedir": "to ask or request",
     "preguntar": "to ask",
     "peinar": "to comb"}

def search_verbos():
 key = input("Introduzca una palabra: ")
 if key in verbos:
   print("Translation: " + verbos[key])
 else:
   print("Palabra no encontrada.")

search_verbos()

verbs = \
    {"dance": "bailar",
     "cook": "concinar",
     "know": "saber",
     "meet": "conocer o reuinir",
     "drink": "tomar o beber",
     "go": "ir",
     "come": "venir",
     "calm": "calmar",
     "give": "dar",
     "have": "tener",
     "iron": "planchar"}

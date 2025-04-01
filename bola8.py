# Sofía Cáceres
# 31-03-2025
# Tengo 8 peluches de rana

import random

respuestas = ["✅ Si, definitivamante.", 
         "⭐ Con toda certeza, que si.", 
         "🔒 Sin lugar a duda.",
         "🤔 Respuesta confusa, inténtalo de nuevo.",
         "🕑 Preguntalo nuevamente más tarde.",
         "🤫 Mejor no dercirte ahora.",
         "✖️  Mis fuentes dicen que no.",
         "🌧️ El panorama no es muy favorable.",
         "🤷‍♂️ Muy dudoso."]

pregunta = input('pregunta:')

respuesta = random.choice(respuestas)

print('respuesta:', respuesta)

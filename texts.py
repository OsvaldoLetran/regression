# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB


texts = [
    'Hoy es un día horrible.',
    'Hoy es un día terrible.',
    'Estoy muy triste hoy.',
    'Este producto es malo',
    'No viniste nunca más por aquí.',
    'No entiendo cómo pueden hacer eso.',
    'Ya no quedan formas de salir de aquí',
    'Odio estar aqui.',
    'Tampoco irás al cine.',
    'No pueden fumar aqui.',
    'Nunca jugaron juntos.',
    'Ya no seguirán igual las cosas aquí.',
    'Todavía no estoy preparado.',
    'No cumplieron con lo pactado.',
    'No quiero verte nunca más.',
    'Jamás viajé en avión',
    'Ni pienso escucharte de nuevo.',
    'No se puede fumar aquí.',
    'Ningún teléfono funciona en esta zona.',
    'Nunca terminé mi curso de alemán.',
    'Él nunca me tiene en cuenta.',
    'No es este mi mejor día',
    'Jamás guardas lo que usas.',
    'Ni siquiera recuerdo su nombre.',
    'No me resulta nada fácil explicárselo.',
    'No quiero que me llames más.',
    'No les queda nada.',
    'No confía ni en su sombra.',
    'Nunca tengo tiempo para descansar.',
    'No alcanzan las hojas para todos.',
    'Nadie entiende tus chistes.',
    'Ya no quedan galletas en el frasco.',
    'Tú no tienes automóvil.',
    'Eso no es gracioso.',
    'Ya no te quiero, te odio',
    '¡Saqué un 10 en el examen de Matemática!',
    '¡Escucha, esa es la canción que me gusta!',
    '¡Felicitaciones por el nacimiento de tu hijo!',
    '¡Qué bello paisaje!',
    'Amo a mi perrito',
    'Amo la torta de chocolate.',
    'Qué mujer más bonita.',
    'Te esperamos con los brazos abiertos.',
    'Mi hogar es un lugar de confort y armonía.',
    'Los niños juegan felices en el parque',
    'La clase de yoga estuvo muy divertida.',
    'El fin de semana iremos al cine.',
    'Mi prima logró conseguir el trabajo.',
    'Este es un buen producto',
    'Compraré solo los zapatos que me gustan.',
    'Sí me gusta cómo se te ve la blusa',
    'Buen trabajo',
    'Mi perro siempre se emociona cuando me ve',
    'La fiesta fue divertida.',
    'Formidable',
    'El perro es fiel.',
    'El examen fue fácil.',
    'La niña está feliz.',
    'Es mi ti favorita.',
    'Estamos orgullosos de él.',
    'Es un excelente empleado.',
    'Se que puedes hacerlo',
    'Estoy muy orgulloso de ti',
    'Fantastico',
    'Me gusta como lo has hecho',
    'Te quiero mucho',
    'Este producto es excelente',
    'Me siento muy feliz hoy.',
    'Este es un día maravilloso.',
    'Este es un buen día.'
]


text_labels = [0] * (len(texts) // 2) + [1] * (len(texts) // 2)


# def text_counter(texts):
#     vectorizer = CountVectorizer()
#     txt_train = vectorizer.fit_transform(texts)
#     return vectorizer, txt_train


# def text_training(txt_train, text_labels):
#     text_classifier = MultinomialNB()
#     text_classifier.fit(txt_train, text_labels)
#     return text_classifier
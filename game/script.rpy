define c = Character("Char")
define c = Character("Ejemplar")
define Gender = ""
define NombreGuia = "PLACEHOLDER"
define NombreEjemplar = "PLACEHOLDER"


label start:
    menu:
        "Genero?"

        "Mujer.":
            $ Gender = "Ella"

        "Hombre.":
            $ Gender = "El"

        "Otro.":
            $ Gender = "Otro"
    menu:
        "Capitulo?"

        "1.":
            jump Fase1

        "2.":
            jump Fase2

        "3.":
            jump Fase3

        "4.":
            jump Fase4

        "5.":
            jump Fase5

        "6.":
            jump Fase6

label Fase1:
    "Hola."
    "Te damos la bienvenida a este proceso el cual se ha elaborado para darte a conocer nuevas formas de afrontar tus problemas asi como algunos pensamientos y sentimientos negativos, que a todo mundo nos Ilegan a aparecer en algunos momentos de nuestras vidas."
    
    scene bg Salon
    show c saluda
    c "Hola, soy [NombreGuia], tengo 13 años de edad y al igual que tu estudio la secundaría, hace unos meses hice este curso y me ha gustado mucho, por 10 que soy voluntaria para acompañarte en este proceso."
    show c piensa
    c "Sabías que los sentimientos negativos como el estrés, la preocupación, angustia o enojo. Pueden ser disminuidos con tu respiración..."
    show c gracia
    c "ilncreíble! ¿No es así? Pues se logra al usar la respiración como una forma de relajación, hay muchas formas, pero en este caso te compartiré una forma muy simple y eficiente de relajarte... Lo mejor de todo, no tendrás que pasar media hora escuchando al psicólogo mientras te cuenta algo... o mejor aún, ni siquiera 10 necesitaras, así que puedes usar este método en cualquier lugar y momento en que 10 necesites."
    show c apuntaDerecha at left
    show fase1grafico1 at right
    c "La técnica se llama respiración en cuadro y se usa un cuadro imaginario con 4 pasos de 4 segundos cada uno."
    
    hide c
    # TODO: pagina 6
    c "Al terminar el video presiona \"continuar\""

    show c sonrie
    c "Bien, ahora que ya conoces esta técnica, se recomienda que hagas el ciclo de respiraciones por 10 menos 20 veces, de esta manera te, relajaras completamente."
    c "Acompañame al siguiente capítulo de esta sesión."

    scene bg Parque

    show c sonrie
    # TODO: cambiar genero a neutro o crear palabras con diferente genero
    c "Sabes, yo no soy muy tranquila, pero cuando aprendí a relajarme, pude enfrentar mejor a mis problemas.„"
    show c apuntaDerecha
    c "Espera-!"
    show c sonrie
    # TODO: no se que hacer con su genero
    show e dormir
    c "Mira, quiero que conozcas a mi compañera [NombreEjemplar]..."
    show c callar
    c "Shh parece que esté dormida..."
    show c gritar
    c "[NombreEjemplar]!!!"
    show c decepcion
    c "Nada! No responde... creo que le tocaré el hombro para ver como esta."
    show c mirarDerecha
    show e mirarIzquierda
    c "Hola [NombreGuia], ¿Hace cuanto que estas aquí?"
    show c hablarDerecha
    # TODO: cambiar genero a neutro o crear palabras con diferente genero
    c "Acaso no me escuchabas, te quiero presentar a una nueva compañera..."

label Fase4:
    # 1
    scene bg salon
    show c saluda
    c "Hola, gracias por acompañarme de nuevo." 
    extend "En esta sesión conoceremos los pensamiento negativos que nos hacen sentir mal, una vez que los conozcamos veremos cómo cambiarlos."
     
    
    # 2
    show c sonreir
    c "Ahora veremos de qué se trata cada tipo de pensamiento."

    # 3
    show c explicar at left 
    c "Cuando dividimos los eventos en dos categorías cerradas, todo o nada, blanco o negro, bien o mal, perfecto o desastre total."
    extend "Un ejemplo es si haces algo que no queda perfecto, entonces es un total fracaso."

    # 4
    show c sonreir 
    c "Un solo evento negativo se toma como algo que demuestra que todo será de la misma manera en el futuro."

    # 5
    show c leer
    c "Se elige solo el detalle negativo y se llegan a conclusiones solo tomando en cuenta a ese detalle, dejando de lado los detalles positivos." 
    extend "Un experto llamado Lawrence E. Shapiro menciona que es como cuando dejas caer una gota de tinta negra en un vaso con agua, esa sola gota oscurece toda la visión de la realidad."

    # 6
    show c leer
    c "Se rechazan las experiencias positivas insistiendo en que no cuentan por un pretexto u otro. De esta manera se puede mantener una creencia negativa que oculta lo que podrían demostrar las experiencias diarias."

    # 7
    show c explicar
    c "Cuando hacemos interpretaciones negativas aun cuando no hay pruebas que le apoyen, estos tipos de pensamientos pueden aparecer de dos maneras:"

    # 7a
    show c explicar at left
    c "Leer la mente: Uno concluye porque sí, que alguien está pensando negativamente acerca de uno y ni siquiera necesita cersiorarse de su conclusión." 
    extend  "El error de la lectura de la fortuna: Anticipas que las cosas van a salir mal y te sientes convecido que tu predicción es un hecho."
    
    # 8
    show c explicar at left
    c "Exageramos la importancia de las cosas, como un error que cometemos o el logro de alguien más... o de manera inapropiada reducimos las cosas positivas hasta que parecen insignificantes."

    # 9
    show c explicar at left
    c "Asumimos que nuestras emociones negativas necesariamente reflejan las cosas como son: Si lo siento, entonces debe ser verdad."

    # 10
    show c explicar at left
    c "Intentamos motivarnos con el uso de las palabras \"debo, debería o no debo\", es como si castigara desde antes de hacer cualquier cosa, la consecuencia emocional de esas palabras es la culpa."

    # 11
    show c explicar at left
    c "Es una forma de sobre generalización, en lugar de describir el error nos etiquetamos negativamente a nosotros." 
    extend "Si alguien se equivoca etiquetamos a la persona, por ejemplo es un \"idiota\" en lugar de hablar de la acción negatica que cometió. Etiquetar además puede acarrear el insulto."

    # 12
    show c explicar at left
    c "Nos vemos como la causa de algunos eventos externos negativos aunque no seamos responsables directos de estos."

    # 13
    show c explicar at left
    c "Son muchos ¿Verdad?"
    extend "Ahora veremos cómo extinguirlos..."
    extend "A ver..."

    # 13a
    show c leer at left
    c "Ah, de acuerdo con mis apuntes que aconseja el uso de la técnica ABCD, que divide las situaciones que vivimos en partes, primero la A se refiere a un evento que nos hace pensar en algo."

    # 13b
    show c explicar at left
    c "B: (Belief = creencia) es el pensamiento que provoca el suceso."

    # 13c
    show c feliz at left 
    c "C: es la consecuencia del pensamiento, es decir que sentimos."

    # 13d
    show c sonreir 
    c "Hasta ahora es un proceso natural que todos hacemos. Pero si le añadimos: D de discutir."

    # 13e
    show c sonreir at left
    c "Entonces retaremos a los pensamientos que desencadenan el cómo nos sentimos."
    extend "Los pensamientos que combatiremos son aquellos negativos que acabamos de revisar."

    # 14
    show c sonreir at left
    c "Me acompañaras en un día normal que dividiremos en A B C y D para identificarlos fácilmente e iremos tomando decisiones para sentirnos mejor."

    # 14a
    show c sonreir at left
    c "Por favor ve respondiendo de acuerdo a como responderías tú eb tu vida real, de esta manera el ejercicio te beneficiara más."

    # 15
    scene bg cancha 
    show c sonreir at left 
    c "Recuerdas que acabo de entrar al equipo de futbol, hoy es nuestro segundo partido y... Voy a estar en la posición delantera, mi responsabilidad es anotar."

    #TODO: personajes y expresiones, este solo es el texto y estructura logica
    # 16
    c "Muy bien, hay viene el balón..."

    # 17
    c "Bien 10 tengo, ahora voy a tirar"

    # 18
    c "EI tiro no fue gol."

label eleccion1111_1_fail:
    scene bg vacio
    # 18e
    "[NombreGuia] se ha dado cuenta de que un pensamiento negativo ha aparecido en su mente."
    # transicion a el pasado por fallar
    jump eleccion1111_1_start

label eleccion1111_1_start:
    menu:
        c "EI tiro no fue gol."

        "Seguramente esta nueva posición no es para mí, no podré meter gol.":
            # 18a
            "La autoestima de [NombreGuia] ha disminuido... \n"
            extend "Razón: Pensamiento todo o nada"
            jump eleccion1111_1_fail

        "Me van a cambiar pronto de posición, soy terrible para patear bien el balón.":
            # 18b
            "[NombreGuia] se siente angustiada... \n"
            extend "Razón: pensamiento de sobre generalización"
            jump eleccion1111_1_fail

        "Vamos a perder por mi culpa.":
            # 18c
            "La autoestima de [NombreGuia] ha disminuido... \n"
            extend "Razón: pensamiento Tipo filtro mental y auto culpa."
            jump eleccion1111_1_fail

        "Estuvo cerca para ser la primera vez que pateo el balón.":
            # 18c
            "[NombreGuia] se siente con más entusiasmo! \n"
            extend "Razón: pensamiento positivo."
            jump eleccion111_1_final

label eleccion1111_2_fail:
    scene bg vacio
    # 18e
    "[NombreGuia] se ha dado cuenta de que un pensamiento negativo ha aparecido en su mente."
    # transicion a el pasado por fallar
    jump eleccion1111_2_start

label eleccion1111_2_start:
    # 19-1
    "Marcador final 2-2"
    e "Vaya, al final nos han empatado, fue un partido difícil."

    menu:
        c "¿qué le digo?"

        "Debería de haber metido al menos un gol más.":
            # 19-1a
            "[NombreGuia] frustrada Y desanimada... \n"
            extend "Razón: uso de la palabra \"debería\"."
            jump eleccion1111_2_fail

        "Solo pude meter un gol para nada es el debut de una estrella.":
            # 19-1b
            "[NombreGuia] siente coraje contra sí misma... \n"
            extend "Razón: Descalificación de lo positivo, era su primera vez y aun así metió gol. Pensamiento todo o nada."
            jump eleccion1111_2_fail

        "Isell ha de pensar que empatamos por mi culpa.":
            # 19-1c
            "[NombreGuia] siente angustia y miedo de perder sus amistades... \n"
            extend "Razón: Pensamiento negativo \"leer la mente\"."
            jump eleccion1111_2_fail

        "Metí un gol seguramente mejoraré más si sigo jugando.":
            # 19-1d
            "[NombreGuia] se siente contenta y satisfecha. \n"
            extend "Razón: pensamiento positivo."
            jump eleccion1111_2_final

label eleccion1111_2_final
    # 20
    c "Gracias por acompañarme, fue un día muy excitante, te espero en la próxima sesión!!!"

    hide c
    jump Finale4 

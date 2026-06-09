label Fase2:
    # 1
    "En esta ocasión, guiaras a [NombreGuia] durante un día. Toma las decisiones que le ayuden a resolver de mejor manera sus problemas."
    #READ: texto inutilizado "En la siguiente sección podrás seleccionar entre varías respuestas, para conocerlas, solo presiona sobre cada opción que aparecerá en el menú de la derecha, cuando las conozcas, entonces das click en la palomita correspondiente a tu selección."

    # 2
    show c enojar
    c "..."

    # 3
    show c triste
    c "Eh! ¿Qué que me pasa? EI día de hoy nuestro maestro de ciencias naturales, nos encargó un trabajo para eI fin de semana... Pero solo nos encargó ese trabajo a 5 alumnos, es un trabajo muy complicado, ni siquiera se puede resolver usando el libro de texto."

    # 4
    c "¿por qué a nosotros 5? Parece que se acerca un concurso de ciencias el mes que entra y es tarea extra para los que tenemos 8.5 de promedio para arriba. No sé qué pensar:"

    menu:
        "¿por qué a nosotros 5? pese a mi 8.5 de promedio?"

        "Mis padres creerán que voy mal y me castigaran el fin de semana, como si no fuera suficiente.":
            pass  
        "Tengo que hacer ese trabajo imposible para no reprobar y bajar mi promedio, quizá lo que quiere el maestro es que reprueben el máximo posible.":
            pass  
        "Las opciones anteriores.":
            pass
    
    # 3
    show c enojar

    menu:
        c "No es justo, ya no sé qué hacer."

        "Tienes razón.":
            # 3a
            show c decidirse
            c "No puedo seguirme indignando..."  
        "Relajarse y luego pensar de nuevo.":
            pass
    
    # 3b
    show c piensa
    c "Se me olvidaba que la tenía... la libreta de notas de mi taller de afrontamiento de problemas."

    #3bb
    show c explicar
    c "Dice que el primer paso es la orientación que le damos al problema... umm..."

    menu:
        c "Entonces lo puedo ver como:"

        "Mis padres creerán que voy mal y me castigaran el fin de semana, como si no fuera suficiente.":
            show c calma
            c "podria demostrarles mi calificacion y que es algo especial solo para los 5... "

        "Tengo que hacer ese trabajo imposible para no reprobar y bajar mi promedio, quizá lo que quiere el maestro es que reprueben el máximo posible..":
            show c calma
            c "Cuando nos dio el trabajo el profesor parecia sonreir, dudo que sea serio, Deberia de pensarlo.."

        "Las opciones anteriores.":
            show c calma
            c "Tengo que calmarme, puedo hablar con mis padres, tengo una buena calificacion y el profesor parecia sonreir casualmente envez de su formalidad recurrente..."

        "Quizá el maestro quiere conocer nuestras capacidades.":
            pass
    
    #3c
    show c decidirse
    c "Le demostraré que no me detendré con el hecho de que la información no viene en el libro de texto."
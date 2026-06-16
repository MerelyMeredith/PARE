default Fase5_bad = False

label Fase5:
    $ Fase5_bad = False
    # 1
    scene bg vacio
    show c saluda
    c "Hola, en esta sesión continuaremos revisando visando los pensamientos negativos. ¿Quieres empezar con la actividad o revisar los tipos de pensamiento negativo antes?"
    menu:
        "¿empezar con la actividad o revisar los tipos de pensamiento negativo?"

        "Continuar.":
            # 2 
            show c apuntaDerecha at left
            show fase5grafico1 at right
            c "Cuando dividimos los eventos en dos categorías cerradas, todo o nada, blanco o negro, bien o mal, perfecto o desastre total."
            c "Un ejemplo es si haces algo que no queda perfecto, entonces es un total fracaso."

            # 2a
            show c explicar at left
            show fase5grafico2 at right
            c "Un solo evento negativo se toma como algo que demuestra que todo será de la misma manera en el futuro."

            # 2b
            show c leer at left
            show fase5grafico3 at right
            c "Se elige solo el detalle negativo y se llegan a conclusiones solo tomando en cuenta a ese detalle, dejando de lado los detalles positivos. Un experto llamado Lawrence E. Shapiro menciona que es como cuando dejas caer una gota de tinta negra en un vaso con agua, esa sola gota oscurece toda la visión de la realidad."

            # 2c
            show c explicar at left
            show fase5grafico4 at right
            c "Se rechazan las experiencias positivas insistiendo en que no cuentan por un pretexto u otro. De esta manera se puede mantener una creencia negativa que oculta 10 que podrían demostrar las experiencias diarias."

            # 2d
            show c sonreir at left
            show fase5grafico5 at right
            c "Cuando hacemos interpretaciones negativas aun cuando no hay pruebas que le apoyen, estos tipos de pensamiento pueden aparecer de dos maneras:"

            # 2d_1
            show c leer at left
            show fase5grafico5 at right
            c "Leer la mente: Uno concluye porque sí, que alguien está pensando negativamente acerca de uno y ni siquiera necesita cerciorarse de su conclusión."
            c "El error de la lectura de la fortuna: Anticipas que las cosas van a salir mal y te sientes convencido que tu predicción es un hecho."

            # 2e
            show c explicar at left
            show fase5grafico6 at right
            c "Exageramos la importancia de las cosas, como un error que cometemos o el logro de alguien más... o de manera inapropiada reducimos las cosas positivas hasta que parecen insignificantes."

            # 2f
            show c apuntaDerecha at left
            show fase5grafico7 at right
            c "Asumimos que nuestras emociones negativas necesariamente reflejan las cosas como son: Si 10 siento, entonces debe ser verdad."

            # 2g
            show c explicar at left
            show fase5grafico8 at right
            c "Intentamos motivarnos con el uso de las palabras \"debo, debería o no debo\", es como si se castigara desde antes de hacer cualquier cosa, la consecuencia emocional de esas palabras es la culpa."

            # 2h
            show c sonreir at left
            show fase5grafico9 at right
            c "Es una forma de sobre generalización, en lugar de describir el error nos etiquetamos negativamente a nosotros. Si alguien se equivoca etiquetamos a la persona, por ejemplo es un \"idiota\" en lugar de hablar de la acción negativa que cometió. Etiquetar además puede acarrear el insulto."

            # 2i
            show c sonreir at left
            show fase5grafico10 at right
            c "Nos vemos como la causa de algunos eventos externos negativos aunque no seamos responsables directos de estos."
            jump Fase5Parte2

        "Revisar.":
            jump Fase5Parte2

label Fase5Reinicio:
    $ Fase5_bad = False
    scene bg void
    # transicion al pasado
    jump Fase5Parte2

label Fase5Parte2:
    # 3
    scene bg Cuarto
    show c sonreir
    c "A continuación dará inicio la actividad del día, recuerda responder de acuerdo a como 10 harías en tu vida real."

    # 4
    show c enojar
    c "El día de hoy tuve una mala nota en el examen de matemáticas, 6.5... no solo eso, mi compañera saco 7. ¿Cómo es posible que nuestras calificaciones de naturales sean de concurso y las de matemáticas sean tan bajas? Aunque Iselle normalmente es aplicada en todas las clases..."

label Fase5Eleccion1_Inicio:

    menu:
        "¿Cómo es posible que nuestras calificaciones sean tan bajas?"

        "Naturales es muy fácil en realidad soy tonto y se nota en matemáticas.":
            # 4a
            show c triste
            c "[NombreGuia] se siente enojado y desanimado.\nRazón: Se auto etiqueta negativamente."
            jump Fase5Eleccion1_Fail

        "Puedo hacer algo para subir mi promedio, quiero hacerlo.":
            # 4b
            show c decidirse
            c "[NombreGuia] no está satisfecho con su desempeño pero siente la necesidad de esforzarse para lograr algo mejor."
            jump Fase5Eleccion2_Inicio

        "Seguramente esto me pasara en otras materias como naturales.":
            # 4d
            show c triste
            c "[NombreGuia] se siente desanimado respecto a la escuela.\nRazón: Sacar conclusiones antes de tiempo."
            jump Fase5Eleccion1_Fail

        "Por juntarse conmigo, Isell saco esas calificaciones.":
            # 4c
            show c triste
            c "[NombreGuia] se siente decepcionado de sí mismo y su autoestima ha bajado.\nRazón: Pensamiento negativo \"personalización\","
            jump Fase5Eleccion1_Fail
            
label Fase5Eleccion1_Fail:
    # 4e
    show c triste
    "[NombreGuia] se ha dado cuenta de que un pensamiento negativo ha aparecido en su mente."
    menu:
        c "..."

        "Reconocerlo y enfrentarlo.":
            jump Fase5Eleccion1_Inicio

        "Seguir avanzando.":
            $ Fase5_bad = True
            jump Fase5Eleccion2_Inicio

label Fase5Eleccion2_Inicio:
    # 5-1
    scene bg Comedor
    show c piensa
    c "Pediré al maestro trabajos extras y le pediré a John que me explique. Umm, John me podría apoyar, Ie hablaré de unas vez."

    # 5-1a
    # 5-2a
    show c telefono
    c "[NombreGuia] intenta hablar por teléfono a su amigo, pero no responden la llamada."
    menu:
        c "no responden la llamada..."

        "Puede ser que este ocupado, le marcaré de nuevo más tarde.":
            # 5-1b
            # 5-2b
            show c sonreirTelefono
            c "Siegfried evita pensar en situaciones que no conoce y se siente más tranquilo."
            if Fase5_bad:
                jump Fase5Eleccion2_Final
            else:
                jump Fase5Eleccion3_Inicio

        "Ah de tener identificador de llamadas y no me quiere contestar.":
            # 5-1c
            # 5-2c
            show c tristeTelefono
            c "Siegfried se siente rechazado y ansioso.\nRazón: uso de pensamiento de sacar conclusiones antes de tiempo."
            jump Fase5Eleccion2_Fail

        "De seguro quiere ir a jugar futbol con otros amigos y no quiere perder el tiempo conmigo.":
            # 5-1d
            # 5-2d
            show c tristeTelefono
            c "Siegfried se siente rechazado y ansioso.\nRazón: uso de pensamiento de sacar conclusiones antes de tiempo."
            jump Fase5Eleccion2_Fail

        "De todos modos tengo el presentimiento de que no me ayudará, mejor solo hablo con el profesor.":
            # 5-1e
            # 5-2e
            show c tristeTelefono
            c "Siegfried siente miedo y se siente menos.\nRazón: Razonamiento emocional"
            jump Fase5Eleccion2_Fail

label Fase5Eleccion2_Fail:
    if Fase5_bad:
        # 5-2f
        show c incomodoTelefono
        "[NombreGuia] se ha dado cuenta de que un pensamiento negativo ha aparecido en su mente."
        menu:
            c "..."

            "Reconocerlo y enfrentarlo.":
                jump Fase5Eleccion2_Inicio

            "Seguir avanzando.":
                # 5-2h
                "[NombreGuia] se siente muy triste empieza a cuestionarse si de verdad es para el eso de estudiar, siente que no es bueno para las matemáticas y se siente mal consigo mismo por no poder pasar bien el año. Quizá no tiene caso estudiar después de todo... Cambia la historia de Siegfried"
                jump Fase5Reinicio
    else:
        # 5-1f
        show c tristeTelefono
        "[NombreGuia] se ha dado cuenta de que un pensamiento negativo ha aparecido en su mente."
        menu:
            c "..."

            "Reconocerlo y enfrentarlo.":
                # 4
                jump Fase5Eleccion2_Inicio

            "Seguir avanzando.":
                # 1
                jump Fase5Eleccion2_Final

label Fase5Eleccion2_Final:
    # 5-1g
    # 5-2g
    show c incomodoTelefono
    c "Siegfried se siente triste esperando la llamada de su compañero, esa ola de inseguridad y miedo le hace gritar.. media hora después recibe la llamada de su amigo John. Has superado el nivel, pero puedes lograr que Siegfried se sienta mejor al reiniciar el capítulo o si quieres puedes terminar este capítulo y terminar esta etapa de la sesión."
    menu:
        c "reiniciar el capítulo o si quieres puedes terminar este capítulo."

        "Reiniciar el capítulo.":
            jump Fase5Reinicio

        "Terminar capítulo.":
            jump Finale5

label Fase5Eleccion3_Inicio:
    # 5-3
    scene bg Comedor
    show c sonreirTelefono
    "Mientras Siegfried esperaba un tiempo para hablarle de nuevo a su compañero decidió revisar los temas que se le hacían más difíciles, paso el tiempo y sin darse cuenta recibió la llamada de su amigo John."

    # 6
    scene bg pantalla dividida
    show c felizTelefono at left
    show ee felizTelefono at right
    ee "Hola Siegfried, tengo tu número de teléfono marcado como llamada perdida, estaba bañándome y no pude contestar. ¿Me hablaste?"
    c "Hola John gracias por hablarme..."

    # 7
    hide ee 
    scene bg cuarto
    show c saluda at center
    c "Gracias por acompañarme, este es el final de nuestro curso, espero haberte comunicado algo positivo y que te hayas divertido."
    jump Finale5
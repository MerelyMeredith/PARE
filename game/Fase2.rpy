label Fase2:
    # 1
    "En esta ocasión, guiaras a [NombreGuia] durante un día. Toma las decisiones que le ayuden a resolver de mejor manera sus problemas."
    #READ: texto inutilizado "En la siguiente sección podrás seleccionar entre varías respuestas, para conocerlas, solo presiona sobre cada opción que aparecerá en el menú de la derecha, cuando las conozcas, entonces das click en la palomita correspondiente a tu selección."

    # 2
    scene bg salon
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

    # 3bb
    show c explicar
    c "Dice que el primer paso es la orientación que le damos al problema... umm..."
    menu:
        c "Entonces lo puedo ver como:"

        "Mis padres creerán que voy mal y me castigaran el fin de semana, como si no fuera suficiente.":
            show c calma
            c "podria demostrarles mi calificacion y que es algo especial solo para los 5... "

        "Tengo que hacer ese trabajo imposible para no reprobar y bajar mi promedio, quizá lo que quiere el maestro es que reprueben el máximo posible.":
            show c calma
            c "Cuando nos dio el trabajo el profesor parecia sonreir, dudo que sea serio, Deberia de pensarlo..."

        "Las opciones anteriores.":
            show c calma
            c "Tengo que calmarme, puedo hablar con mis padres, tengo una buena calificacion y el profesor parecia sonreir casualmente envez de su formalidad recurrente..."

        "Quizá el maestro quiere conocer nuestras capacidades.":
            pass
    
    # 3c
    show c decidirse
    c "Le demostraré que no me detendré con el hecho de que la información no viene en el libro de texto."

    # 4
    show c piensa
    c "Ah! Son tantos problemas a vencer, entre mis padres enojados, si repruebo, si no hago el trabajo y no voy al concurso!!!"

    menu:
        c "Cuál problema es en el que me debería de concentrar?"

        "Evitar que se enojen tus padres.":
            # 4a
            show c decepcion
            c "Les explicaré que es trabajo extra para prepararme e ir al concurso... Pero ¿qué pasa con el trabajo que hay que hacer?"

        "No reprobar.":
            # 4b
            show c decepcion
            c "No creo reprobar por no hacer esa tarea. ¿Entonces qué hago?"

        "No ir al concurso.":
            # 4c
            show c decepcion
            c "Para ir al concurso... Tengo que hacer el trabajo."

        "Hacer el trabajo.":
            # 4d
            pass
    
    #READ: me salte 4d por su trivialidad

    # 5
    show c leer
    c "Umm. ¿Qué dice mi libreta de notas acerca de esto? A claro, el paso que sigue es definir el problema. En este caso... ¿cuál es el problema?"
    menu:
        c "¿cuál es el problema?"

        "No ir al concurso.":
            # 5a
            show c decidirse
            c "Pero antes tengo que resolver otras situaciones..."  
        "Encontrar la información para hacer la tarea.":
            pass

    # 5b
    show c piensa
    c "Claró primero debo de buscar otros lugares donde encontrar la información necesaria para hacer la tarea. ¿Dónde encontraré la información?"

    menu:
        c "¿Dónde encontraré la información?"

        "Hay muchos sitios.":
            # 5c
            show c piensa
            menu:
                c "Si son tantos donde se podría encontrar, es difícil decidir." 

                "Revisar libreta para resolver problemas.":
                    # 5e
                    c "En la libreta dice que 10 que sigue es..."  
                "Hacer una lista.":
                    pass
        "Hacer una lista.":
            pass
    
    # 5d
    show c decidirse
    c "Claro! EI siguiente paso para resolver problemas es generar una lista de alternativas..."

    # 6
    show c sonreir
    c "Bien, ya escribí una lista de donde podría encontrar la información que necesito: biblioteca de la escuela, biblioteca pública, internet, enciclopedia de mi casa, preguntarle a un experto, puesto de revistas, librería..."

    # 7
    c "No me alcanzara el fin de semana para revisar todos los lugares."
    menu:
        c "¿Qué hago?"

        "Debería revisar todas.":
            # 7a
            show c decidirse
            c "Si, pero..."  
        "Elegir las opciones más adecuadas.":
            pass
    
    # 7b
    show c calma
    c "Sigue elegir la opción u opciones más adecuadas."
    menu:
        c "¿Cómo tomo una decisión?"

        "A la suerte.":
            # 7c
            show c feliz
            c "Hago papelitos con el nombre de cada opción en cada uno, luego doblo los papeles, luego que mi hermanita seleccione dos papelitos. Si todo sale bien tendré suerte y en cualquiera de esos lugares, encontraré la información."

            # 7cc
            show c sorpresa
            c "iUn momento! ¿y si no está la información ahí? Es una situación seria, iNo puedo arriesgar mis estudios en un juego de azar!"

        "Según las ganas que tenga el fin de semana.":
            # 7d
            show c leer
            c "Creo que debería encontrar otra opción... ¿Qué tal si no tengo ganas de hacer nada?"

        "Hacer una lista de ventajas y desventajas de cada opción.":
            pass
    
    # 7e
    show c callar
    c "Bien, ahora contaré las ventajas y desventajas... cual son ventajas importantes y cuales desventajas definitivamente descalifican las opciones... veamos... No conozco a ningún experto además del profesor y él no me hará la tarea..."

    # 8
    show c feliz
    c "Bien al final elegí... internet, biblioteca pública y biblioteca de la escuela son las que me dieron más ventajas y además ventajas muy buenas."
    menu:
        c "A cual iré solo tendré tiempo de ir a dos lugares..."

        "Biblioteca pública y biblioteca de la escuela.":
            # 8a
            show c feliz
            c "He entregado el trabajo y me saque un 9.5 de calificación. De acuerdo con las notas de resolución de problemas, el último paso es la evaluación... ¿Creo que puedo mejorar los resultados cambiando el proceso? ¿Funcionó el método que use?"

        "Biblioteca de la escuela e Internet.":
            # 8b
            show c leer
            c "Umm... el método funcionó pues me saque un 9.5 pero si hubiera encontrado más información seguramente me hubiera sacado un 10... Quizá para la próxima debería encontrar una forma que facilite poder visitar 3 lugares en vez de dos."

        "Internet y biblioteca pública":
            pass

    # 9
    show c feliz
    c "Vaya, ha sido un reto complicado pero aprendí mucho venciéndolo... iEspero que tu también!"

    # 10
    show c apuntaDerecha at left
    show fase2grafico1 at right
    c "Los pasos que vimos fueron:"
    c "-Generación de alternativas. -Evaluar los resultados finales. -La orientación que es transformar el problema en un reto. -Decidir cuál o cuáles opciones me ayudaran a resolver el problema. -Encontrar el problema a resolver. -Poner en práctica la solución."

    # 11
    hide fase2grafico1
    show c triste at center
    c "Ummm... creo que ese no era el orden..."

label eleccion11_1_start:
    menu:
        c "¿cuál será eI primer paso?"

        "Generación de alternativas.":
            # 11a
            show c decepcion
            c "Umm... creo que no es... probemos de nuevo."
            jump eleccion11_1_start

        "Evaluar los resultados finales.":
            # 11a
            show c decepcion
            c "Umm... creo que no es... probemos de nuevo."
            jump eleccion11_1_start

        "La orientación que es transformar el problema en un reto.":
            # 11b
            jump eleccion11_1_final

        "Decidir cuál o cuáles opciones me ayudaran a resolver el problema.":
            # 11a
            show c decepcion
            c "Umm... creo que no es... probemos de nuevo."
            jump eleccion11_1_start

label eleccion11_1_final:
    # 11b
    show c feliz
    c "Gracias!!! Si ahora recuerdo ese era el primer paso."

label eleccion11_2_start:
    menu:
        c "El segundo era..."

        "Generación de alternativas.":
            # 11c
            show c decepcion
            c "Umm... creo que no es... probemos de nuevo."
            jump eleccion11_2_start

        "Evaluar los resultados finales.":
            # 11c
            show c decepcion
            c "Umm... creo que no es... probemos de nuevo."
            jump eleccion11_2_start

        "Decidir cuál o cuáles opciones me ayudaran a resolver el problema.":
            # 11c
            show c decepcion
            c "Umm... creo que no es... probemos de nuevo."
            jump eleccion11_2_start

        "Encontrar el problema a resolver.":
            # 11d
            jump eleccion11_2_final

label eleccion11_2_final:
    # 11d
    show c sonreir
    c "Cierto!"

label eleccion11_3_start:
    menu:
        c "El tercerooo???..."

        "Generación de alternativas.":
            # 11f
            jump eleccion11_3_final

        "Evaluar los resultados finales.":
            # 11e
            show c decepcion
            c "Umm... creo que no es... probemos de nuevo."
            jump eleccion11_3_start

        "Decidir cuál o cuáles opciones me ayudaran a resolver el problema.":
            # 11e
            show c decepcion
            c "Umm... creo que no es... probemos de nuevo."
            jump eleccion11_3_start

        "Poner en práctica la solución.":
            # 11e
            show c decepcion
            c "Umm... creo que no es... probemos de nuevo."
            jump eleccion11_3_start

label eleccion11_3_final:
    # 11f
    show c sonreir
    c "Tienes razón, este es."

label eleccion11_4_start:
    menu:
        c "¿EI cuarto será?"

        "Evaluar los resultados finales.":
            # 11g
            show c decepcion
            c "Umm... creo que no es... probemos de nuevo."
            jump eleccion11_4_start

        "Decidir cuál o cuáles opciones me ayudaran a resolver el problema.":
            # 11h
            jump eleccion11_4_final

        "Poner en práctica la solución.":
            # 11g
            show c decepcion
            c "Umm... creo que no es... probemos de nuevo."
            jump eleccion11_4_start

label eleccion11_4_final:
    # 11h
    show c sonreir
    c "Si! Decidir cómo resolver el problema!"

label eleccion11_5_start:
    menu:
        c "¿Que seguía?"

        "Evaluar los resultados finales.":
            # 11i
            show c decepcion
            c "Umm... creo que no es... probemos de nuevo."
            jump eleccion11_5_start

        "Poner en práctica la solución.":
            pass
    
    # 11j
    show c apuntaDerecha at left
    c "Claro! Bien, ahora sabemos que al final quedaría así:"

    # 12
    show fase2grafico2 at right
    c "Los pasos que vimos fueron:"
    c "1-La orientación que.es transformar el problema en un reto. 2-Encontrar el problema a resolver. 3-Generación de alternativas de respuesta. 4-Decidir cuál o cuáles opciones me ayudaran a resolver el problema. 5-Poner en práctica la solución. 6-Evaluar los resultados finales."

    # 13
    hide fase2grafico2
    show c calma at center
    c "Vaya, ha sido un proceso intenso, Muchas gracias por acompañarme este día."

    # 14
    show c sonreir
    c "Te espero en la próxima. Hasta luego!!!"

    jump Finale2
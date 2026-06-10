label Fase3:
    # 1
    scene bg Cuarto
    show c saluda
    c "Hola, me da gusto verte de nuevo, en esta sesión conoceremos la conducta asertiva. Comportarnos de manera asertiva, nos permite cuidar de nuestros derechos y los de los demás, se trata de expresar nuestros sentimientos y gustos de forma clara honesta y adecuada. Interesante verdad."

    # 2
    show c apuntaDerecha
    c "Hoy me acompañaras de nuevo durante un día de clases, apóyame eligiendo los comportamientos asertivos que me ayudaran a sentirme mejor."

    # 3
    show c callar
    c "El día de hoy me he levantado una hora antes para preparar exposición con mi amigo de la infancia, son las 6 a.m. él llegara a las 7 a.m. para ensayar y luego irnos a la escuela."

    # 3_
    scene bg Comedor
    show c sonreir
    c "7 am, listo! preparé las lecturas. John no tardará en llegar ya 10 veras."

    # 3__
    show c triste
    c "7:10 ya se está tardando, bueno no es tan tarde."

    # 3a_
    show c dormir
    c "..."

    # 3a__
    show c enojar
    c "7:30 John!!!! Me las vas a pagar, no ensayamos nada y me levante temprano. Si le hablo por teléfono puedo despertar a sus abuelos..."

    # 3a___
    show c piensa
    c "Tengo que irme a las 7:45 para la escuela y así llegar a tiempo..."

label eleccion111_1_start:
    menu:
        "¿qué hago?"

        "Estudiar mi parte.":
            # 3b
            show c gracia
            c "Comportamiento Asertivo: Tengo hambre y necesito comer para estar bien en la escuela, el hecho de que John no llegue a tiempo, no implica que yo tenga que descuidarme."

            # 3e
            show c sonreir
            c "Cuando elegimos el comportamiento asertivo respetamos nuestros derechos y sentimientos."
            jump eleccion111_1_final

        "Esperar quizá llegue en este momento y él no ha estudiado tampoco.":
            # 3c
            show c callar
            c "Comportamiento pasivo."

            # 3d
            c "Ummm... ¿Qué es el comportamiento pasivo? EI comportamiento pasivo es cuando hacemos algo que niega nuestros propios derechos y/o sentimientos. Bueno, como no los conocías volvamos a tomar la decisión."
            jump eleccion111_1_start

label eleccion111_2_start:
    scene bg vacio
    # transicion a el pasado
    jump eleccion111_1_final

label eleccion111_1_final:
    # 4
    scene bg Comedor
    show c calma
    c "Terminé, ya me siento mejor, son las 7:45 me voy a la escuela."
    show c gritar
    c "John!"

    # 4_
    scene bg puerta
    show ee saludar
    ee "Hola justo iba a tocar la puerta para irnos juntos, no pude llegar a tiempo pues me desvele haciendo tarea."

    # 4__
    menu:
        c "..."

        "No te preocupes, preparé las lecturas como acordamos, no sacaremos muy buena calificación pero podemos leerlas sin preparar exposición.":
            # 4a
            scene bg vestibulo
            show c calma
            c "Comportamiento pasivo: EI comportamiento pasivo es cuando hacemos algo que niega nuestros propios derechos y/o sentimientos. En este caso Siegfried estaba molesto y sentía frustración por levantarse temprano sin embargo no tomo en cuenta sus sentimientos Y actuó de forma pasiva con John."

            # 4d
            scene bg parque
            show c incomodo at left
            show ee calma at right
            "Siegfried y John se van a la escuela pero Siegfried no se siente nada bien con John ni consigo mismo."
            c "creo que esto no es 10 que deseo para mí."
            jump eleccion111_2_start

        "Pero qué te pasa, encima que llegas tarde, pasa por mí como si nada, jamás trabajaremos en equipo de nuevo, no se puede ser más flojo.":
            # 4b
            scene bg vestibulo
            show c enojar
            c "Comportamiento agresivo: Se da cuando negamos los sentimientos y derechos del otro, le culpamos, insultamos u otras cosas que pueden hacer sentir mal o poner a la defensiva a la otra persona."

            # 4e
            scene bg puerta
            show ee explicar
            ee "Espera, fue un trabajo extra y si no te pude hablar fue porque me quede dormido mientras trabajaba, de hecho, acabo de terminar eI trabajo hace unos minutos."

            # 4e_
            scene bg parque
            show c incomodo at left
            show ee incomodo at right
            "Siegfriedy John se van a la escuela, pero ambos no pueden dejar de sentirse incomodos."
            c "creo que esto no es lo que deseo para mí."
            jump eleccion111_2_start

        "Te he esperado desde las 7:00 como acordamos, me hubiera gustado que al menos me hubieras avisado que llegarías tarde, fue algo molesto para mí.":
            # 4c
            scene bg vestibulo
            show c decidirse
            c "Comportamiento Asertivo: Siegfried respeto sus sentimientos de frustración y el trabajo que hizo al levantarse antes de 10 normal, por lo que, sin insultos, se 10 hizo saber a John y le hizo saber que hubiera preferido que él hubiera pensado en sus derechos."

            # 4f
            scene bg puerta
            show ee decepcion
            ee "Tienes razón reconozco que te hice daño sin querer al no avisarte, déjame compensarlo de alguna forma..."
            jump eleccion111_2_final
            
label eleccion111_3_start:
    scene bg vacio
    # transicion a el pasado
    jump eleccion111_2_final

label eleccion111_2_final:
    # 5
    scene bg cancha
    show c sonreir
    c "Vaya, el día está cada vez mejor, John me ha invitado a jugar futbol es la primera vez que juego en la escuela."

    # 6
    show c apuntaDerecha
    c "Parece que están eligiendo posiciones, quiero jugar en el campo, realmente no me gustaría jugar en la portería... Aunque bueno nunca he jugado,"
    menu:
        c "¿qué debería hacer?"

        "Me acercaré, además hay otros que se ven mucho más malos que yo.":
            # 6a
            show c gritar at left
            show fase3grafico1 at right
            c "quiero jugar en la delantera, soy más alto que esos niños y se ven muy malos, uno de ellos debería ser portero."

            # 6d
            show c incomodo at center
            show fase3grafico2 at left
            show fase3grafico3 at right
            "Siegfried ha logrado jugar en el campo pero ataco a dos niños de quienes se burlaron y empezaron a llamar con apodos por su corta estatura. Comportamiento agresivo: la persona actúa sobre los derechos de los demás, menosprecia a otros, puede lograr sus metas, pero lastima a los demás."
            jump eleccion111_3_start

        "No sé si jugaré bien, si elijo y no juego bien, mejor será que me pongan en la posición en la que crean mejor.":
            # 6b
            show c alienado 
            show fase3grafico1 at right
            #TODO: genero
            "Los comoañeros de Siegfried 10 vieron muv aDartado, quizá tiene miedo de jugar pensaron, vamos a ponerlo en la portería para que se vaya acostumbrando."

            # 6e
            show ee triste at left
            "Siegfried no podrá jugar en el campo como quería, se siente triste y quizá algo humillado... Quizá creen que soy muy malo, quizá es por mi altura. Ellos saben más de futbol que yo. Comportamiento pasivo: la persona deja que los demás decidan por ella, difícilmente logra la meta deseada."
            jump eleccion111_3_start

        "Quiero jugar en el campo, me propondré para jugar donde quiero, así me divertiré.":
            # 6c
            show fase3grafico4 at right
            show c decidirse
            c "Hola, sé que es la primera vez que juego pero de verdad quiero jugar en el campo, voy a poner mi mayor esfuerzo para que ganemos."

            # 6f
            show c orgulloso at left
            show ee sonreir at right
            ee "Fue divertido verdad, sabes que te íbamos a poner en la portería por ser nuevo pero se te vio que tenías muchas ganas, por eso creímos que estaría bien que jugaras en el campo. Aunque te cansaste muy rápido."

            # 6f_
            show c alagado at left
            show ee alagado at right
            c "si me divertí mucho aunque al final por cansancio jugué también en la portería."
            "Comportamiento asertivo: La persona se valora así misma, se expresa, decide por sí misma y tiene más posibilidades de lograr la meta deseada."
            jump eleccion111_3_final
            
label eleccion111_4_start:
    scene bg vacio
    # transicion a el pasado
    jump eleccion111_3_final

label eleccion111_3_final:
    # 7
    scene bg salon
    show c sonreir
    c "Bien, ha terminado mi día de clases, Gracias por cuidar bien de mí."

    # 8
    hide c
    show npcF sonreir at right
    npcF "Hola amigo, podrías llevarte mi mochila a tu casa, nos vamos a ir de compras y no quiero estarla cargando."
    
    # 8_
    show c piensa at left
    show npcF sonreir at right
    c "Umm, tengo que llegar por las verduras que dijo mi mamá, no podría cargar con dos mochilas y las verduras, no quiero hacer eso..."

    menu:
        "¿qué le digo?"

        "No voy a cargar tus cosas para que tú te diviertas, no soy una mula.":
            # 8a
            show c enojar
            "Respuesta agresiva"
            jump eleccion111_4_start

        "Lo siento, pero realmente hoy no puedo hacer eso.":
            # 8b
            show c explicar
            "Respuesta asertiva"
            jump eleccion111_4_final

        "Hoy no podría hacerlo.":
            # 8b
            show c explicar
            "Respuesta asertiva"
            jump eleccion111_4_final

        "Voy a batallar pero está bien, ya veré que hago.":
            # 8c
            show c incomodo at left
            "Respuesta pasiva"
            jump eleccion111_4_start
           
label eleccion111_5_start:
    scene bg vacio
    # transicion a el pasado
    jump eleccion111_4_final

label eleccion111_4_final:
    # 8d
    scene bg salon
    show c incomodo at left
    show npcF sonreir at right
    npcF "¿En serio...?, ándale es que ya nos vamos y me voy a ver muy mal con la mochila en el centro comercial, mis amigas ya encargaron la suya, anda no seas malo"
    menu:
        "¿qué le digo?"

        "De verdad, hoy no puedo hacerlo, por favor busca otra opción.":
            # 9
            "En ocasiones las personas no están acostumbradas a aceptar una respuesta negativa. EI cambiar de opinión sin razones suficientes decae en falta de asertividad. Pero es importante saber que el aceptar un no como respuesta a una petición nuestra, es también ser asertivo, así como esperamos que respeten nuestros no, conlleva aceptar el no de los demás."
            jump eleccion111_5_final

        "Bueno está bien, yo te ayudo, perdona por hacerme del rogar.":
            # 8c
            show c incomodo at left
            "Respuesta pasiva"
            jump eleccion111_4_start

        "Pero no entiendes ya te dije que no, no voy a cargar tus cosas para que tú te diviertas.":
            # 8a
            show c enojar
            "Respuesta agresiva"
            jump eleccion111_4_start
           
label eleccion111_6_start:
    scene bg vacio
    # transicion a el pasado
    jump eleccion111_5_final

label eleccion111_5_final:
    # 10
    scene bg salon
    show c decepcion at left
    show npcF carisma at right
    npcF "Umm, si quieres, yo te hago las compras de tu mamá para que no des la vuelta al mercado y tú me cargas mi mochila, te llevo pronto el mandado, no te preocupes."
    menu:
        "¿qué le digo?"

        "Está bien, pero no tardes mucho pues mi mamá se enojaría mucho.":
            # 8c
            show c incomodo
            "Respuesta pasiva"
            jump eleccion111_4_start

        "Gracias por querer ayudarme, pero estaré bien.":
            # 11
            show c sonreir
            jump eleccion111_6_final

        "Por favor, no seas fastidiosa.":
            # 8a
            show c enojar
            "Respuesta agresiva"
            jump eleccion111_4_start

label eleccion111_7_start:
    scene bg vacio
    # transicion a el pasado
    jump eleccion111_6_final

label eleccion111_6_final:
    # 12
    scene bg salon
    show c decepcion at left
    show npcF burla at right
    npcF "Umm... como te tiene tu mamá, de seguro es muy regañona o tu muy miedoso"
    menu:
        "¿qué le digo?"

        "No decir nada, aceptar la mochila de la compañera.":
            # 8c
            show c incomodo
            "Respuesta pasiva"
            jump eleccion111_4_start

        "No me gusta lo que estás haciendo, hablaremos en otra ocasión":
            # 13
            show c sonreir
            show npcF enojar at right
            npcF "Hay está bien le diré a alguien más que si me haga el favor."

            # 14
            hide npcF
            show c sonreir at center
            c "Gracias por apoyarme a resolver este caso."
            jump eleccion111_7_final

        "Quiero que dejes de hacer eso, hablaremos en otra ocasión.":
            # 13
            show c sonreir
            show npcF enojar at right
            npcF "Hay está bien le diré a alguien más que si me haga el favor."

            # 14
            hide npcF
            show c sonreir at center
            c "Gracias por apoyarme a resolver este caso."
            jump eleccion111_7_final
        
        "Calla jamás volveré a hacerte un favor para que ni 10 pidas.":
            # 8a
            show c enojar
            "Respuesta agresiva"
            jump eleccion111_4_start
           
label eleccion111_8_start:
    scene bg vacio
    # transicion a el pasado
    jump eleccion111_7_final

label eleccion111_7_final:
    # 15
    scene bg salon
    hide c
    show prof saludar at right
    prof "Hola Siegfried antes de que te vayas te quiero felicitar por tu gran trabajo en ciencias naturales, una compañera tuya 10 hizo casi también como tú, los dos irán al concurso."
    menu:
        "¿qué le digo?"

        "Muchas gracias profesor.":
            # 15a
            show prof calma
            prof "Claro es merecido, hasta luego Siegfried"
            "(EI maestro se ve satisfecho)."
            jump eleccion111_8_final

        "Mi compañera es muy aplicada, aunque yo no tanto.":
            # 15b
            show prof incomodo
            prof "Bueno hasta luego Siegfried."
            "(El maestro se ve triste)"
            jump eleccion111_8_start

        "Qué bueno escuchar que me fue bien.":
            # 15a
            show prof calma
            prof "Claro es merecido, hasta luego Siegfried"
            "(EI maestro se ve satisfecho)."
            jump eleccion111_8_final
        
        "Bueno seguramente 10 hice mejor que mi compañera.":
            # 15c
            show prof desconcertado
            prof "Eeh bueno, nos vemos pronto Siegfried"
            "(EI maestro se ve sorprendido)."
            jump eleccion111_8_start

label eleccion111_9_start:
    scene bg vacio
    # transicion a el pasado
    jump eleccion111_8_final

label eleccion111_8_final:
    # 16
    scene bg salon2
    show c orgulloso at left
    show e saludar at right
    e "Siegfried, me entere que iremos al concurso."
    c "Entonces eras tú, eI maestro no me dijo quien era."
    menu:
        "¿qué le digo?"

        "Creo que hiciste un trabajo excelente.":
            jump eleccion111_9_final

        "Tu investigación es muy buena.":
            jump eleccion111_9_final

        "Enterate que el maestro dijo que mi tarea fue la mejor.":
            jump eleccion111_9_start
        
        "Tuve mucha suerte en hacer el trabajo, quizá el maestro se equivocó conmigo.":
            jump eleccion111_9_start

label eleccion111_9_final:
    # 17
    show c sonreir at left
    show e sonreir at right
    c "Así que haré equipo con Isell para el concurso, ieso será genial! Bien, hemos acabado nuestra sesión sobre asertividad, espero te hayas divertido como yo."
    c "Hasta pronto!!!"
    
    jump Finale3

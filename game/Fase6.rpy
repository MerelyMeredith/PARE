label Fase6:
    # 1
    scene bg Cama
    show c durmiendo
    "Y así Ygritte se fue a dormir sintiéndose satisfecha por un día lleno de retos enfrentados."

    # 2
    "Durante el sueño empezó a sentir que una persona conocida se aparecía"
    "Siento que la conozco pensaba Ygritte."

    # 3
    scene bg void
    show eee forma0
    "Pero no sabía si era familiar, amigo o compañera de la escuela. Se sentía como esas personas que quizá no sean tan cercanas pero que estaría bien tener una buena relación con ellas."

    # 4
    show eee forma1
    c "Entonces esa silueta apenas perceptible se va haciendo verde como una masa sin forma..."

    # 5
    hide eee 
    c "Sobrevive a la agresión."

    # 6
    show eee
    eee "Hola Ygritte te has portado muy mal...\n"
    extend "He venido a vengarme."

    # 7
    show eee atacando
    "EI monstruo hecha una masa verde pegajosa a Ygritte."

    # 8
    hide eee 
    show c atacada
    "La masa verde se ha pegado a Ygritte."
    eee "Con esto te aplastaré."

    #9
    show eee atacando
    show c atacada
    eee "Umm... Ahora recuerdo que empataron en el juego de futbol,si fueras mejor y hubieras metido más goles hubieran ganado."
    "Ygritte siente que la masa que le ha pegado se vuelve tensa. Ygritte dice:" 

    label Fase6Eleccion1_Inicio:
        menu: 
                #1
                "Tienes envidia porque no puedes jugar... ni siquiera tienes pies.":
                    pass
                    
                #2
                "Ygritte sonríe y dice gracias por recordármelo, tienes razon puedo ser mejor.":
                    pass

                #3
                "No responde pero piensa que es cierto lo que él dice... Ygritte dice para sí misma... lo siento.":
                    pass
                
   
    #10a
    "La masa se envuelve en el cuerpo de Ygritte."
    eee "Ah te crees muy lista, eres una de las mías, recuerdo que pensaste en hacer burla de tus compañeras para poder jugar tú, por eso estas pagando ahora. Ja ja ja ja ja, Ygritte me parece que eres una egoísta."

    label Fase6Eleccion2_Inicio:
        menu:
            #1
            "No responde, pero piensa que es cierto que él dice... Ygritte dice para sí misma... lo siento.":
                #11b
                "La masa verde empieza a apretar duramente a Ygritte" 

            #2
            "Tú lo has dicho, tú eres el egoísta.":
                #11b
                "La masa verde empieza a apretar duramente a Ygritte" 
            
            #3
            "Eso parezco ¿no es así?":
                #11a
                "La masa se envuelve en el cuerpo de Ygritte." 
               

    #11 
    eee "Ja! Deberías saberlo, tú no solo pareces... ERES!!!! Egoísta."

    label Fase6Eleccion3_Inicio:
        menu :
            #1
            "Quizá tienes razón":
                #12b
                "La masa se envuelve en el cuerpo de Ygritte."
            #2
            "Lo siento, lo siento! !":
                #12c
                "La masa verde empieza a apretar duramente a Ygritte y esta a punto de apoderarse de ella"
            #3
            "Pero no verde!":
                #12c
                "La masa verde empieza a apretar duramente a Ygritte y esta a punto de apoderarse de ella"
    
    #12 
    eee "Eres egoísta y más fea por dentro que yo por fuera"

    label Fase6Eleccion4_Inicio:
        menu :
            #1
            "Seré egoísta pero nadie te gana en lo Horrible!":
                
            #2
            "Si tú lo dices.":
                pass
            #3
            "Lo siento soy una mala persona":
                pass

    label Fase6Fail:
        "Ygritte ha sido atrapada por el moustro."
        menu:
            "Pulsa OK para reiniciar."
            #
            "OK":
                jump Fase6Eleccion1_Inicio 
        
       
            
        
                
        
      
    


    

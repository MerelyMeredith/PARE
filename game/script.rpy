define NombreGuia = "GUIA"
define c = Character(NombreGuia)

define NombreEjemplar1 = "EJEMPLAR1"
define e = Character(NombreEjemplar1)

define NombreEjemplar2 = "EJEMPLAR2"
define ee = Character(NombreEjemplar2)

define NombreEjemplar3 = "EJEMPLAR3"
define eee = Character(NombreEjemplar3)

define NpcFem = "Compañera"
define npcF = Character(NpcFem)

define Profesor = "Profesor"
define prof = Character(Profesor)

label start:
    scene bg vacio
    menu:
        "Genero"

        "Mujer.":
            $ genero = fem
            "[genero.suj]"

        "Hombre.":
            $ genero = masc
            "[genero.suj]"

        "No Binario.":
            $ genero = neu
            "[genero.suj]"

label Menu:
    scene bg vacio
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

label Finale1:
    jump Menu

label Finale2:
    jump Menu

label Finale3:
    jump Menu
    
label Finale4:
    jump Menu
    
label Finale5:
    jump Menu

# Acciones de Guia:
# saluda
# piensa
# gracia
# apuntaDerecha
# sonreir
# callar
# gritar
# decepcion
# calma
# explicar
# estirar
# celebrar
# enojar
# triste
# decidirse
# leer
# feliz
# dormir
# incomodo
# alienado
# alagado
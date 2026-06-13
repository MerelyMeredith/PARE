define NombreGuia = "GUIA"
define c = Character(NombreGuia)

define NombreEjemplar1 = "EJEMPLAR1"
define e = Character(NombreEjemplar1)

define NombreEjemplar2 = "EJEMPLAR2"
define ee = Character(NombreEjemplar2)

define NpcFem = "Compañera"
define npcF = Character(NpcFem)

define Profesor = "Profesor"
define prof = Character(Profesor)

define Gender = ""


label start:
    scene bg vacio
    menu:
        "Genero?"

        "Mujer.":
            $ Gender = "Ella"

        "Hombre.":
            $ Gender = "El"

        "Otro.":
            $ Gender = "Otro"

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
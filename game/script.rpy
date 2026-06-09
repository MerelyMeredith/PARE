define NombreGuia = "GUIA"
define NombreEjemplar = "EJEMPLAR"
define c = Character(NombreGuia)
define e = Character(NombreEjemplar)
define Gender = ""


label Start:
    menu:
        "Genero?"

        "Mujer.":
            $ Gender = "Ella"

        "Hombre.":
            $ Gender = "El"

        "Otro.":
            $ Gender = "Otro"

label Menu:
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
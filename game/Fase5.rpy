label Fase5:
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

label Fase5Parte2:
    # 3
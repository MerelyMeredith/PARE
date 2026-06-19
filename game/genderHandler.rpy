init python:
    class Pronoun:
        def __init__(self, suj, obj, term):
            self.suj = suj    # Pronombre de sujeto (él / ella / elle)
            self.obj = obj    # Pronombre de objeto (lo / la / le)
            self.term = term  # Terminación adjetivos (o / a / e -> p.ej. cansado/cansada/cansade)

    masc = Pronoun("él", "lo", "o")
    fem = Pronoun("ella", "la", "a")
    neu = Pronoun("elle", "le", "e") # Usando 'elle' y lenguaje inclusivo 'e' para adjetivos

def llibres_per_categoria(biblioteca, categoria):
    """
    Nom de la funció: 
        llibres_per_categoria
    Paràmetres:
        prestecs (llista de diccionaris): Les dades dels llibres i els seus préstecs.
        categoria (string): La categoria de llibres a buscar.
    Retorna:
        llista: Llista amb els títols dels llibres de la categoria especificada.
    Funcionalitat: 
        Donat el nom d'una categoria, retorna una llista amb tots els títols 
        dels llibres que pertanyen a aquesta categoria.
    Exemple de retorn:
        ["El Quixot", "Don Juan Tenorio"]
    """
    llibres_per_categoria = []
    for llibre in biblioteca:
        if llibre["categoria"] == categoria:
            llibres_per_categoria.append(llibre["llibre"])
    return llibres_per_categoria

def esta_disponible(biblioteca, llibre):
    """
    Nom de la funció: 
        esta_disponible
    Paràmetres:
        prestecs (llista de diccionaris): Les dades dels llibres i els seus préstecs.
        llibre (string): El títol del llibre a comprovar.
    Retorna:
        Boolean: True si el llibre està disponible, False si no ho està.
    Funcionalitat: 
        Comprova si un llibre està disponible per ser prestat, és a dir, 
        si tots els seus préstecs anteriors han estat retornats.
    Exemple de retorn:
        True
    """
    
    for llibre_b in biblioteca:
        if llibre_b["llibre"] == llibre:
            for usuari in llibre_b["prestecs"]:
                if usuari["retornat"] == False:
                    return False
            
    return True

def usuari_te_prestecs(biblioteca, usuari):
    """
    Nom de la funció: 
        usuari_te_prestecs
    Paràmetres:
        prestecs (llista de diccionaris): Les dades dels llibres i els seus préstecs.
        usuari (string): El nom de l'usuari a comprovar.
    Retorna:
        Boolean: True si l'usuari té llibres sense retornar, False si no en té.
    Funcionalitat: 
        Comprova si un usuari té algun llibre pendent de retornar 
        (préstec amb retornat = False).
    Exemple de retorn:
        False
    """
    for llibre in biblioteca:
        for us in llibre["prestecs"]:
            if us["usuari"] == usuari and us["retornat"] == False:
                return True
    return False

def dies_prestec_total(biblioteca, llibre):
    """
    Nom de la funció: 
        dies_prestec_total
    Paràmetres:
        prestecs (llista de diccionaris): Les dades dels llibres i els seus préstecs.
        llibre (string): El títol del llibre a calcular.
    Retorna:
        int: La suma total de dies que el llibre ha estat prestat.
    Funcionalitat: 
        Calcula la suma total de dies que un llibre determinat ha estat prestat, 
        tenint en compte tots els seus préstecs (tant retornats com no retornats).
    Exemple de retorn:
        45
    """
    total = 0
    for llibre_b in biblioteca:
        if llibre_b["llibre"] == llibre:
            for usuari in llibre_b["prestecs"]:
                total += usuari["dies"]
            return total
    return total 

   
def main():
    biblioteca = [
    {
        "llibre": "El Quixot",
        "autor": "Cervantes",
        "categoria": "novel·la",
        "prestecs": [
            {"usuari": "Joan", "dies": 15, "retornat": True},
            {"usuari": "Maria", "dies": 20, "retornat": False},
            {"usuari": "Pere", "dies": 12, "retornat": True}
        ]
    },
    {
        "llibre": "1984",
        "autor": "Orwell",
        "categoria": "ciència-ficció",
        "prestecs": [
            {"usuari": "Pere", "dies": 10, "retornat": True},
            {"usuari": "Anna", "dies": 25, "retornat": True},
            {"usuari": "Marta", "dies": 18, "retornat": False}
        ]
    },
    {
        "llibre": "El Senyor dels Anells",
        "autor": "Tolkien",
        "categoria": "fantasia",
        "prestecs": [
            {"usuari": "Maria", "dies": 30, "retornat": True},
            {"usuari": "Joan", "dies": 22, "retornat": True},
            {"usuari": "Pere", "dies": 15, "retornat": False}
        ]
    },
    {
        "llibre": "Crim i Càstig",
        "autor": "Dostoievski",
        "categoria": "novel·la",
        "prestecs": [
            {"usuari": "Anna", "dies": 28, "retornat": True},
            {"usuari": "Marta", "dies": 14, "retornat": True},
            {"usuari": "Joan", "dies": 21, "retornat": True}
        ]
    }
    ]
    
    # exercici 1
    print(llibres_per_categoria(biblioteca, "novel·la"))

    
    # exercici 2
    print(esta_disponible(biblioteca, "El Senyor dels Anells"))
    
    # exercici 3
    print(usuari_te_prestecs(biblioteca, "Pere"))


    # exercici 4
    print(dies_prestec_total(biblioteca, "El Senyor dels Anells"))  

if __name__ == "__main__":
    main()
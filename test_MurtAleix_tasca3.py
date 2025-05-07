from Prova_escrita_05 import *
import pytest


@pytest.mark.parametrize(
    # test
    "biblioteca, categoria, res_esperat", 
    [
        
        ( # Test 1
            [{"llibre": "El Quixot", "categoria": "novel·la"}, {"llibre": "Crim i Càstig", "categoria": "novel·la"}], 
            "novel·la", # Busca en la categoria de novel·la el llibre que esperem
            ['El Quixot', 'Crim i Càstig'] # Resultat que ha de trobar, en cas d'ester buit voldrá dir que no ha de trobar res
        ),
        
        # ( # Test 2 | ¡Per a aquest segon test he fet que falli extpressament!
        #     [{"llibre": "1984", "categoria": "ciència-ficció"}], 
        #     "fantasia", # Busca en la categoria de novel·la el llibre que esperem
        #     ["1984"] # En aquest cas el resultat no será "1984" ja que està buscant en la categoria de fantasia, pel que no el trobarà i per aixó retorna un valor buit
        # ),
        
        ( # Test 3
            [{"llibre": "El Senyor dels Anells", "categoria": "fantasia"}], 
            "fantasia", # Busca en la categoria de novel·la el llibre que esperem
            ["El Senyor dels Anells"] # Resultat que ha de trobar, en cas d'ester buit voldrá dir que no ha de trobar res
        ),
    ]
)
def test_llibres_per_categoria(biblioteca, categoria, res_esperat):
    """
        Donat el nom d'una categoria, retorna una llista amb tots els títols dels llibres que pertanyen a aquesta categoria.
    """
    assert llibres_per_categoria(biblioteca, categoria) == res_esperat
    
    
@pytest.mark.parametrize(
    "biblioteca, llibre, disponibilitat_esperada", 
    [
        
        ( # Test 1
            [{"llibre": "El Quixot", "prestecs": [{"usuari": "Joan", "dies": 15, "retornat": True}]}], 
            "El Quixot", # Busca en la categoria de novel·la el llibre que esperem
            True # Resultat que ha de trobar, en cas d'ester buit voldrá dir que no ha de trobar res
        ),

        ( # Test 2
            [{"llibre": "Crim i Càstig", "prestecs": [{"usuari": "Marta", "dies": 14, "retornat": True}]}], 
            "Crim i Càstig", # Busca en la categoria de novel·la el llibre que esperem
            True # Resultat que ha de trobar, en cas d'ester buit voldrá dir que no ha de trobar res
        ),
        
        ( # Test 3
            [{"llibre": "El Senyor dels Anells", "prestecs": [{"usuari": "Pere", "dies": 15, "retornat": False}]}], 
            "Crim i Càstig", # Busca en la categoria de novel·la el llibre que esperem, En aquest cas intentem buscar el llibre
            True # En aquest cas, el llibre no és trobat a la biblioteca (no passa el if llibre_b["llibre"] == llibre), pel que el bucle acaba i retorna True
        ),
    ]
)
def test_esta_disponible(biblioteca, llibre, disponibilitat_esperada):
    """
        Comprova si un llibre està disponible per ser prestat, és a dir, si tots els seus préstecs anteriors han estat retornats.
    """

    assert esta_disponible(biblioteca, llibre) == disponibilitat_esperada



@pytest.mark.parametrize(
    "biblioteca, usuari, te_prestecs",
    [
        
        ( # Test 1 
            [{"prestecs": [{"usuari": "Maria", "dies": 20, "retornat": False}]}],
            "Maria", # Busquem per usuari si falta retornar llibres per que miri per tots els llibres.
            True, # Al NO haber retornat el llibre retorna un true significant que te llibres per retornar. 
        ),
        
        ( # Test 2
            [{"prestecs": [{"usuari": "Anna", "dies": 28, "retornat": True}]}],
            "Anna", # Busquem per usuari si falta retornar llibres per que miri per tots els llibres.
            False, # Al tenir la Anna tots els llibres retornats, ens retorna False ja que no ha de retornar res.
        ),
        
        # ( #Test 3 | ¡Per a aquest Tercer test he fet que falli extpressament!
        #     [{"prestecs": [{"usuari": "Maria", "dies": 15, "retornat": False}]}],
        #     "Maria", # Busquem per usuari si falta retornar llibres per que miri per tots els llibres.
        #     False, # Al no tenir-lo/s retornat/s el/s llibres, ens retorna un True significant que ha de retornar algún llibre
        # ),
    ]
)
def test_usuari_te_prestecs(biblioteca, usuari, te_prestecs):
    """ 
        Comprova si un usuari té algun llibre pendent de retornar (préstec amb retornat = False).
    """
    
    assert usuari_te_prestecs(biblioteca, usuari) == te_prestecs

@pytest.mark.parametrize(
    "biblioteca, llibre, esperat_dies_prestec_total",
    [
        
        ( # Test 1
            [{"llibre": "El Quixot", 
              "prestecs": [ # Tots els prestecs de El Quixot -¬
                    {"usuari": "Joan", "dies": 15, "retornat": True},
                    {"usuari": "Maria", "dies": 20, "retornat": False},
                    {"usuari": "Pere", "dies": 12, "retornat": True}
                ]}],
            "El Quixot", # Busquem els nombres que s'han de sumar a partir de el nom del llibre
            47 # Suma de 15 + 20 + 12
        ),
        
        # ( # Test 2 | ¡Per a aquest segon test he fet que falli extpressament!
        #     [{"llibre": "El Senyor dels Anells", 
        #       "prestecs": [ # Tots els prestecs de El Senyor dels Anells -¬
        #             {"usuari": "Maria", "dies": 30, "retornat": True},
        #             {"usuari": "Joan", "dies": 22, "retornat": True},
        #             {"usuari": "Pere", "dies": 15, "retornat": False}
        #         ]}],
        #     "El Senyor dels Anells", # Busquem els nombres que s'han de sumar a partir de el nom del llibre
        #     77 # Suma de 30 + 22 + 15 Feta malament! 
        # ),
        
        ( # Test 3
            [{"llibre": "Crim i Càstig", 
              "prestecs": [ # Tots els prestecs de Crim i Càstig -¬
                    {"usuari": "Anna", "dies": 28, "retornat": True},
                    {"usuari": "Marta", "dies": 14, "retornat": True},
                    {"usuari": "Joan", "dies": 21, "retornat": True}
                ]}],
            "Crim i Càstig", # Busquem els nombres que s'han de sumar a partir de el nom del llibre
            63 # Suma de 28 + 14 + 21
        )
    ]
)
def test_dies_prestec_total(biblioteca, llibre, esperat_dies_prestec_total):
    """ 
        Calcula la suma total de dies que un llibre determinat ha estat prestat, 
        tenint en compte tots els seus préstecs (tant retornats com no retornats).
    """
    
    assert dies_prestec_total(biblioteca, llibre) == esperat_dies_prestec_total

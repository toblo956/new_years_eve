import pandas as pd

INITIAL_SESSION_STATE = {
    "pack_list" : pd.DataFrame({'Grejer' : pd.Series()}),
    "cocktail_responsibilities" : pd.DataFrame({'Namn' : pd.Series(), 'Cocktail' : pd.Series(), 'Ingredienser' : pd.Series()}),
    "food_responsibilities" : pd.DataFrame({'Maträtt' : pd.Series(), 'Namn' : pd.Series(), 'Ingredienser' : pd.Series()}),
    "responsibilities" : pd.DataFrame({'Person': pd.Series(), "Att Köpa" : pd.Series(), "Att ta med" : pd.Series(), "Ansvar" : pd.Series(), "Övrigt" : pd.Series()}),
}



from typing import List, Set
import pandas as pd

"""
Se reciben dos dataframes.

El primero de nacimientos:
* dia_nacimiento (int)
* mes_nacimiento (int, rango 1(enero)-12(diciembre) )
* anio_nacimiento (int)
* peso_al_nacer (int)
* longitud_al_nacer (int)
* id_hospital (int)
* tipo_parto (int, 1 natural, 2 cesárea)

El segundo de hospitales:
* id_hospital (int)
* direccion (string)
* promedio_nacimientos_mensual (float)
"""


def consigna1(nacimientos, hospitales) -> Set[int]:
    """
    Calcular la cantidad de nacimientos para cada uno de los hospitales para el mes de Octubre de 2017 e
    indicar aquellos hospitales que superan el promedio de nacimientos mensuales

    :param nacimientos: dataframe de nacimientos
    :param hospitales: dataframe de hospitales
    :return: set de ids de hospitales que cumplen la condicion
    """
    pass

def consigna2(nacimientos, hospitales) -> pd.DataFrame:
    """
    Comparando el mes de Octubre de 2017 indicar si se incremento el % de cesáreas con respecto a ese mes del año 2016
    en un dataframe con columnas (id_hospital, se_incremento)

    :param nacimientos: dataframe de nacimientos
    :param hospitales: dataframe de hospitales
    :return: dataframe con columnas (id_hospital, se_incremento)
    siendo se_incremento booleano.
    """
    pass

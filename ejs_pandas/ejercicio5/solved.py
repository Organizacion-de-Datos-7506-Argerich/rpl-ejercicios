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
    nacimientos_2017 = nacimientos[(nacimientos['mes_nacimiento']==10) & (nacimientos['anio_nacimiento']==2017)]
    nacimientos_2017 = nacimientos_2017.groupby('id_hospital').agg({'peso_al_nacer': 'count'})
    merged = pd.merge(nacimientos_2017, hospitales, on='id_hospital', how='inner')
    return set(merged[merged.peso_al_nacer > merged.promedio_nacimientos_mensual].id_hospital.tolist())

def consigna2(nacimientos, hospitales) -> pd.DataFrame:
    """
    Comparando el mes de Octubre de 2017 indicar si se incremento el % de cesáreas con respecto a ese mes del año 2016
    en un dataframe con columnas (id_hospital, se_incremento)

    :param nacimientos: dataframe de nacimientos
    :param hospitales: dataframe de hospitales
    :return: dataframe con columnas (id_hospital, se_incremento)
    siendo se_incremento booleano.
    """
    nacimientos_2017 = nacimientos[(nacimientos['mes_nacimiento']==10) & (nacimientos['anio_nacimiento']==2017)]
    nacimientos_2017['cesarea_2017'] = nacimientos_2017['tipo_parto'].map(lambda x: 1 if x==2 else 0)
    nacimientos_2017 = nacimientos_2017.groupby('id_hospital').agg({'cesarea_2017': 'mean'}).reset_index()

    nacimientos_2016 = nacimientos[(nacimientos['mes_nacimiento'] == 10) & (nacimientos['anio_nacimiento'] == 2016)]
    nacimientos_2016['cesarea_2016'] = nacimientos_2016['tipo_parto'].map(lambda x: 1 if x == 2 else 0)
    nacimientos_2016 = nacimientos_2016.groupby('id_hospital').agg({'cesarea_2016': 'mean'}).reset_index()

    merged = pd.merge(nacimientos_2017, nacimientos_2016, on='id_hospital', how='inner')
    merged['se_incremento'] = merged['cesarea_2017'] > merged['cesarea_2016']
    return merged[['id_hospital', 'se_incremento']]




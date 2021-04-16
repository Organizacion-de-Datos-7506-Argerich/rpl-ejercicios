from typing import List, Set
import pandas as pd

"""
Se reciben dos dataframes.

El primero de casos policiales:
* fecha (string con formato, YYYY-MM-DD)
* id_caso (int)
* descripcion (string)
* estado_caso (int, 1: caso abierto, 2: caso resuelto, 3: cerrado sin resolución)
* categoria (string)
* latitud (float)
* longitud (float)

El segundo de batiseñales:
* id_caso (int)
* respuesta (int, 1 si batman respondio, 0 en caso contrario)
"""


def consigna1(casos, batiseniales) -> float:
    """
    Tasa de resolución de casos de la fuerza policial por categoría de caso
    (para aquellos casos en los que no participó Batman).

    :param casos: dataframe de casos policiales
    :param batiseniales: dataframe de batiseñales
    :return: la tasa de resolución pedida
    """
    casos['resuelto'] = casos['estado_caso'] == 2
    casos = pd.merge(casos, batiseniales, on='id_caso', how='left')
    casos['respuesta'] = casos['respuesta'].fillna(0)
    casos = casos[casos['respuesta']==0]
    return casos['resuelto'].mean()

def consigna2(casos, batiseniales) -> float:
    """
    Tasa de resolución de casos con la ayuda de Batman (para aquellos casos en
    los que fue llamado con la batiseñal, participó en la resolución).

    :param casos: dataframe de casos policiales
    :param batiseniales: dataframe de batiseñales
    :return: la tasa de resolución pedida
    """
    casos['resuelto'] = casos['estado_caso'] == 2
    casos = pd.merge(casos, batiseniales, on='id_caso', how='left')
    casos = casos[casos['respuesta'] == 1]
    return casos['resuelto'].mean()

def consigna3(casos, batiseniales) -> str:
    """
    Indicar el mes del año 2020 en el que Batman tuvo mayor participación
    en la investigación de casos.

    :param casos: dataframe de casos policiales
    :param batiseniales: dataframe de batiseñales
    :return: el mes como un string MM
    """
    casos['resuelto'] = casos['estado_caso'] == 2
    casos = pd.merge(casos, batiseniales, on='id_caso', how='left')
    casos = casos[casos['respuesta'] == 1]
    casos['mes'] = casos['fecha'].map(lambda x: x.split('-')[1])
    return casos['mes'].value_counts().index[0]
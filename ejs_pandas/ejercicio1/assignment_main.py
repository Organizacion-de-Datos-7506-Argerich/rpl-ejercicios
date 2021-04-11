from typing import Tuple, Dict

"""
Se recibe un dataframe con columnas: 
* padron (int)
* materia (string)
* nota (int)
* fecha (string de formato DD-MM-YYYY)
"""


def promedio_general(df) -> float:
    """
    Cuál es el promedio general de notas

    :param df: Dataframe con columnas: padron, materia, nota, fecha
    :return: promedio general de notas
    """
    pass


def nota_max_min_2019(df) -> Tuple[int, int]:
    """
    Cuál es la nota más alta y la nota más baja registrada durante el año 2019.

    :param df: Dataframe con columnas: padron, materia, nota, fecha
    :return: nota más alta y más baja de 2019
    """
    pass


def padron_mayor_aprobadas_ult_cuatri(df) -> int:
    """
    Cuál es el padrón con mayor cantidad de materias aprobadas durante el último cuatrimestre

    Hay una función 'calcular_cuatrimestre' que dada una fecha devuelve '1C' o '2C' según que cuatrimetre sea.
    Se dice que una materia esta aprobada si la nota es mayor a >=4

    :param df: Dataframe con columnas: padron, materia, nota, fecha
    :return: padrón con mayor cantidad de materias aprobadas durante el último cuatrimestre
    """
    pass


def nota_promedio_por_materia(df) -> Dict[str, float]:
    """
    Cuál es la nota promedio por materia

    :param df: Dataframe con columnas: padron, materia, nota, fecha
    :return: un diccionario cuya clave es una materia y valor la nota promedio
    """
    pass


def nota_promedio_por_padron(df) -> Dict[int, float]:
    """
    Cuál es la nota promedio por padron

    :param df: Dataframe con columnas: padron, materia, nota, fecha
    :return: un diccionario cuya clave es un padron y valor la nota promedio
    """
    pass

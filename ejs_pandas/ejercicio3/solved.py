import pandas as pd

"""
Se recibe un dataframe con columnas: 
* codigo_producto (int)
* codigo_fabricante (int)
* mes (string)
* ventas_mensuales (int)
"""


def consignaA(df) -> pd.DataFrame:
    """
    Promedio por producto

    :param df: Dataframe
    :return: promedio por producto como indica la consigna
    """
    df = df.groupby('codigo_producto').agg({'ventas_mensuales': 'mean'})
    return df.reset_index().rename(columns={'ventas_mensuales': 'promedio_ventas'})


def consignaB(df) -> pd.DataFrame:
    """
    Mínimo, Máximo y Promedio de ventas por producto

    :param df: Dataframe
    :return: dataframe pedido como en la consigna
    """
    return df.groupby('codigo_producto'). \
        agg({'ventas_mensuales': ['min', 'max', 'mean']}). \
        rename(columns={'min': 'minimo_ventas_mensual',
                        'max': 'maximo_ventas_mensual',
                        'mean': 'promedio_ventas_mensual'})['ventas_mensuales']. \
        reset_index()


def consignaC(df) -> pd.DataFrame:
    """
    Mínimo, Máximo y Promedio de ventas por producto

    :param df: Dataframe
    :return: dataframe pedido como en la consigna
    """
    return df.groupby('codigo_producto'). \
        agg({'ventas_mensuales': ['min', 'max', 'mean']}). \
        rename(columns={'min': 'minimo_ventas_mensual',
                        'max': 'maximo_ventas_mensual',
                        'mean': 'promedio_ventas_mensual'}). \
        stack().reset_index(). \
        rename(columns={'level_1': 'agregado', 'ventas_mensuales': 'valor'}). \
        set_index(['codigo_producto', 'agregado'])


def consignaD(df) -> pd.DataFrame:
    """
    Mínimo, Máximo y Promedio de ventas por producto

    :param df: Dataframe
    :return: dataframe pedido como en la consigna
    """
    return consignaB(df).pivot_table(columns='codigo_producto')


def consignaE(df) -> pd.DataFrame:
    """
     Qué productos son provistos por los distintos fabricantes, indicando True/False

    :param df: Dataframe
    :return: dataframe pedido como en la consigna
    """

    return df.groupby(['codigo_producto', 'codigo_fabricante']).agg({'mes': 'count'}).reset_index(). \
        pivot_table(index=['codigo_producto'], columns=['codigo_fabricante'], values='mes').fillna(0).applymap(
        lambda x: x > 0)

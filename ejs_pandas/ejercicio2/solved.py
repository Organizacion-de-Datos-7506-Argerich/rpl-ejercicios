from typing import List

import pandas as pd

"""
Se recibe un dataframe con columnas: 
* nro_de_transacción (int)
* tipo_de_transacción (string)
* cuenta_origen (int)
* cuenta_destino (int)
* fecha (string tipo dd-mm-aaaa)
* hora (string de tipo hh:mm)
* monto (int)
"""


def transacciones_tienen_tipo(df) -> bool:
    """
    Indica si todas las transacciones tienen tipo o no

    :param df: Dataframe
    :return: True si todas las transacciones tienen tipo
    """
    return df['tipo_de_transacción'].isnull().sum() == 0


def transferencias_tienen_cuenta_destino_y_origen(df) -> bool:
    """
    Indica si todas las transacciones de tipo 'Transferencia'
    tienen o no cuenta de origen Y de destino

    :param df: Dataframe
    :return: True si todas las transferencias tienen destino y origen
    """
    df = df[df['tipo_de_transacción']=='Transferencia']
    return df['cuenta_origen'].isnull().sum() + \
           df['cuenta_destino'].isnull().sum() == 0


def transf_deposito_extraccion_monto_positivo(df) -> bool:
    """
    Indica si todas las transacciones de tipo 'Transferencia', 'Deposito' y 'Extraccion'
    tienen monto >0

    :param df: Dataframe
    :return: True si se cumple la condicion pedida
    """
    df = df[df['tipo_de_transacción'].isin(['Transferencia', 'Deposito', 'Extraccion'])]
    return (df.monto <= 0).sum() == 0


def top10_mayor_monto(df) -> List[int]:
    """
    Indica los ids de las 10 transacciones de mayor monto
    ordenadas de mayor monto a menor

    :param df: Dataframe
    :return: Lista de ints con los ids de las 10 transacciones de mayor monto
    """
    return df.sort_values('monto', ascending=False)['nro_de_transacción'].tolist()[:10]


def transaccion_mayor_monto_promedio(df) -> str:
    """
    Devuelve el tipo de transaccion con mayor monto promedio

    :param df: Dataframe
    :return: Tipo de transacción con mayor monto promedio
    """
    return df.groupby('tipo_de_transacción').agg({'monto': 'mean'}).idxmax()['monto']


def top5_cuentas_mas_transacciones(df) -> List[int]:
    """
    Indicar cuáles son las 5 cuentas involucradas en la mayor cantidad de transacciones.

    :param df: Dataframe
    :return: Top 5 de cuentas con más transacciones
    """
    como_origen = df.groupby('cuenta_origen').agg({'nro_de_transacción': 'count'})
    como_destino = df.groupby('cuenta_destino').agg({'nro_de_transacción': 'count'})
    suma = como_origen.add(como_destino, fill_value=0). \
        sort_values('nro_de_transacción', ascending=False)
    return suma.index.tolist()[:5]


def top5_cuentas_monto_mas_alto_involucrado(df) -> List[int]:
    """
    Top 5 de cuentas con monto más alto involucrado en alguna transacción
    ordenado por monto descendente

    :param df: Dataframe
    :return: Top 5 de cuentas con monto más alto en alguna transaccion
    """
    como_origen = df.sort_values('monto', ascending=False). \
        drop_duplicates('cuenta_origen', keep='first'). \
        set_index('cuenta_origen')['monto']
    como_destino = df.sort_values('monto', ascending=False). \
        drop_duplicates('cuenta_destino', keep='first'). \
        set_index('cuenta_destino')['monto']
    max_df = pd.concat([como_origen, como_destino], axis=1).fillna(0)
    max_df['max'] = max_df.max(axis=1)
    return max_df.sort_values('max', ascending=False).index.tolist()[:5]


def top5_cuentas_mas_transacciones_para_trans_mayor(df) -> List[int]:
    """
    Top 5 de cuentas con más transacciones solo para las
    transacción de mayor monto promedio ordenado por cantidad
    de transacciones descendente

    :param df: Dataframe
    :return: Top 5
    """
    return top5_cuentas_monto_mas_alto_involucrado(
        df[df['tipo_de_transacción'] == transaccion_mayor_monto_promedio(df)])

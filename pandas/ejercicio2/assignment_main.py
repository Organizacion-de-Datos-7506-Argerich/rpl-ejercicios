from typing import List

from utils import *

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
    pass


def transferencias_tienen_cuenta_destino_y_origen(df) -> bool:
    """
    Indica si todas las transacciones de tipo 'Transferencia'
    tienen o no cuenta de origen Y de destino

    :param df: Dataframe
    :return: True si todas las transferencias tienen destino y origen
    """
    pass


def transf_deposito_extraccion_monto_positivo(df) -> bool:
    """
    Indica si todas las transacciones de tipo 'Transferencia', 'Deposito' y 'Extraccion'
    tienen monto >0

    :param df: Dataframe
    :return: True si se cumple la condicion pedida
    """
    pass


def top10_mayor_monto(df) -> List[int]:
    """
    Indica los ids de las 10 transacciones de mayor monto
    ordenadas de mayor monto a menor

    :param df: Dataframe
    :return: Lista de ints con los ids de las 10 transacciones de mayor monto
    """
    pass


def transaccion_mayor_monto_promedio(df) -> str:
    """
    Devuelve el tipo de transaccion con mayor monto promedio

    :param df: Dataframe
    :return: Tipo de transacción con mayor monto promedio
    """
    pass


def top5_cuentas_mas_transacciones(df) -> List[int]:
    """
    Top 5 de cuentas con más transacciones ordenado por cantidad
    de transacciones descendente

    :param df: Dataframe
    :return: Top 5 de cuentas con más transacciones
    """
    pass


def top5_cuentas_monto_mas_alto_involucrado(df) -> List[int]:
    """
    Top 5 de cuentas con monto más alto involucrado en alguna transacción
    ordenado por monto descendente

    :param df: Dataframe
    :return: Top 5 de cuentas con monto más alto en alguna transaccion
    """
    pass


def top5_cuentas_mas_transacciones_para_trans_mayor(df) -> List[int]:
    """
    Top 5 de cuentas con más transacciones solo para las
    transacción de mayor monto promedio ordenado por cantidad
    de transacciones descendente

    :param df: Dataframe
    :return: Top 5
    """
    pass

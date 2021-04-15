import math
import os
import unittest
import pandas as pd

import timeout_decorator

from assignment_main import *

if os.getenv('IS_TRAVIS'):
    from solved import *


class TestMethods(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_transacciones_tienen_tipo_true(self):
        df_data = [
            (1, 'TipoI', 4, 4, '03-01-2021', '00:00', 1),
            (2, 'TipoII', 6, 6, '03-01-2021', '00:00', 1),
            (3, 'TipoIII', 9, 10, '03-01-2021', '00:00', 1),
            (4, 'TipoIV', 2, 20, '03-01-2021', '00:00', 1)
        ]

        df = pd.DataFrame(df_data,
                          columns=['nro_de_transacción', 'tipo_de_transacción',
                                   'cuenta_origen', 'cuenta_destino',
                                   'fecha', 'hora', 'monto'])

        self.assertEqual(transacciones_tienen_tipo(df), True)

    @timeout_decorator.timeout(5)
    def test_transacciones_tienen_tipo_nan(self):
        df_data = [
            (1, 'TipoI', 4, 4, '03-01-2021', '00:00', 1),
            (2, 'TipoII', 6, 6, '03-01-2021', '00:00', 1),
            (3, math.nan, 9, 10, '03-01-2021', '00:00', 1),
            (4, 'TipoIV', 2, 20, '03-01-2021', '00:00', 1)
        ]

        df = pd.DataFrame(df_data,
                          columns=['nro_de_transacción', 'tipo_de_transacción',
                                   'cuenta_origen', 'cuenta_destino',
                                   'fecha', 'hora', 'monto'])

        self.assertEqual(transacciones_tienen_tipo(df), False)

    @timeout_decorator.timeout(5)
    def test_transacciones_tienen_tipo_none(self):
        df_data = [
            (1, 'TipoI', 4, 4, '03-01-2021', '00:00', 1),
            (2, 'TipoII', 6, 6, '03-01-2021', '00:00', 1),
            (3, None, 9, 10, '03-01-2021', '00:00', 1),
            (4, 'TipoIV', 2, 20, '03-01-2021', '00:00', 1)
        ]

        df = pd.DataFrame(df_data,
                          columns=['nro_de_transacción', 'tipo_de_transacción',
                                   'cuenta_origen', 'cuenta_destino',
                                   'fecha', 'hora', 'monto'])

        self.assertEqual(transacciones_tienen_tipo(df), False)

    @timeout_decorator.timeout(5)
    def test_transferencias_destino_y_origen_simple(self):
        df_data = [
            (1, 'Transferencia', 4, 4, '03-01-2021', '00:00', 1),
            (2, 'Transferencia', 6, 6, '03-01-2021', '00:00', 1),
            (3, 'Transferencia', 9, 10, '03-01-2021', '00:00', 1),
            (4, 'Transferencia', 2, 20, '03-01-2021', '00:00', 1),
            (5, 'Prestamo', 4, 30, '03-01-2021', '00:00', 1),
            (6, 'Prestamo', 5, 50, '03-01-2021', '00:00', 1),
            (7, 'Varios', 999, 60, '03-01-2021', '00:00', 1)
        ]

        df = pd.DataFrame(df_data,
                          columns=['nro_de_transacción', 'tipo_de_transacción',
                                   'cuenta_origen', 'cuenta_destino',
                                   'fecha', 'hora', 'monto'])

        self.assertEqual(transferencias_tienen_cuenta_destino_y_origen(df), True)

    @timeout_decorator.timeout(5)
    def test_transferencias_destino_y_origen_false_simple(self):
        df_data = [
            (1, 'Transferencia', 4, 4, '03-01-2021', '00:00', 1),
            (2, 'Transferencia', 6, 6, '03-01-2021', '00:00', 1),
            (3, 'Transferencia', None, None, '03-01-2021', '00:00', 1),
            (4, 'Transferencia', 4, 20, '03-01-2021', '00:00', 1),
            (5, 'Prestamo', None, 30, '03-01-2021', '00:00', 1),
            (6, 'Prestamo', None, 50, '03-01-2021', '00:00', 1),
            (7, 'Varios', 999, 60, '03-01-2021', '00:00', 1)
        ]

        df = pd.DataFrame(df_data,
                          columns=['nro_de_transacción', 'tipo_de_transacción',
                                   'cuenta_origen', 'cuenta_destino',
                                   'fecha', 'hora', 'monto'])

        self.assertEqual(transferencias_tienen_cuenta_destino_y_origen(df), False)

    @timeout_decorator.timeout(5)
    def test_transferencias_destino_y_origen_false_complex(self):
        df_data = [
            (1, 'Transferencia', 4, 4, '03-01-2021', '00:00', 1),
            (2, 'Transferencia', 6, 6, '03-01-2021', '00:00', 1),
            (3, 'Transferencia', 9, 10, '03-01-2021', '00:00', 1),
            (4, 'Transferencia', None, 20, '03-01-2021', '00:00', 1),
            (5, 'Prestamo', None, 30, '03-01-2021', '00:00', 1),
            (6, 'Prestamo', None, 50, '03-01-2021', '00:00', 1),
            (7, 'Varios', 999, 60, '03-01-2021', '00:00', 1)
        ]

        df = pd.DataFrame(df_data,
                          columns=['nro_de_transacción', 'tipo_de_transacción',
                                   'cuenta_origen', 'cuenta_destino',
                                   'fecha', 'hora', 'monto'])

        self.assertEqual(transferencias_tienen_cuenta_destino_y_origen(df), False)

        df_data = [
            (1, 'Transferencia', 4, 4, '03-01-2021', '00:00', 1),
            (2, 'Transferencia', 6, None, '03-01-2021', '00:00', 1),
            (3, 'Transferencia', 9, 10, '03-01-2021', '00:00', 1),
            (4, 'Transferencia', 4, 20, '03-01-2021', '00:00', 1),
            (5, 'Prestamo', None, 30, '03-01-2021', '00:00', 1),
            (6, 'Prestamo', None, 50, '03-01-2021', '00:00', 1),
            (7, 'Varios', 999, 60, '03-01-2021', '00:00', 1)
        ]

        df = pd.DataFrame(df_data,
                          columns=['nro_de_transacción', 'tipo_de_transacción',
                                   'cuenta_origen', 'cuenta_destino',
                                   'fecha', 'hora', 'monto'])

        self.assertEqual(transferencias_tienen_cuenta_destino_y_origen(df), False)

    @timeout_decorator.timeout(5)
    def test_montos_positivos_simple(self):
        df_data = [
            (1, 'Transferencia', 4, 4, '03-01-2021', '00:00', 1),
            (2, 'Transferencia', 6, 6, '03-01-2021', '00:00', 1),
            (3, 'Transferencia', 4, None, '03-01-2021', '00:00', 1),
            (4, 'Transferencia', 4, 20, '03-01-2021', '00:00', 1),
            (5, 'Debito', 5, 30, '03-01-2021', '00:00', 999),
            (6, 'Debito', 65, 50, '03-01-2021', '00:00', 1),
            (7, 'Extraccion', 999, 60, '03-01-2021', '00:00', 1)
        ]

        df = pd.DataFrame(df_data,
                          columns=['nro_de_transacción', 'tipo_de_transacción',
                                   'cuenta_origen', 'cuenta_destino',
                                   'fecha', 'hora', 'monto'])

        self.assertEqual(transf_deposito_extraccion_monto_positivo(df), True)

    @timeout_decorator.timeout(5)
    def test_montos_positivos_false(self):
        df_data = [
            (1, 'Transferencia', 4, 4, '03-01-2021', '00:00', 1),
            (2, 'Transferencia', 6, 6, '03-01-2021', '00:00', 1),
            (3, 'Transferencia', 4, None, '03-01-2021', '00:00', 1),
            (4, 'Transferencia', 4, 20, '03-01-2021', '00:00', 1),
            (5, 'Debito', 5, 30, '03-01-2021', '00:00', 999),
            (6, 'Deposito', 65, 50, '03-01-2021', '00:00', -5),
            (7, 'Extraccion', 999, 60, '03-01-2021', '00:00', 1)
        ]

        df = pd.DataFrame(df_data,
                          columns=['nro_de_transacción', 'tipo_de_transacción',
                                   'cuenta_origen', 'cuenta_destino',
                                   'fecha', 'hora', 'monto'])

        self.assertEqual(transf_deposito_extraccion_monto_positivo(df), False)

        df_data = [
            (1, 'Transferencia', 4, 4, '03-01-2021', '00:00', 1),
            (2, 'Transferencia', 6, 6, '03-01-2021', '00:00', 1),
            (3, 'Transferencia', 4, None, '03-01-2021', '00:00', 1),
            (4, 'Transferencia', 4, 20, '03-01-2021', '00:00', 1),
            (5, 'Debito', 5, 30, '03-01-2021', '00:00', 999),
            (6, 'Deposito', 65, 50, '03-01-2021', '00:00', 777),
            (7, 'Extraccion', 999, 60, '03-01-2021', '00:00', -88)
        ]

        df = pd.DataFrame(df_data,
                          columns=['nro_de_transacción', 'tipo_de_transacción',
                                   'cuenta_origen', 'cuenta_destino',
                                   'fecha', 'hora', 'monto'])

        self.assertEqual(transf_deposito_extraccion_monto_positivo(df), False)

        df_data = [
            (1, 'Transferencia', 4, 4, '03-01-2021', '00:00', 1),
            (2, 'Transferencia', 6, 6, '03-01-2021', '00:00', -6),
            (3, 'Transferencia', 4, None, '03-01-2021', '00:00', 1),
            (4, 'Transferencia', 4, 20, '03-01-2021', '00:00', 1),
            (5, 'Debito', 5, 30, '03-01-2021', '00:00', 999),
            (6, 'Deposito', 65, 50, '03-01-2021', '00:00', 1),
            (7, 'Extraccion', 999, 60, '03-01-2021', '00:00', 1)
        ]

        df = pd.DataFrame(df_data,
                          columns=['nro_de_transacción', 'tipo_de_transacción',
                                   'cuenta_origen', 'cuenta_destino',
                                   'fecha', 'hora', 'monto'])

        self.assertEqual(transf_deposito_extraccion_monto_positivo(df), False)

    @timeout_decorator.timeout(5)
    def test_montos_positivos_false_con_cero(self):
        df_data = [
            (1, 'Transferencia', 4, 4, '03-01-2021', '00:00', 1),
            (2, 'Transferencia', 6, 6, '03-01-2021', '00:00', 1),
            (3, 'Transferencia', 4, None, '03-01-2021', '00:00', 0),
            (4, 'Transferencia', 4, 20, '03-01-2021', '00:00', 1),
            (5, 'Debito', 5, 30, '03-01-2021', '00:00', 999),
            (6, 'Debito', 65, 50, '03-01-2021', '00:00', 777),
            (7, 'Extraccion', 999, 60, '03-01-2021', '00:00', 1)
        ]

        df = pd.DataFrame(df_data,
                          columns=['nro_de_transacción', 'tipo_de_transacción',
                                   'cuenta_origen', 'cuenta_destino',
                                   'fecha', 'hora', 'monto'])

        self.assertEqual(transf_deposito_extraccion_monto_positivo(df), False)

    @timeout_decorator.timeout(5)
    def test_top10_mayor_monto(self):
        df_data = [
            (1, 'Transferencia', 4, 4, '03-01-2021', '00:00', 28),
            (2, 'Transferencia', 6, 6, '03-01-2021', '00:00', 400),
            (3, 'Transferencia', 4, None, '03-01-2021', '00:00', 7),
            (4, 'Transferencia', 4, 20, '03-01-2021', '00:00', 700),
            (5, 'Debito', 5, 30, '03-01-2021', '00:00', -1),
            (6, 'Debito', 65, 50, '03-01-2021', '00:00', 1),
            (7, 'Extraccion', 999, 60, '03-01-2021', '00:00', 1),
            (8, 'Extraccion', 999, 60, '03-01-2021', '00:00', 27000),
            (9, 'Extraccion', None, 60, '03-01-2021', '00:00', 7),
            (10, 'Extraccion', 999, 60, '03-01-2021', '00:00', 500),
            (11, 'Extraccion', 999, 60, '03-01-2021', '00:00', 32),
            (12, 'Extraccion', 999, 60, '03-01-2021', '00:00', 1000),
            (13, 'Extraccion', 999, 60, '03-01-2021', '00:00', 10000),
            (14, 'Extraccion', 999, 60, '03-01-2021', '00:00', 675)
        ]

        df = pd.DataFrame(df_data,
                          columns=['nro_de_transacción', 'tipo_de_transacción',
                                   'cuenta_origen', 'cuenta_destino',
                                   'fecha', 'hora', 'monto'])

        top10 = top10_mayor_monto(df)

        self.assertTrue(top10 == [8, 13, 12, 4, 14, 10, 2, 11, 1, 3] or
                        top10 == [8, 13, 12, 4, 14, 10, 2, 11, 1, 9])

    @timeout_decorator.timeout(5)
    def test_tipo_mayor_monto_promedio(self):
        df_data = [
            (1, 'Transferencia', 4, 4, '03-01-2021', '00:00', 28),
            (2, 'Transferencia', 6, 6, '03-01-2021', '00:00', 400),
            (3, 'Transferencia', 4, None, '03-01-2021', '00:00', 7),
            (4, 'Transferencia', 4, 20, '03-01-2021', '00:00', 700),
            (5, 'Debito', 5, 30, '03-01-2021', '00:00', -10000000),
            (6, 'Debito', 65, 50, '03-01-2021', '00:00', 1),
            (7, 'Extraccion', 999, 60, '03-01-2021', '00:00', 1),
            (8, 'Debito', 999, 60, '03-01-2021', '00:00', 27000),
            (9, 'Extraccion', None, 60, '03-01-2021', '00:00', 7),
            (10, 'Extraccion', 999, 60, '03-01-2021', '00:00', 500),
            (11, 'Extraccion', 999, 60, '03-01-2021', '00:00', 32),
            (12, 'Extraccion', 999, 60, '03-01-2021', '00:00', 1000),
            (13, 'Extraccion', 999, 60, '03-01-2021', '00:00', 10000),
            (14, 'Extraccion', 999, 60, '03-01-2021', '00:00', 675)
        ]

        df = pd.DataFrame(df_data,
                          columns=['nro_de_transacción', 'tipo_de_transacción',
                                   'cuenta_origen', 'cuenta_destino',
                                   'fecha', 'hora', 'monto'])

        self.assertEqual(transaccion_mayor_monto_promedio(df), 'Extraccion')

    @timeout_decorator.timeout(5)
    def test_top5_cuentas_mas_transacciones(self):
        df_data = [
            (1, 'Transferencia', 6, 4, '03-01-2021', '00:00', 28),
            (2, 'Transferencia', 6, 4, '03-01-2021', '00:00', 400),
            (3, 'Transferencia', 6, 4, '03-01-2021', '00:00', 7),
            (4, 'Transferencia', 0, 4, '03-01-2021', '00:00', 700),
            (5, 'Debito', 5, 60, '03-01-2021', '00:00', -10000000),
            (6, 'Debito', 65, 5, '03-01-2021', '00:00', 1),
            (7, 'Extraccion', 4, 5, '03-01-2021', '00:00', 1),
            (8, 'Debito', 60, 999, '03-01-2021', '00:00', 27000),
            (9, 'Extraccion', 0, 60, '03-01-2021', '00:00', 7),
            (10, 'Extraccion', 65, 999, '03-01-2021', '00:00', 500),
            (11, 'Extraccion', 999, 60, '03-01-2021', '00:00', 32),
            (12, 'Extraccion', 5, 60, '03-01-2021', '00:00', 1000),
            (13, 'Extraccion', 999, 65, '03-01-2021', '00:00', 10000),
            (14, 'Extraccion', 999, 65, '03-01-2021', '00:00', 675)
        ]

        df = pd.DataFrame(df_data,
                          columns=['nro_de_transacción', 'tipo_de_transacción',
                                   'cuenta_origen', 'cuenta_destino',
                                   'fecha', 'hora', 'monto'])

        top5 = top5_cuentas_mas_transacciones(df)

        self.assertEqual(set(top5[:3]), {999, 4, 60})
        self.assertEqual(set(top5[3:]), {5, 65})

    @timeout_decorator.timeout(5)
    def test_top5_cuentas_involucradas_en_monto_mas_alto(self):
        df_data = [
            (1, 'Transferencia', 6, 4, '03-01-2021', '00:00', 28),
            (2, 'Transferencia', 6, 4, '03-01-2021', '00:00', 400),
            (3, 'Transferencia', 6, 0, '03-01-2021', '00:00', 7),
            (4, 'Transferencia', 4, 4, '03-01-2021', '00:00', 700),
            (5, 'Debito', 5, 5, '03-01-2021', '00:00', -10000000),
            (6, 'Debito', 65, 5, '03-01-2021', '00:00', 1),
            (7, 'Extraccion', 4, 60, '03-01-2021', '00:00', 1),
            (8, 'Debito', 60, 999, '03-01-2021', '00:00', 27000),
            (9, 'Extraccion', 0, 60, '03-01-2021', '00:00', 7),
            (10, 'Extraccion', 65, 999, '03-01-2021', '00:00', 500),
            (11, 'Extraccion', 999, 60, '03-01-2021', '00:00', 32),
            (12, 'Extraccion', 5, 60, '03-01-2021', '00:00', 1000),
            (13, 'Extraccion', 999, 65, '03-01-2021', '00:00', 10000),
            (14, 'Extraccion', 999, 65, '03-01-2021', '00:00', 675)
        ]

        df = pd.DataFrame(df_data,
                          columns=['nro_de_transacción', 'tipo_de_transacción',
                                   'cuenta_origen', 'cuenta_destino',
                                   'fecha', 'hora', 'monto'])

        top5 = top5_cuentas_monto_mas_alto_involucrado(df)

        self.assertEqual(set(top5[:2]), {60, 999})
        self.assertEqual(top5[2], 65)
        self.assertEqual(top5[3], 5)
        self.assertEqual(top5[4], 4)

    @timeout_decorator.timeout(5)
    def test_top5_cuentas_mas_transacciones_para_trans_mayor(self):
        df_data = [
            (1, 'Transferencia', 6, 4, '03-01-2021', '00:00', 28),
            (2, 'Transferencia', 6, 4, '03-01-2021', '00:00', 400),
            (3, 'Transferencia', 6, 4, '03-01-2021', '00:00', 7),
            (4, 'Transferencia', 0, 4, '03-01-2021', '00:00', 700),
            (5, 'Debito', 5, 60, '03-01-2021', '00:00', -10000000),
            (6, 'Debito', 65, 5, '03-01-2021', '00:00', 1),
            (7, 'Extraccion', 4, 5, '03-01-2021', '00:00', 1),
            (8, 'Debito', 60, 999, '03-01-2021', '00:00', 27000),
            (9, 'Extraccion', 0, 60, '03-01-2021', '00:00', 7),
            (10, 'Extraccion', 65, 999, '03-01-2021', '00:00', 500),
            (11, 'Extraccion', 999, 60, '03-01-2021', '00:00', 32),
            (12, 'Extraccion', 5, 60, '03-01-2021', '00:00', 1000),
            (13, 'Extraccion', 999, 65, '03-01-2021', '00:00', 10000),
            (14, 'Extraccion', 999, 65, '03-01-2021', '00:00', 675)
        ]

        df = pd.DataFrame(df_data,
                          columns=['nro_de_transacción', 'tipo_de_transacción',
                                   'cuenta_origen', 'cuenta_destino',
                                   'fecha', 'hora', 'monto'])

        top5 = top5_cuentas_mas_transacciones_para_trans_mayor(df)
        self.assertEqual(set(top5[:2]), {65, 999})
        self.assertEqual(set(top5[2:4]), {5, 60})
        self.assertTrue(top5[4] in {4, 0})
        # Workaround para que RPL no falle por bug desconocido

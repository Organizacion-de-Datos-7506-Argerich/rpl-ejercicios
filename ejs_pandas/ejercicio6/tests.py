import os
import re
import unittest
import pandas as pd

import timeout_decorator

from assignment_main import *

if os.getenv('IS_TRAVIS'):
    from solved import *


class TestMethods(unittest.TestCase):

    @timeout_decorator.timeout(5)
    def test_consigna1(self):
        df_data = [
            ('2020-01-01', 1, 'Robo de alfajores al fan de wanda', 1, 'Robo', 1.0, 1.0),
            ('2020-01-01', 2, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-02-01', 3, 'Robo de alfajores al fan de wanda', 3, 'Robo', 1.0, 1.0),
            ('2020-02-01', 4, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-03-01', 5, 'Robo de alfajores al fan de wanda', 3, 'Robo', 1.0, 1.0),
            ('2020-03-01', 6, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-04-01', 7, 'Robo de alfajores al fan de wanda', 1, 'Robo', 1.0, 1.0),
            ('2020-04-01', 8, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-05-01', 9, 'Robo de alfajores al fan de wanda', 3, 'Robo', 1.0, 1.0),
            ('2020-05-01', 10, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-06-01', 11, 'Robo de alfajores al fan de wanda', 3, 'Robo', 1.0, 1.0),
            ('2020-06-01', 12, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-07-01', 13, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),  # participa
            ('2020-07-01', 14, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-08-01', 15, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-08-01', 16, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),  # participa
            ('2020-09-01', 17, 'Robo de alfajores al fan de wanda', 1, 'Robo', 1.0, 1.0),
            ('2020-09-01', 18, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-10-01', 19, 'Robo de alfajores al fan de wanda', 3, 'Robo', 1.0, 1.0),
            ('2020-10-01', 20, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),  # participa
            ('2020-11-01', 21, 'Robo de alfajores al fan de wanda', 3, 'Robo', 1.0, 1.0),
            ('2020-11-01', 22, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),  # participa
            ('2020-12-01', 23, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),  # participa
            ('2020-12-01', 24, 'Robo de alfajores al fan de wanda', 3, 'Robo', 1.0, 1.0),  # participa
        ]

        casos = pd.DataFrame(df_data,
                             columns=['fecha', 'id_caso', 'descripcion',
                                      'estado_caso', 'categoria', 'latitud',
                                      'longitud'])

        df_data = [
            (13, 1),
            (14, 0),
            (15, 0),
            (16, 1),
            (17, 0),
            (18, 0),
            (19, 0),
            (20, 1),
            (21, 0),
            (22, 1),
            (23, 1),
            (24, 1),
        ]

        batiseniales = pd.DataFrame(df_data,
                                    columns=['id_caso', 'respuesta'])

        self.assertEqual(consigna1(casos, batiseniales), 0.5)

    @timeout_decorator.timeout(5)
    def test_consigna2(self):
        df_data = [
            ('2020-01-01', 1, 'Robo de alfajores al fan de wanda', 1, 'Robo', 1.0, 1.0),
            ('2020-01-01', 2, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-02-01', 3, 'Robo de alfajores al fan de wanda', 3, 'Robo', 1.0, 1.0),
            ('2020-02-01', 4, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-03-01', 5, 'Robo de alfajores al fan de wanda', 3, 'Robo', 1.0, 1.0),
            ('2020-03-01', 6, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-04-01', 7, 'Robo de alfajores al fan de wanda', 1, 'Robo', 1.0, 1.0),
            ('2020-04-01', 8, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-05-01', 9, 'Robo de alfajores al fan de wanda', 3, 'Robo', 1.0, 1.0),
            ('2020-05-01', 10, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-06-01', 11, 'Robo de alfajores al fan de wanda', 3, 'Robo', 1.0, 1.0),
            ('2020-06-01', 12, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-07-01', 13, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),  # participa
            ('2020-07-01', 14, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-08-01', 15, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-08-01', 16, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),  # participa
            ('2020-09-01', 17, 'Robo de alfajores al fan de wanda', 1, 'Robo', 1.0, 1.0),
            ('2020-09-01', 18, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-10-01', 19, 'Robo de alfajores al fan de wanda', 3, 'Robo', 1.0, 1.0),
            ('2020-10-01', 20, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),  # participa
            ('2020-11-01', 21, 'Robo de alfajores al fan de wanda', 3, 'Robo', 1.0, 1.0),
            ('2020-11-01', 22, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),  # participa
            ('2020-12-01', 23, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),  # participa
            ('2020-12-01', 24, 'Robo de alfajores al fan de wanda', 3, 'Robo', 1.0, 1.0),  # participa
        ]

        casos = pd.DataFrame(df_data,
                             columns=['fecha', 'id_caso', 'descripcion',
                                      'estado_caso', 'categoria', 'latitud',
                                      'longitud'])

        df_data = [
            (13, 1),
            (14, 0),
            (15, 0),
            (16, 1),
            (17, 0),
            (18, 0),
            (19, 0),
            (20, 1),
            (21, 0),
            (22, 1),
            (23, 1),
            (24, 1),
        ]

        batiseniales = pd.DataFrame(df_data,
                                    columns=['id_caso', 'respuesta'])

        self.assertEqual(consigna2(casos, batiseniales), 5/6)

    @timeout_decorator.timeout(5)
    def test_consigna3(self):
        df_data = [
            ('2020-01-01', 1, 'Robo de alfajores al fan de wanda', 1, 'Robo', 1.0, 1.0),
            ('2020-01-01', 2, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-02-01', 3, 'Robo de alfajores al fan de wanda', 3, 'Robo', 1.0, 1.0),
            ('2020-02-01', 4, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-03-01', 5, 'Robo de alfajores al fan de wanda', 3, 'Robo', 1.0, 1.0),
            ('2020-03-01', 6, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-04-01', 7, 'Robo de alfajores al fan de wanda', 1, 'Robo', 1.0, 1.0),
            ('2020-04-01', 8, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-05-01', 9, 'Robo de alfajores al fan de wanda', 3, 'Robo', 1.0, 1.0),
            ('2020-05-01', 10, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-06-01', 11, 'Robo de alfajores al fan de wanda', 3, 'Robo', 1.0, 1.0),
            ('2020-06-01', 12, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-07-01', 13, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),  # participa
            ('2020-07-01', 14, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-08-01', 15, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-08-01', 16, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),  # participa
            ('2020-09-01', 17, 'Robo de alfajores al fan de wanda', 1, 'Robo', 1.0, 1.0),
            ('2020-09-01', 18, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),
            ('2020-10-01', 19, 'Robo de alfajores al fan de wanda', 3, 'Robo', 1.0, 1.0),
            ('2020-10-01', 20, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),  # participa
            ('2020-11-01', 21, 'Robo de alfajores al fan de wanda', 3, 'Robo', 1.0, 1.0),
            ('2020-11-01', 22, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),  # participa
            ('2020-12-01', 23, 'Robo de alfajores al fan de wanda', 2, 'Robo', 1.0, 1.0),  # participa
            ('2020-12-01', 24, 'Robo de alfajores al fan de wanda', 3, 'Robo', 1.0, 1.0),  # participa
        ]

        casos = pd.DataFrame(df_data,
                             columns=['fecha', 'id_caso', 'descripcion',
                                      'estado_caso', 'categoria', 'latitud',
                                      'longitud'])

        df_data = [
            (13, 1),
            (14, 0),
            (15, 0),
            (16, 1),
            (17, 0),
            (18, 0),
            (19, 0),
            (20, 1),
            (21, 0),
            (22, 1),
            (23, 1),
            (24, 1),
        ]

        batiseniales = pd.DataFrame(df_data,
                                    columns=['id_caso', 'respuesta'])

        self.assertEqual(consigna3(casos, batiseniales), '12')
        # Workaround para bug de RPL

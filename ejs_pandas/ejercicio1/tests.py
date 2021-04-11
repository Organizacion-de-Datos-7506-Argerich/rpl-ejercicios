import os
import unittest
import pandas as pd

import timeout_decorator

from .assignment_main import *

if os.getenv('IS_TRAVIS'):
    from .solved import *


class TestMethods(unittest.TestCase):

    @timeout_decorator.timeout(5)
    def test_promedio_general_simple(self):
        notas_data = [
            (1, 'Datos', 4, '03-01-2021'),
            (2, 'Datos', 6, '03-01-2021'),
            (3, 'Datos', 9, '03-01-2021'),
            (4, 'Datos', 2, '03-01-2021')
        ]

        notas_df = pd.DataFrame(notas_data,
                                columns=['padron', 'materia',
                                         'nota', 'fecha'])

        self.assertEqual(promedio_general(notas_df), 5.25)

    @timeout_decorator.timeout(5)
    def test_nota_max_min_2019_simple(self):
        notas_data = [
            (1, 'Datos', 4, '03-01-2019'),
            (2, 'Datos', 6, '03-01-2019'),
            (3, 'Datos', 9, '03-01-2021'),
            (4, 'Datos', 3, '03-01-2019'),
            (5, 'Datos', 4, '03-01-2019'),
            (6, 'Datos', 5, '03-01-2019'),
            (7, 'Datos', 3, '03-01-2019'),
            (8, 'Datos', 8, '03-01-2019'),
            (9, 'Datos', 2, '03-01-2020')
        ]

        notas_df = pd.DataFrame(notas_data,
                                columns=['padron', 'materia',
                                         'nota', 'fecha'])

        self.assertEqual(nota_max_min_2019(notas_df), (8, 3))

    @timeout_decorator.timeout(5)
    def test_padron_mayor_aprobadas_ult_cuatri_simple(self):
        notas_data = [
            (1, 'Datos', 4, '03-01-2019'),
            (2, 'Datos', 6, '03-01-2019'),
            (3, 'Datos', 9, '03-01-2021'),
            (4, 'Datos', 3, '03-01-2019'),
            (5, 'Datos', 4, '03-01-2019'),
            (6, 'Datos', 5, '03-01-2019'),
            (7, 'Datos', 3, '03-01-2019'),
            (8, 'Datos', 8, '03-01-2019'),
            (9, 'Datos', 2, '03-01-2020'),
            (10, 'Estructura', 5, '04-07-2021'),
            (10, 'Datos', 7, '04-07-2021'),
            (10, 'ANMIII', 3, '04-07-2021'),
            (10, 'Algebra II', 1, '04-07-2021'),
            (11, 'Estructura', 4, '04-07-2021'),
            (11, 'Datos', 7, '04-07-2021'),
            (11, 'ANMIII', 7, '04-07-2021')
        ]

        notas_df = pd.DataFrame(notas_data,
                                columns=['padron', 'materia',
                                         'nota', 'fecha'])

        self.assertEqual(padron_mayor_aprobadas_ult_cuatri(notas_df), 11)

    @timeout_decorator.timeout(5)
    def test_nota_promedio_por_materia_simple(self):
        notas_data = [
            (1, 'Datos', 4, '03-01-2019'),
            (2, 'Datos', 6, '03-01-2019'),
            (3, 'Datos', 9, '03-01-2021'),
            (4, 'Datos', 3, '03-01-2019'),
            (5, 'Datos', 4, '03-01-2019'),
            (6, 'Datos', 5, '03-01-2019'),
            (7, 'Datos', 3, '03-01-2019'),
            (8, 'Datos', 8, '03-01-2019'),
            (9, 'Datos', 2, '03-01-2020'),
            (10, 'Estructura', 5, '04-07-2021'),
            (10, 'Datos', 7, '04-07-2021'),
            (10, 'ANMIII', 3, '04-07-2021'),
            (10, 'Algebra II', 1, '04-07-2021'),
            (11, 'Estructura', 4, '04-07-2021'),
            (11, 'Datos', 7, '04-07-2021'),
            (11, 'ANMIII', 7, '04-07-2021')
        ]

        notas_df = pd.DataFrame(notas_data,
                                columns=['padron', 'materia',
                                         'nota', 'fecha'])

        self.assertEqual(nota_promedio_por_materia(notas_df),
                         notas_df.groupby('materia').agg({'nota': 'mean'}).to_dict())

    @timeout_decorator.timeout(5)
    def test_nota_promedio_por_padron_simple(self):
        notas_data = [
            (1, 'Datos', 4, '03-01-2019'),
            (2, 'Datos', 6, '03-01-2019'),
            (3, 'Datos', 9, '03-01-2021'),
            (4, 'Datos', 3, '03-01-2019'),
            (5, 'Datos', 4, '03-01-2019'),
            (6, 'Datos', 5, '03-01-2019'),
            (7, 'Datos', 3, '03-01-2019'),
            (8, 'Datos', 8, '03-01-2019'),
            (9, 'Datos', 2, '03-01-2020'),
            (10, 'Estructura', 5, '04-07-2021'),
            (10, 'Datos', 7, '04-07-2021'),
            (10, 'ANMIII', 3, '04-07-2021'),
            (10, 'Algebra II', 1, '04-07-2021'),
            (11, 'Estructura', 4, '04-07-2021'),
            (11, 'Datos', 7, '04-07-2021'),
            (11, 'ANMIII', 7, '04-07-2021')
        ]

        notas_df = pd.DataFrame(notas_data,
                                columns=['padron', 'materia',
                                         'nota', 'fecha'])

        self.assertEqual(nota_promedio_por_padron(notas_df),
                         notas_df.groupby('padron').agg({'nota': 'mean'}).to_dict())

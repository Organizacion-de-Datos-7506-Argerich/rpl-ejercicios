import os
import re
import unittest
import pandas as pd

import timeout_decorator

from assignment_main import *

if os.getenv('IS_TRAVIS'):
    from solved import *


class TestMethods(unittest.TestCase):

    @staticmethod
    def normalize_df_for_tests(df, orderer_column=None):
        def remove_accents(raw_text):
            if not isinstance(raw_text, str):
                return raw_text
            raw_text = re.sub(u"[àáâãäå]", 'a', raw_text)
            raw_text = re.sub(u"[èéêë]", 'e', raw_text)
            raw_text = re.sub(u"[ìíîï]", 'i', raw_text)
            raw_text = re.sub(u"[òóôõö]", 'o', raw_text)
            raw_text = re.sub(u"[ùúûü]", 'u', raw_text)
            raw_text = re.sub(u"[ýÿ]", 'y', raw_text)
            raw_text = re.sub(u"[ß]", 'ss', raw_text)
            raw_text = re.sub(u"[ñ]", 'n', raw_text)
            return raw_text

        df.columns = [remove_accents(c) for c in df.columns]
        if orderer_column:
            df = df.sort_values(orderer_column)
        return df.sort_index(axis=1)

    @timeout_decorator.timeout(5)
    def test_consignaA(self):
        data = [
            (1, 1, 4, 8),
            (2, 1, 6, 0),
            (2, 1, 6, 10),
            (3, 4, 9, 6),
            (3, 4, 4, 2),
            (4, 3, 2, 8)
        ]

        df = pd.DataFrame(data,
                          columns=['codigo_producto', 'codigo_fabricante',
                                   'mes', 'ventas_mensuales'])

        result_df = pd.DataFrame([(1, 8), (2, 5), (3, 4), (4, 8)],
                                 columns=['codigo_producto', 'promedio_ventas'])

        student_df = consignaA(df)

        result_df = self.normalize_df_for_tests(result_df, 'codigo_producto')
        student_df = self.normalize_df_for_tests(student_df, 'codigo_producto')

        self.assertTrue(result_df.equals(student_df))

    @timeout_decorator.timeout(5)
    def test_consignaB(self):
        data = [
            (1, 1, 4, 8),
            (2, 1, 6, 0),
            (2, 1, 6, 10),
            (3, 4, 9, 6),
            (3, 4, 4, 2),
            (4, 3, 2, 8)
        ]

        df = pd.DataFrame(data,
                          columns=['codigo_producto', 'codigo_fabricante',
                                   'mes', 'ventas_mensuales'])

        result_df = pd.DataFrame([(1, 8, 8, 8),
                                  (2, 0, 10, 5),
                                  (3, 2, 6, 4),
                                  (4, 8, 8, 8)],
                                 columns=['codigo_producto', 'minimo_ventas_mensual',
                                          'maximo_ventas_mensual', 'promedio_ventas_mensual'])

        student_df = consignaB(df)

        result_df = self.normalize_df_for_tests(result_df, 'codigo_producto')
        student_df = self.normalize_df_for_tests(student_df, 'codigo_producto')

        self.assertTrue(result_df.equals(student_df))

    @timeout_decorator.timeout(5)
    def test_consignaC(self):
        data = [
            (1, 1, 4, 8),
            (2, 1, 6, 0),
            (2, 1, 6, 10),
            (3, 4, 9, 6),
            (3, 4, 4, 2),
            (4, 3, 2, 8)
        ]

        df = pd.DataFrame(data,
                          columns=['codigo_producto', 'codigo_fabricante',
                                   'mes', 'ventas_mensuales'])

        result_df = pd.DataFrame([(1, 'minimo_ventas_mensual', 8),
                                  (1, 'maximo_ventas_mensual', 8),
                                  (1, 'promedio_ventas_mensual', 8),
                                  (2, 'minimo_ventas_mensual', 0),
                                  (2, 'maximo_ventas_mensual', 10),
                                  (2, 'promedio_ventas_mensual', 5),
                                  (3, 'minimo_ventas_mensual', 2),
                                  (3, 'maximo_ventas_mensual', 6),
                                  (3, 'promedio_ventas_mensual', 4),
                                  (4, 'minimo_ventas_mensual', 8),
                                  (4, 'maximo_ventas_mensual', 8),
                                  (4, 'promedio_ventas_mensual', 8)],
                                 columns=['codigo_producto', 'agregado', 'valor'])

        student_df = consignaC(df)

        result_df = result_df.set_index(['codigo_producto', 'agregado'])

        result_df = self.normalize_df_for_tests(result_df, ['codigo_producto', 'agregado'])
        student_df = self.normalize_df_for_tests(student_df, ['codigo_producto', 'agregado'])

        self.assertTrue(result_df.equals(student_df))

    @timeout_decorator.timeout(5)
    def test_consignaD(self):
        data = [
            (1, 1, 4, 8),
            (2, 1, 6, 0),
            (2, 1, 6, 10),
            (3, 4, 9, 6),
            (3, 4, 4, 2),
            (4, 3, 2, 8)
        ]

        df = pd.DataFrame(data,
                          columns=['codigo_producto', 'codigo_fabricante',
                                   'mes', 'ventas_mensuales'])

        result_df = pd.DataFrame([(1, 8, 8, 8),
                                  (2, 0, 10, 5),
                                  (3, 2, 6, 4),
                                  (4, 8, 8, 8)],
                                 columns=['codigo_producto', 'minimo_ventas_mensual',
                                          'maximo_ventas_mensual', 'promedio_ventas_mensual']). \
            pivot_table(columns='codigo_producto')

        student_df = consignaD(df)

        result_df = self.normalize_df_for_tests(result_df)
        student_df = self.normalize_df_for_tests(student_df)

        self.assertTrue(result_df.equals(student_df))

    @timeout_decorator.timeout(5)
    def test_consignaE(self):
        data = [
            (1, 1, 4, 8),
            (2, 1, 6, 0),
            (2, 1, 6, 10),
            (3, 4, 9, 6),
            (3, 4, 4, 2),
            (4, 3, 2, 8)
        ]

        df = pd.DataFrame(data,
                          columns=['codigo_producto', 'codigo_fabricante',
                                   'mes', 'ventas_mensuales'])

        result_df = pd.DataFrame([(1, True, False, False),
                                  (2, True, False, False),
                                  (3, False, False, True),
                                  (4, False, True, False)],
                                 columns=['codigo_producto', 1, 3, 4]). \
            set_index('codigo_producto')

        student_df = consignaE(df)

        result_df = self.normalize_df_for_tests(result_df)
        student_df = self.normalize_df_for_tests(student_df)

        self.assertTrue(result_df.equals(student_df))

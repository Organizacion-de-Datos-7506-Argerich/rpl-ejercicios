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
    def test_consigna1(self):
        df_data = [
            (4, 10, 2017, 10, 1, 1, 1),
            (8, 10, 2017, 10, 1, 1, 1),
            (15, 10, 2017, 10, 1, 1, 1),
            (21, 10, 2017, 10, 1, 1, 2),
            (27, 10, 2017, 10, 1, 1, 2),

            (3, 10, 2017, 10, 1, 2, 2),
            (5, 10, 2017, 10, 1, 2, 2),
            (9, 10, 2017, 10, 1, 2, 1),
            (19, 10, 2017, 10, 1, 2, 1),
            (19, 10, 2017, 10, 1, 2, 1),

            (6, 10, 2017, 10, 1, 3, 2),
            (22, 10, 2017, 10, 1, 3, 2),
            (11, 10, 2017, 10, 1, 3, 1),
            (9, 10, 2017, 10, 1, 3, 1),
            (14, 10, 2017, 10, 1, 3, 2),

            (6, 10, 2016, 10, 1, 3, 2),
            (22, 10, 2016, 10, 1, 3, 1),
            (11, 10, 2016, 10, 1, 3, 1),
            (9, 10, 2016, 10, 1, 3, 1),
            (14, 10, 2016, 10, 1, 3, 2),

            (3, 10, 2016, 10, 1, 2, 2),
            (5, 10, 2016, 10, 1, 2, 1),

            (4, 10, 2016, 10, 1, 1, 2)
        ]

        nacimientos = pd.DataFrame(df_data,
                              columns=['dia_nacimiento', 'mes_nacimiento', 'anio_nacimiento',
                                       'peso_al_nacer', 'longitud_al_nacer', 'id_hospital',
                                       'tipo_parto'])

        df_data = [
            (1, "Av Paseo Colon 700", 5.3),
            (2, "Av Paseo Colon 700", 3.3),
            (3, "Av Paseo Colon 700", 3.1),
            (4, "Av Paseo Colon 700", 3.2),
            (5, "Av Paseo Colon 700", 20.1),
        ]

        hospitales = pd.DataFrame(df_data,
                                 columns=['id_hospital', 'direccion',
                                          'promedio_nacimientos_mensual'])

        self.assertEqual(consigna1(nacimientos, hospitales), {2,3})

    @timeout_decorator.timeout(5)
    def test_consigna2(self):
        df_data = [
            (4, 10, 2017, 10, 1, 1, 1),
            (8, 10, 2017, 10, 1, 1, 1),
            (15, 10, 2017, 10, 1, 1, 1),
            (21, 10, 2017, 10, 1, 1, 2),
            (27, 10, 2017, 10, 1, 1, 2),

            (3, 10, 2017, 10, 1, 2, 2),
            (5, 10, 2017, 10, 1, 2, 2),
            (9, 10, 2017, 10, 1, 2, 1),
            (19, 10, 2017, 10, 1, 2, 1),
            (19, 10, 2017, 10, 1, 2, 1),

            (6, 10, 2017, 10, 1, 3, 2),
            (22, 10, 2017, 10, 1, 3, 2),
            (11, 10, 2017, 10, 1, 3, 1),
            (9, 10, 2017, 10, 1, 3, 1),
            (14, 10, 2017, 10, 1, 3, 2),

            (6, 10, 2016, 10, 1, 3, 2),
            (22, 10, 2016, 10, 1, 3, 1),
            (11, 10, 2016, 10, 1, 3, 1),
            (9, 10, 2016, 10, 1, 3, 1),
            (14, 10, 2016, 10, 1, 3, 2),

            (3, 10, 2016, 10, 1, 2, 2),
            (5, 10, 2016, 10, 1, 2, 1),

            (4, 10, 2016, 10, 1, 1, 2)
        ]

        nacimientos = pd.DataFrame(df_data,
                              columns=['dia_nacimiento', 'mes_nacimiento', 'anio_nacimiento',
                                       'peso_al_nacer', 'longitud_al_nacer', 'id_hospital',
                                       'tipo_parto'])

        df_data = [
            (1, "Av Paseo Colon 700", 5.3),
            (2, "Av Paseo Colon 700", 3.3),
            (3, "Av Paseo Colon 700", 3.1),
            (4, "Av Paseo Colon 700", 3.2),
            (5, "Av Paseo Colon 700", 20.1),
        ]

        hospitales = pd.DataFrame(df_data,
                                 columns=['id_hospital', 'direccion',
                                          'promedio_nacimientos_mensual'])

        student_df = consigna2(nacimientos, hospitales)

        result_df = pd.DataFrame([(1, False),
                                  (2, False),
                                  (3, True)],
                                 columns=['id_hospital', 'se_incremento'])

        result_df = self.normalize_df_for_tests(result_df, 'id_hospital')
        student_df = self.normalize_df_for_tests(student_df, 'id_hospital')

        student_df.index = result_df.index

        self.assertTrue(result_df.equals(student_df))
        # Workaround para que RPL no falle por bug desconocido

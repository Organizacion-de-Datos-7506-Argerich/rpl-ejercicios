import os
import re
import unittest
from datetime import datetime
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
            (1, 1, 1, datetime.now().isoformat()),
            (1, 1, 2, datetime.now().isoformat()),
            (1, 1, 3, datetime.now().isoformat()),
            (1, 1, 2, datetime.now().isoformat()),
            (1, 1, 1, datetime.now().isoformat()),
            (1, 2, 3, datetime.now().isoformat()),
            (1, 2, 3, datetime.now().isoformat()),
            (1, 2, 3, datetime.now().isoformat()),
            (1, 3, 5, datetime.now().isoformat()),
            (1, 3, 0, datetime.now().isoformat()),
            (1, 4, 4, datetime.now().isoformat()),
            (1, 5, 5, datetime.now().isoformat()),
            (1, 7, 1, datetime.now().isoformat())
        ]

        ebooks = pd.DataFrame(df_data,
                              columns=['user_id', 'book_id',
                                       'rating', 'timestamp'])

        df_data = [
            (1, "El principito", 1.0),
            (2, "Sinceramente", 3.3),
            (3, "Primer Tiempo", 3.1),
            (4, "Meal Prep", 3.2),
            (6, "El Aleph", 5.0),
        ]

        goodreads = pd.DataFrame(df_data,
                                 columns=['book_id', 'book_name',
                                          'avg_rating'])

        self.assertEqual(consigna1(ebooks, goodreads), [5, 4, 2, 3, 1])

    @timeout_decorator.timeout(5)
    def test_consigna2(self):
        df_data = [
            (1, 1, 1, datetime.now().isoformat()),
            (1, 1, 2, datetime.now().isoformat()),
            (1, 1, 3, datetime.now().isoformat()),
            (1, 1, 2, datetime.now().isoformat()),
            (1, 1, 1, datetime.now().isoformat()),
            (1, 2, 3, datetime.now().isoformat()),
            (1, 2, 3, datetime.now().isoformat()),
            (1, 2, 3, datetime.now().isoformat()),
            (1, 3, 5, datetime.now().isoformat()),
            (1, 3, 0, datetime.now().isoformat()),
            (1, 4, 4, datetime.now().isoformat()),
            (1, 5, 5, datetime.now().isoformat()),
            (1, 7, 1, datetime.now().isoformat())
        ]

        ebooks = pd.DataFrame(df_data,
                              columns=['user_id', 'book_id',
                                       'rating', 'timestamp'])

        df_data = [
            (1, "El principito", 1.0),
            (2, "Sinceramente", 3.3),
            (3, "Primer Tiempo", 3.1),
            (4, "Meal Prep", 3.2),
            (6, "El Aleph", 5.0),
        ]

        goodreads = pd.DataFrame(df_data,
                                 columns=['book_id', 'book_name',
                                          'avg_rating'])

        student_df = consigna2(ebooks, goodreads)

        result_df = pd.DataFrame([(1, "El principito"),
                                  (3, "Primer Tiempo")],
                                 columns=['book_id', 'book_name'])

        result_df = self.normalize_df_for_tests(result_df, 'book_id')
        student_df = self.normalize_df_for_tests(student_df, 'book_id')

        student_df.index = result_df.index

        self.assertTrue(result_df.equals(student_df))

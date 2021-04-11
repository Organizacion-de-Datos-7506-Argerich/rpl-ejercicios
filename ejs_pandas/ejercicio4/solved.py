from typing import List
import pandas as pd

"""
Se reciben dos dataframes.

El primero del sitio de EBooks:
* user_id (int)
* book_id (int)
* rating (int)
* timestamp (string en formato ISO 8601)

El segundo de GoodReads:
* book_id (int)
* book_name (string)
* avg_rating (float)
"""


def consigna1(ebooks, goodreads) -> List[int]:
    """
    Obtener el TOP5 de Ebooks en el sitio de Ebooks por promedio de rating.

    :param ebooks: dataframe de ebooks
    :param goodreads: dataframe de Goodreads
    :return: una lista ordenada con el top 5 pedido
    """
    return ebooks.groupby('book_id'). \
               agg({'rating': 'mean'}).reset_index(). \
               sort_values('rating', ascending=False).book_id.tolist()[:5]


def consigna2(ebooks, goodreads) -> pd.DataFrame:
    """
    Obtener un dataframe de los libros tienen una diferencia de rating promedio mayor al 20% entre el sitio de Ebooks y
    GoodReads (respecto del sitio de ebooks)

    :param ebooks: dataframe de ebooks
    :param goodreads: dataframe de Goodreads
    :return: dataframe con columnas (book_id, book_name)
    """
    ebooks_mean = ebooks.groupby('book_id'). \
        agg({'rating': 'mean'}).reset_index()
    joined = pd.merge(ebooks_mean, goodreads, on='book_id', how='inner')
    joined['rate_difference'] = joined['rating'] - joined['avg_rating']
    joined['rate_difference'] = joined['rate_difference'].map(lambda x: abs(x))
    joined['rate_difference'] = joined['rate_difference'] / joined['rating']
    joined = joined[joined.rate_difference > 0.2]
    return joined[['book_id', 'book_name']]

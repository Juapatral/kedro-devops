<<<<<<< HEAD
"""My transform uppercase."""

import pandas as pd


def transform_uppercase(dataframe: pd.DataFrame) -> pd.DataFrame:
    """My transform function
    Args:
        dataframe (pd.DataFrame): dataframe to transform

    Returns:
        pd.DataFrame: transformed dataframe
    """
    return dataframe.applymap(lambda column: column.upper())
=======
import pandas as pd
from requests import Response


def transform_uppercase(data_set: Response) -> pd.DataFrame:
    """
    Transform a lowercase dataframe to uppercase.

    Args:
        data (pd.DataFrame): A raw dataframe

    Returns:
        pd.DataFrame: An uppercase dataframe
    """
    json_data = data_set.json()
    pokemons = json_data.get("results")
    data = pd.json_normalize(pokemons)
    return data.applymap(lambda x: x.upper())
>>>>>>> upstream/main

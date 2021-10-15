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

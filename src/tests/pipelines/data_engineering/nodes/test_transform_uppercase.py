"""My test transform uppercase."""

import pandas as pd

from kedro_devops.pipelines.data_engineering.nodes.transform_uppercase import (
    transform_uppercase,
)


class TestTransformUppercase:
    """My test class."""

    # first test
    def test_transform_string(self):
        """My first test.
        Testing
        """
        t_dataframe = pd.DataFrame({"names": ["juan", "manuel", "alberto"]})
        output = pd.DataFrame({"names": ["JUAN", "MANUEL", "ALBERTO"]})
        assert output.equals(transform_uppercase(t_dataframe))

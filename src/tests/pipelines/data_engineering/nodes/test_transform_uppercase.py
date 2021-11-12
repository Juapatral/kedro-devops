<<<<<<< HEAD
"""My test transform uppercase."""

import pandas as pd
=======
import pandas as pd
from requests.models import Response
from pytest import MonkeyPatch
>>>>>>> upstream/main

from kedro_devops.pipelines.data_engineering.nodes.transform_uppercase import (
    transform_uppercase,
)


class TestTransformUppercase:
<<<<<<< HEAD
    """My test class."""

    # first test
    def test_transform_string(self):
        """My first test.
        Testing
        """
        t_dataframe = pd.DataFrame({"names": ["juan", "manuel", "alberto"]})
        output = pd.DataFrame({"names": ["JUAN", "MANUEL", "ALBERTO"]})
        assert output.equals(transform_uppercase(t_dataframe))
=======
    def test_transform_string(self, monkeypatch: MonkeyPatch):
        """
        should return a upper case string for a string dataframe
        """

        def mock_json():
            return {
                "results": [{"data": "test1"}, {"data": "test2"}, {"data": "test3"}]
            }

        t_dataframe = Response()
        monkeypatch.setattr(t_dataframe, "json", mock_json)

        output = transform_uppercase(t_dataframe)

        assert output.equals(pd.DataFrame({"data": ["TEST1", "TEST2", "TEST3"]}))
>>>>>>> upstream/main

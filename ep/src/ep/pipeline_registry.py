"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline, node


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    return {"__default__": Pipeline([
            node(lambda x: x.describe(), inputs='pandas_iris_data', outputs=None),
        ])}

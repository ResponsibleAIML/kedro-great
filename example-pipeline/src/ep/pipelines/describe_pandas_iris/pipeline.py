"""
This is a boilerplate pipeline 'describe_pandas_iris'
generated using Kedro 0.18.11
"""

from kedro.pipeline import Pipeline, node, pipeline


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([node(lambda x: x.describe(), inputs='pandas_iris_data', outputs=None),
                     node(lambda x: x.show(), inputs='spark_iris_data', outputs=None),])

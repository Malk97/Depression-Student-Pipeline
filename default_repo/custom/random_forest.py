import pandas as pd
import numpy as np


if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from default_repo.model.Training import randomforestmodel

@custom
def transform_custom(data,*args, **kwargs):
    best_model = randomforestmodel(data)
    return best_model




@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

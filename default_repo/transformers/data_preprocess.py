if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from default_repo.data_preprocess.convert_type import convert_ty
from default_repo.data_preprocess.rename_column import rename
from default_repo.data_preprocess.handell_null import fill_value1
from default_repo.data_preprocess.encoder import encoder_ver

@transformer
def transform(data, *args, **kwargs):
    convert_dataType=convert_ty(data) 
    rename_columnData=rename(convert_dataType)
    fill_null_value=fill_value1(rename_columnData)
    Encoding_data=encoder_ver(fill_null_value)
     

    return Encoding_data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

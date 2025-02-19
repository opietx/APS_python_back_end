from core_tools.data.SQL.connect import set_up_local_storage
set_up_local_storage('list of params goes here') 

from core_tools.data.ds.data_set import load_by_uuid
ds = load_by_uuid(17389_43288_456266815)

# https://gitlab.tudelft.nl/sdesnoo/core_tools/-/tree/v1.5.6/core_tools/data?ref_type=tags

# DescribePvcCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.describe_pvc_command import DescribePvcCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DescribePvcCommand from a JSON string
describe_pvc_command_instance = DescribePvcCommand.from_json(json)
# print the JSON string representation of the object
print(DescribePvcCommand.to_json())

# convert the object into a dict
describe_pvc_command_dict = describe_pvc_command_instance.to_dict()
# create an instance of DescribePvcCommand from a dict
describe_pvc_command_from_dict = DescribePvcCommand.from_dict(describe_pvc_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



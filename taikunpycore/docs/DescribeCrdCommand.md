# DescribeCrdCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.describe_crd_command import DescribeCrdCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeCrdCommand from a JSON string
describe_crd_command_instance = DescribeCrdCommand.from_json(json)
# print the JSON string representation of the object
print(DescribeCrdCommand.to_json())

# convert the object into a dict
describe_crd_command_dict = describe_crd_command_instance.to_dict()
# create an instance of DescribeCrdCommand from a dict
describe_crd_command_from_dict = DescribeCrdCommand.from_dict(describe_crd_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



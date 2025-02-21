# DescribeConfigMapCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.describe_config_map_command import DescribeConfigMapCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeConfigMapCommand from a JSON string
describe_config_map_command_instance = DescribeConfigMapCommand.from_json(json)
# print the JSON string representation of the object
print(DescribeConfigMapCommand.to_json())

# convert the object into a dict
describe_config_map_command_dict = describe_config_map_command_instance.to_dict()
# create an instance of DescribeConfigMapCommand from a dict
describe_config_map_command_from_dict = DescribeConfigMapCommand.from_dict(describe_config_map_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



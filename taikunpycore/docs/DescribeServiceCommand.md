# DescribeServiceCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.describe_service_command import DescribeServiceCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeServiceCommand from a JSON string
describe_service_command_instance = DescribeServiceCommand.from_json(json)
# print the JSON string representation of the object
print(DescribeServiceCommand.to_json())

# convert the object into a dict
describe_service_command_dict = describe_service_command_instance.to_dict()
# create an instance of DescribeServiceCommand from a dict
describe_service_command_from_dict = DescribeServiceCommand.from_dict(describe_service_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



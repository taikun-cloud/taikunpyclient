# DescribeNodeCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.describe_node_command import DescribeNodeCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeNodeCommand from a JSON string
describe_node_command_instance = DescribeNodeCommand.from_json(json)
# print the JSON string representation of the object
print(DescribeNodeCommand.to_json())

# convert the object into a dict
describe_node_command_dict = describe_node_command_instance.to_dict()
# create an instance of DescribeNodeCommand from a dict
describe_node_command_from_dict = DescribeNodeCommand.from_dict(describe_node_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



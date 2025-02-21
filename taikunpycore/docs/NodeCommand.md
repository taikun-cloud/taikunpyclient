# NodeCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.node_command import NodeCommand

# TODO update the JSON string below
json = "{}"
# create an instance of NodeCommand from a JSON string
node_command_instance = NodeCommand.from_json(json)
# print the JSON string representation of the object
print(NodeCommand.to_json())

# convert the object into a dict
node_command_dict = node_command_instance.to_dict()
# create an instance of NodeCommand from a dict
node_command_from_dict = NodeCommand.from_dict(node_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



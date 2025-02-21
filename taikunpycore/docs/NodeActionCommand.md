# NodeActionCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | 
**name** | **str** |  | 
**action** | [**ENodeAction**](ENodeAction.md) |  | 

## Example

```python
from taikunpycore.models.node_action_command import NodeActionCommand

# TODO update the JSON string below
json = "{}"
# create an instance of NodeActionCommand from a JSON string
node_action_command_instance = NodeActionCommand.from_json(json)
# print the JSON string representation of the object
print(NodeActionCommand.to_json())

# convert the object into a dict
node_action_command_dict = node_action_command_instance.to_dict()
# create an instance of NodeActionCommand from a dict
node_action_command_from_dict = NodeActionCommand.from_dict(node_action_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UpdateEdgeNodesCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**edge_nodes** | **List[str]** |  | [optional] 

## Example

```python
from taikunpycore.models.update_edge_nodes_command import UpdateEdgeNodesCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEdgeNodesCommand from a JSON string
update_edge_nodes_command_instance = UpdateEdgeNodesCommand.from_json(json)
# print the JSON string representation of the object
print(UpdateEdgeNodesCommand.to_json())

# convert the object into a dict
update_edge_nodes_command_dict = update_edge_nodes_command_instance.to_dict()
# create an instance of UpdateEdgeNodesCommand from a dict
update_edge_nodes_command_from_dict = UpdateEdgeNodesCommand.from_dict(update_edge_nodes_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# NodesSearchCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_term** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.nodes_search_command import NodesSearchCommand

# TODO update the JSON string below
json = "{}"
# create an instance of NodesSearchCommand from a JSON string
nodes_search_command_instance = NodesSearchCommand.from_json(json)
# print the JSON string representation of the object
print(NodesSearchCommand.to_json())

# convert the object into a dict
nodes_search_command_dict = nodes_search_command_instance.to_dict()
# create an instance of NodesSearchCommand from a dict
nodes_search_command_from_dict = NodesSearchCommand.from_dict(nodes_search_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



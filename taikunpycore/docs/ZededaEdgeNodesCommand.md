# ZededaEdgeNodesCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_url** | **str** |  | [optional] 
**api_token** | **str** |  | [optional] 
**project** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.zededa_edge_nodes_command import ZededaEdgeNodesCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ZededaEdgeNodesCommand from a JSON string
zededa_edge_nodes_command_instance = ZededaEdgeNodesCommand.from_json(json)
# print the JSON string representation of the object
print(ZededaEdgeNodesCommand.to_json())

# convert the object into a dict
zededa_edge_nodes_command_dict = zededa_edge_nodes_command_instance.to_dict()
# create an instance of ZededaEdgeNodesCommand from a dict
zededa_edge_nodes_command_from_dict = ZededaEdgeNodesCommand.from_dict(zededa_edge_nodes_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



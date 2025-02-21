# NodeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_name** | **object** |  | 
**kubelet_ready** | **object** |  | 
**kubelet_sufficient** | **object** |  | 
**kubelet_disk_pressure** | **object** |  | 
**kubelet_memory** | **object** |  | 

## Example

```python
from taikunpycore.models.node_dto import NodeDto

# TODO update the JSON string below
json = "{}"
# create an instance of NodeDto from a JSON string
node_dto_instance = NodeDto.from_json(json)
# print the JSON string representation of the object
print(NodeDto.to_json())

# convert the object into a dict
node_dto_dict = node_dto_instance.to_dict()
# create an instance of NodeDto from a dict
node_dto_from_dict = NodeDto.from_dict(node_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



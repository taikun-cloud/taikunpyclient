# KubernetesNodeListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_name** | **str** |  | 
**type** | **List[str]** |  | 
**status** | **List[str]** |  | 
**reason** | **List[str]** |  | 
**message** | **List[str]** |  | 

## Example

```python
from taikunpycore.models.kubernetes_node_list_dto import KubernetesNodeListDto

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesNodeListDto from a JSON string
kubernetes_node_list_dto_instance = KubernetesNodeListDto.from_json(json)
# print the JSON string representation of the object
print(KubernetesNodeListDto.to_json())

# convert the object into a dict
kubernetes_node_list_dto_dict = kubernetes_node_list_dto_instance.to_dict()
# create an instance of KubernetesNodeListDto from a dict
kubernetes_node_list_dto_from_dict = KubernetesNodeListDto.from_dict(kubernetes_node_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# KubernetesEventCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**source** | **object** |  | [optional] 
**involved_object** | **object** |  | [optional] 
**first_time_stamp** | **datetime** |  | [optional] 
**last_time_stamp** | **datetime** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.kubernetes_event_create_dto import KubernetesEventCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesEventCreateDto from a JSON string
kubernetes_event_create_dto_instance = KubernetesEventCreateDto.from_json(json)
# print the JSON string representation of the object
print(KubernetesEventCreateDto.to_json())

# convert the object into a dict
kubernetes_event_create_dto_dict = kubernetes_event_create_dto_instance.to_dict()
# create an instance of KubernetesEventCreateDto from a dict
kubernetes_event_create_dto_from_dict = KubernetesEventCreateDto.from_dict(kubernetes_event_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



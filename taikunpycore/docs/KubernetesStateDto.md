# KubernetesStateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**reason** | [**EKubernetesState**](EKubernetesState.md) |  | [optional] 

## Example

```python
from taikunpycore.models.kubernetes_state_dto import KubernetesStateDto

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesStateDto from a JSON string
kubernetes_state_dto_instance = KubernetesStateDto.from_json(json)
# print the JSON string representation of the object
print(KubernetesStateDto.to_json())

# convert the object into a dict
kubernetes_state_dto_dict = kubernetes_state_dto_instance.to_dict()
# create an instance of KubernetesStateDto from a dict
kubernetes_state_dto_from_dict = KubernetesStateDto.from_dict(kubernetes_state_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



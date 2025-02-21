# KubernetesVersionListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**is_kubevap_enabled** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.kubernetes_version_list_dto import KubernetesVersionListDto

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesVersionListDto from a JSON string
kubernetes_version_list_dto_instance = KubernetesVersionListDto.from_json(json)
# print the JSON string representation of the object
print(KubernetesVersionListDto.to_json())

# convert the object into a dict
kubernetes_version_list_dto_dict = kubernetes_version_list_dto_instance.to_dict()
# create an instance of KubernetesVersionListDto from a dict
kubernetes_version_list_dto_from_dict = KubernetesVersionListDto.from_dict(kubernetes_version_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



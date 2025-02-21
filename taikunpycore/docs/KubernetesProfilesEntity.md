# KubernetesProfilesEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**taikun_lb_enabled** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.kubernetes_profiles_entity import KubernetesProfilesEntity

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesProfilesEntity from a JSON string
kubernetes_profiles_entity_instance = KubernetesProfilesEntity.from_json(json)
# print the JSON string representation of the object
print(KubernetesProfilesEntity.to_json())

# convert the object into a dict
kubernetes_profiles_entity_dict = kubernetes_profiles_entity_instance.to_dict()
# create an instance of KubernetesProfilesEntity from a dict
kubernetes_profiles_entity_from_dict = KubernetesProfilesEntity.from_dict(kubernetes_profiles_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



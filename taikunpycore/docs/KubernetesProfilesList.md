# KubernetesProfilesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[KubernetesProfilesListDto]**](KubernetesProfilesListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.kubernetes_profiles_list import KubernetesProfilesList

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesProfilesList from a JSON string
kubernetes_profiles_list_instance = KubernetesProfilesList.from_json(json)
# print the JSON string representation of the object
print(KubernetesProfilesList.to_json())

# convert the object into a dict
kubernetes_profiles_list_dict = kubernetes_profiles_list_instance.to_dict()
# create an instance of KubernetesProfilesList from a dict
kubernetes_profiles_list_from_dict = KubernetesProfilesList.from_dict(kubernetes_profiles_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



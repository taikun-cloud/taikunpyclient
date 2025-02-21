# KubernetesProfilesSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CommonSearchResponseData]**](CommonSearchResponseData.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.kubernetes_profiles_search_list import KubernetesProfilesSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesProfilesSearchList from a JSON string
kubernetes_profiles_search_list_instance = KubernetesProfilesSearchList.from_json(json)
# print the JSON string representation of the object
print(KubernetesProfilesSearchList.to_json())

# convert the object into a dict
kubernetes_profiles_search_list_dict = kubernetes_profiles_search_list_instance.to_dict()
# create an instance of KubernetesProfilesSearchList from a dict
kubernetes_profiles_search_list_from_dict = KubernetesProfilesSearchList.from_dict(kubernetes_profiles_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



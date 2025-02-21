# KubernetesProfilesSearchCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_term** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.kubernetes_profiles_search_command import KubernetesProfilesSearchCommand

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesProfilesSearchCommand from a JSON string
kubernetes_profiles_search_command_instance = KubernetesProfilesSearchCommand.from_json(json)
# print the JSON string representation of the object
print(KubernetesProfilesSearchCommand.to_json())

# convert the object into a dict
kubernetes_profiles_search_command_dict = kubernetes_profiles_search_command_instance.to_dict()
# create an instance of KubernetesProfilesSearchCommand from a dict
kubernetes_profiles_search_command_from_dict = KubernetesProfilesSearchCommand.from_dict(kubernetes_profiles_search_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



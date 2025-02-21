# KubernetesProfilesLockManagerCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.kubernetes_profiles_lock_manager_command import KubernetesProfilesLockManagerCommand

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesProfilesLockManagerCommand from a JSON string
kubernetes_profiles_lock_manager_command_instance = KubernetesProfilesLockManagerCommand.from_json(json)
# print the JSON string representation of the object
print(KubernetesProfilesLockManagerCommand.to_json())

# convert the object into a dict
kubernetes_profiles_lock_manager_command_dict = kubernetes_profiles_lock_manager_command_instance.to_dict()
# create an instance of KubernetesProfilesLockManagerCommand from a dict
kubernetes_profiles_lock_manager_command_from_dict = KubernetesProfilesLockManagerCommand.from_dict(kubernetes_profiles_lock_manager_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



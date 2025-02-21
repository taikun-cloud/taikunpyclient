# AccessProfilesLockManagementCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.access_profiles_lock_management_command import AccessProfilesLockManagementCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AccessProfilesLockManagementCommand from a JSON string
access_profiles_lock_management_command_instance = AccessProfilesLockManagementCommand.from_json(json)
# print the JSON string representation of the object
print(AccessProfilesLockManagementCommand.to_json())

# convert the object into a dict
access_profiles_lock_management_command_dict = access_profiles_lock_management_command_instance.to_dict()
# create an instance of AccessProfilesLockManagementCommand from a dict
access_profiles_lock_management_command_from_dict = AccessProfilesLockManagementCommand.from_dict(access_profiles_lock_management_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



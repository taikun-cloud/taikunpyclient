# LockProjectAppCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.lock_project_app_command import LockProjectAppCommand

# TODO update the JSON string below
json = "{}"
# create an instance of LockProjectAppCommand from a JSON string
lock_project_app_command_instance = LockProjectAppCommand.from_json(json)
# print the JSON string representation of the object
print(LockProjectAppCommand.to_json())

# convert the object into a dict
lock_project_app_command_dict = lock_project_app_command_instance.to_dict()
# create an instance of LockProjectAppCommand from a dict
lock_project_app_command_from_dict = LockProjectAppCommand.from_dict(lock_project_app_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



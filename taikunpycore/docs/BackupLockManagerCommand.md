# BackupLockManagerCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.backup_lock_manager_command import BackupLockManagerCommand

# TODO update the JSON string below
json = "{}"
# create an instance of BackupLockManagerCommand from a JSON string
backup_lock_manager_command_instance = BackupLockManagerCommand.from_json(json)
# print the JSON string representation of the object
print(BackupLockManagerCommand.to_json())

# convert the object into a dict
backup_lock_manager_command_dict = backup_lock_manager_command_instance.to_dict()
# create an instance of BackupLockManagerCommand from a dict
backup_lock_manager_command_from_dict = BackupLockManagerCommand.from_dict(backup_lock_manager_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RestoreBackupCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**backup_name** | **str** |  | [optional] 
**restore_name** | **str** |  | [optional] 
**include_namespaces** | **List[str]** |  | [optional] 
**exclude_namespaces** | **List[str]** |  | [optional] 

## Example

```python
from taikunpycore.models.restore_backup_command import RestoreBackupCommand

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreBackupCommand from a JSON string
restore_backup_command_instance = RestoreBackupCommand.from_json(json)
# print the JSON string representation of the object
print(RestoreBackupCommand.to_json())

# convert the object into a dict
restore_backup_command_dict = restore_backup_command_instance.to_dict()
# create an instance of RestoreBackupCommand from a dict
restore_backup_command_from_dict = RestoreBackupCommand.from_dict(restore_backup_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



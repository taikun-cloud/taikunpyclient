# DeleteBackupCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.delete_backup_command import DeleteBackupCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteBackupCommand from a JSON string
delete_backup_command_instance = DeleteBackupCommand.from_json(json)
# print the JSON string representation of the object
print(DeleteBackupCommand.to_json())

# convert the object into a dict
delete_backup_command_dict = delete_backup_command_instance.to_dict()
# create an instance of DeleteBackupCommand from a dict
delete_backup_command_from_dict = DeleteBackupCommand.from_dict(delete_backup_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



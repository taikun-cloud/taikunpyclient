# BackupCredentialsSearchCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_term** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.backup_credentials_search_command import BackupCredentialsSearchCommand

# TODO update the JSON string below
json = "{}"
# create an instance of BackupCredentialsSearchCommand from a JSON string
backup_credentials_search_command_instance = BackupCredentialsSearchCommand.from_json(json)
# print the JSON string representation of the object
print(BackupCredentialsSearchCommand.to_json())

# convert the object into a dict
backup_credentials_search_command_dict = backup_credentials_search_command_instance.to_dict()
# create an instance of BackupCredentialsSearchCommand from a dict
backup_credentials_search_command_from_dict = BackupCredentialsSearchCommand.from_dict(backup_credentials_search_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



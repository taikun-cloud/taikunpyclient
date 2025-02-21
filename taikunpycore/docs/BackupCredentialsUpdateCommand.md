# BackupCredentialsUpdateCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**s3_name** | **str** |  | [optional] 
**s3_access_key_id** | **str** |  | [optional] 
**s3_secret_key** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.backup_credentials_update_command import BackupCredentialsUpdateCommand

# TODO update the JSON string below
json = "{}"
# create an instance of BackupCredentialsUpdateCommand from a JSON string
backup_credentials_update_command_instance = BackupCredentialsUpdateCommand.from_json(json)
# print the JSON string representation of the object
print(BackupCredentialsUpdateCommand.to_json())

# convert the object into a dict
backup_credentials_update_command_dict = backup_credentials_update_command_instance.to_dict()
# create an instance of BackupCredentialsUpdateCommand from a dict
backup_credentials_update_command_from_dict = BackupCredentialsUpdateCommand.from_dict(backup_credentials_update_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



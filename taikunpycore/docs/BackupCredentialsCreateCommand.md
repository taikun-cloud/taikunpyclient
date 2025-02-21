# BackupCredentialsCreateCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s3_name** | **str** |  | [optional] 
**s3_access_key_id** | **str** |  | [optional] 
**s3_secret_key** | **str** |  | [optional] 
**s3_endpoint** | **str** |  | [optional] 
**s3_region** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.backup_credentials_create_command import BackupCredentialsCreateCommand

# TODO update the JSON string below
json = "{}"
# create an instance of BackupCredentialsCreateCommand from a JSON string
backup_credentials_create_command_instance = BackupCredentialsCreateCommand.from_json(json)
# print the JSON string representation of the object
print(BackupCredentialsCreateCommand.to_json())

# convert the object into a dict
backup_credentials_create_command_dict = backup_credentials_create_command_instance.to_dict()
# create an instance of BackupCredentialsCreateCommand from a dict
backup_credentials_create_command_from_dict = BackupCredentialsCreateCommand.from_dict(backup_credentials_create_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



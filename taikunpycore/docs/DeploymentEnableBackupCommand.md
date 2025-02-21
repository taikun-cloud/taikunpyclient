# DeploymentEnableBackupCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**s3_credential_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.deployment_enable_backup_command import DeploymentEnableBackupCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentEnableBackupCommand from a JSON string
deployment_enable_backup_command_instance = DeploymentEnableBackupCommand.from_json(json)
# print the JSON string representation of the object
print(DeploymentEnableBackupCommand.to_json())

# convert the object into a dict
deployment_enable_backup_command_dict = deployment_enable_backup_command_instance.to_dict()
# create an instance of DeploymentEnableBackupCommand from a dict
deployment_enable_backup_command_from_dict = DeploymentEnableBackupCommand.from_dict(deployment_enable_backup_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateBackupPolicyCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**include_namespaces** | **List[str]** |  | [optional] 
**cron_period** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**retention_period** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.create_backup_policy_command import CreateBackupPolicyCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBackupPolicyCommand from a JSON string
create_backup_policy_command_instance = CreateBackupPolicyCommand.from_json(json)
# print the JSON string representation of the object
print(CreateBackupPolicyCommand.to_json())

# convert the object into a dict
create_backup_policy_command_dict = create_backup_policy_command_instance.to_dict()
# create an instance of CreateBackupPolicyCommand from a dict
create_backup_policy_command_from_dict = CreateBackupPolicyCommand.from_dict(create_backup_policy_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



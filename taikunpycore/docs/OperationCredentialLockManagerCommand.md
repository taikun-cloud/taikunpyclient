# OperationCredentialLockManagerCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.operation_credential_lock_manager_command import OperationCredentialLockManagerCommand

# TODO update the JSON string below
json = "{}"
# create an instance of OperationCredentialLockManagerCommand from a JSON string
operation_credential_lock_manager_command_instance = OperationCredentialLockManagerCommand.from_json(json)
# print the JSON string representation of the object
print(OperationCredentialLockManagerCommand.to_json())

# convert the object into a dict
operation_credential_lock_manager_command_dict = operation_credential_lock_manager_command_instance.to_dict()
# create an instance of OperationCredentialLockManagerCommand from a dict
operation_credential_lock_manager_command_from_dict = OperationCredentialLockManagerCommand.from_dict(operation_credential_lock_manager_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



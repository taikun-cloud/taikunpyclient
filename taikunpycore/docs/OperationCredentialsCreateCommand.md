# OperationCredentialsCreateCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**prometheus_username** | **str** |  | [optional] 
**prometheus_password** | **str** |  | [optional] 
**prometheus_url** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.operation_credentials_create_command import OperationCredentialsCreateCommand

# TODO update the JSON string below
json = "{}"
# create an instance of OperationCredentialsCreateCommand from a JSON string
operation_credentials_create_command_instance = OperationCredentialsCreateCommand.from_json(json)
# print the JSON string representation of the object
print(OperationCredentialsCreateCommand.to_json())

# convert the object into a dict
operation_credentials_create_command_dict = operation_credentials_create_command_instance.to_dict()
# create an instance of OperationCredentialsCreateCommand from a dict
operation_credentials_create_command_from_dict = OperationCredentialsCreateCommand.from_dict(operation_credentials_create_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



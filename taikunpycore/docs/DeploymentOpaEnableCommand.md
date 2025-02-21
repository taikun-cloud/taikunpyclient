# DeploymentOpaEnableCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**opa_credential_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.deployment_opa_enable_command import DeploymentOpaEnableCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentOpaEnableCommand from a JSON string
deployment_opa_enable_command_instance = DeploymentOpaEnableCommand.from_json(json)
# print the JSON string representation of the object
print(DeploymentOpaEnableCommand.to_json())

# convert the object into a dict
deployment_opa_enable_command_dict = deployment_opa_enable_command_instance.to_dict()
# create an instance of DeploymentOpaEnableCommand from a dict
deployment_opa_enable_command_from_dict = DeploymentOpaEnableCommand.from_dict(deployment_opa_enable_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



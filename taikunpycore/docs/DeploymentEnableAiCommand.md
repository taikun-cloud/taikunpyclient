# DeploymentEnableAiCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**ai_credential_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.deployment_enable_ai_command import DeploymentEnableAiCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentEnableAiCommand from a JSON string
deployment_enable_ai_command_instance = DeploymentEnableAiCommand.from_json(json)
# print the JSON string representation of the object
print(DeploymentEnableAiCommand.to_json())

# convert the object into a dict
deployment_enable_ai_command_dict = deployment_enable_ai_command_instance.to_dict()
# create an instance of DeploymentEnableAiCommand from a dict
deployment_enable_ai_command_from_dict = DeploymentEnableAiCommand.from_dict(deployment_enable_ai_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DeploymentActionCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | 
**name** | **str** |  | 
**namespace** | **str** |  | 
**scale_replica_count** | **int** |  | [optional] 
**action** | [**EDeploymentAction**](EDeploymentAction.md) |  | 

## Example

```python
from taikunpycore.models.deployment_action_command import DeploymentActionCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentActionCommand from a JSON string
deployment_action_command_instance = DeploymentActionCommand.from_json(json)
# print the JSON string representation of the object
print(DeploymentActionCommand.to_json())

# convert the object into a dict
deployment_action_command_dict = deployment_action_command_instance.to_dict()
# create an instance of DeploymentActionCommand from a dict
deployment_action_command_from_dict = DeploymentActionCommand.from_dict(deployment_action_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



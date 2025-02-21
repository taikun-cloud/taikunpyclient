# DeploymentCompletedCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**result** | **str** |  | [optional] 
**from_cron_job** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.deployment_completed_command import DeploymentCompletedCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentCompletedCommand from a JSON string
deployment_completed_command_instance = DeploymentCompletedCommand.from_json(json)
# print the JSON string representation of the object
print(DeploymentCompletedCommand.to_json())

# convert the object into a dict
deployment_completed_command_dict = deployment_completed_command_instance.to_dict()
# create an instance of DeploymentCompletedCommand from a dict
deployment_completed_command_from_dict = DeploymentCompletedCommand.from_dict(deployment_completed_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



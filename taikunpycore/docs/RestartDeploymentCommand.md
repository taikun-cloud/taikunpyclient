# RestartDeploymentCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.restart_deployment_command import RestartDeploymentCommand

# TODO update the JSON string below
json = "{}"
# create an instance of RestartDeploymentCommand from a JSON string
restart_deployment_command_instance = RestartDeploymentCommand.from_json(json)
# print the JSON string representation of the object
print(RestartDeploymentCommand.to_json())

# convert the object into a dict
restart_deployment_command_dict = restart_deployment_command_instance.to_dict()
# create an instance of RestartDeploymentCommand from a dict
restart_deployment_command_from_dict = RestartDeploymentCommand.from_dict(restart_deployment_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



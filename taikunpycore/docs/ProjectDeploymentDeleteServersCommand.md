# ProjectDeploymentDeleteServersCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**server_ids** | **List[int]** |  | [optional] 
**force_delete_v_clusters** | **bool** |  | [optional] 
**delete_autoscaling_servers** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.project_deployment_delete_servers_command import ProjectDeploymentDeleteServersCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDeploymentDeleteServersCommand from a JSON string
project_deployment_delete_servers_command_instance = ProjectDeploymentDeleteServersCommand.from_json(json)
# print the JSON string representation of the object
print(ProjectDeploymentDeleteServersCommand.to_json())

# convert the object into a dict
project_deployment_delete_servers_command_dict = project_deployment_delete_servers_command_instance.to_dict()
# create an instance of ProjectDeploymentDeleteServersCommand from a dict
project_deployment_delete_servers_command_from_dict = ProjectDeploymentDeleteServersCommand.from_dict(project_deployment_delete_servers_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ProjectDeploymentDeleteVmsCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**vm_ids** | **List[int]** |  | [optional] 

## Example

```python
from taikunpycore.models.project_deployment_delete_vms_command import ProjectDeploymentDeleteVmsCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDeploymentDeleteVmsCommand from a JSON string
project_deployment_delete_vms_command_instance = ProjectDeploymentDeleteVmsCommand.from_json(json)
# print the JSON string representation of the object
print(ProjectDeploymentDeleteVmsCommand.to_json())

# convert the object into a dict
project_deployment_delete_vms_command_dict = project_deployment_delete_vms_command_instance.to_dict()
# create an instance of ProjectDeploymentDeleteVmsCommand from a dict
project_deployment_delete_vms_command_from_dict = ProjectDeploymentDeleteVmsCommand.from_dict(project_deployment_delete_vms_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



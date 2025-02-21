# DeleteKubeConfigByProjectIdCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.delete_kube_config_by_project_id_command import DeleteKubeConfigByProjectIdCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteKubeConfigByProjectIdCommand from a JSON string
delete_kube_config_by_project_id_command_instance = DeleteKubeConfigByProjectIdCommand.from_json(json)
# print the JSON string representation of the object
print(DeleteKubeConfigByProjectIdCommand.to_json())

# convert the object into a dict
delete_kube_config_by_project_id_command_dict = delete_kube_config_by_project_id_command_instance.to_dict()
# create an instance of DeleteKubeConfigByProjectIdCommand from a dict
delete_kube_config_by_project_id_command_from_dict = DeleteKubeConfigByProjectIdCommand.from_dict(delete_kube_config_by_project_id_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



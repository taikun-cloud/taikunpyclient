# AdminUpdateProjectKubeConfigCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.admin_update_project_kube_config_command import AdminUpdateProjectKubeConfigCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUpdateProjectKubeConfigCommand from a JSON string
admin_update_project_kube_config_command_instance = AdminUpdateProjectKubeConfigCommand.from_json(json)
# print the JSON string representation of the object
print(AdminUpdateProjectKubeConfigCommand.to_json())

# convert the object into a dict
admin_update_project_kube_config_command_dict = admin_update_project_kube_config_command_instance.to_dict()
# create an instance of AdminUpdateProjectKubeConfigCommand from a dict
admin_update_project_kube_config_command_from_dict = AdminUpdateProjectKubeConfigCommand.from_dict(admin_update_project_kube_config_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



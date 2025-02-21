# AdminProjectUpdateCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**kubernetes_current_version** | **str** |  | [optional] 
**kubespray_current_version** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.admin_project_update_command import AdminProjectUpdateCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AdminProjectUpdateCommand from a JSON string
admin_project_update_command_instance = AdminProjectUpdateCommand.from_json(json)
# print the JSON string representation of the object
print(AdminProjectUpdateCommand.to_json())

# convert the object into a dict
admin_project_update_command_dict = admin_project_update_command_instance.to_dict()
# create an instance of AdminProjectUpdateCommand from a dict
admin_project_update_command_from_dict = AdminProjectUpdateCommand.from_dict(admin_project_update_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



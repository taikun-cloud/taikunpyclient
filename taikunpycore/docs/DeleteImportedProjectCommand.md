# DeleteImportedProjectCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**is_force_delete** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.delete_imported_project_command import DeleteImportedProjectCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteImportedProjectCommand from a JSON string
delete_imported_project_command_instance = DeleteImportedProjectCommand.from_json(json)
# print the JSON string representation of the object
print(DeleteImportedProjectCommand.to_json())

# convert the object into a dict
delete_imported_project_command_dict = delete_imported_project_command_instance.to_dict()
# create an instance of DeleteImportedProjectCommand from a dict
delete_imported_project_command_from_dict = DeleteImportedProjectCommand.from_dict(delete_imported_project_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateProjectAppCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**catalog_app_id** | **int** |  | [optional] 
**extra_values** | **str** |  | [optional] 
**auto_sync** | **bool** |  | [optional] 
**taikun_link_enabled** | **bool** |  | [optional] 
**parameters** | [**List[ProjectAppParamsDto]**](ProjectAppParamsDto.md) |  | [optional] 

## Example

```python
from taikunpycore.models.create_project_app_command import CreateProjectAppCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectAppCommand from a JSON string
create_project_app_command_instance = CreateProjectAppCommand.from_json(json)
# print the JSON string representation of the object
print(CreateProjectAppCommand.to_json())

# convert the object into a dict
create_project_app_command_dict = create_project_app_command_instance.to_dict()
# create an instance of CreateProjectAppCommand from a dict
create_project_app_command_from_dict = CreateProjectAppCommand.from_dict(create_project_app_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



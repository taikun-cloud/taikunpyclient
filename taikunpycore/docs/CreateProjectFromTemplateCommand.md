# CreateProjectFromTemplateCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_name** | **str** |  | [optional] 
**can_commit** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.create_project_from_template_command import CreateProjectFromTemplateCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectFromTemplateCommand from a JSON string
create_project_from_template_command_instance = CreateProjectFromTemplateCommand.from_json(json)
# print the JSON string representation of the object
print(CreateProjectFromTemplateCommand.to_json())

# convert the object into a dict
create_project_from_template_command_dict = create_project_from_template_command_instance.to_dict()
# create an instance of CreateProjectFromTemplateCommand from a dict
create_project_from_template_command_from_dict = CreateProjectFromTemplateCommand.from_dict(create_project_from_template_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



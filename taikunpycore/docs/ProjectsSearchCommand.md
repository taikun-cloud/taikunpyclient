# ProjectsSearchCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_term** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.projects_search_command import ProjectsSearchCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsSearchCommand from a JSON string
projects_search_command_instance = ProjectsSearchCommand.from_json(json)
# print the JSON string representation of the object
print(ProjectsSearchCommand.to_json())

# convert the object into a dict
projects_search_command_dict = projects_search_command_instance.to_dict()
# create an instance of ProjectsSearchCommand from a dict
projects_search_command_from_dict = ProjectsSearchCommand.from_dict(projects_search_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



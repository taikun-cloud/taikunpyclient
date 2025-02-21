# BindFlavorToProjectCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**flavors** | **List[str]** |  | [optional] 

## Example

```python
from taikunpycore.models.bind_flavor_to_project_command import BindFlavorToProjectCommand

# TODO update the JSON string below
json = "{}"
# create an instance of BindFlavorToProjectCommand from a JSON string
bind_flavor_to_project_command_instance = BindFlavorToProjectCommand.from_json(json)
# print the JSON string representation of the object
print(BindFlavorToProjectCommand.to_json())

# convert the object into a dict
bind_flavor_to_project_command_dict = bind_flavor_to_project_command_instance.to_dict()
# create an instance of BindFlavorToProjectCommand from a dict
bind_flavor_to_project_command_from_dict = BindFlavorToProjectCommand.from_dict(bind_flavor_to_project_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



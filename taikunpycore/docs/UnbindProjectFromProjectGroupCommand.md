# UnbindProjectFromProjectGroupCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_group_id** | **int** |  | [optional] 
**project_ids** | **List[int]** |  | [optional] 

## Example

```python
from taikunpycore.models.unbind_project_from_project_group_command import UnbindProjectFromProjectGroupCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UnbindProjectFromProjectGroupCommand from a JSON string
unbind_project_from_project_group_command_instance = UnbindProjectFromProjectGroupCommand.from_json(json)
# print the JSON string representation of the object
print(UnbindProjectFromProjectGroupCommand.to_json())

# convert the object into a dict
unbind_project_from_project_group_command_dict = unbind_project_from_project_group_command_instance.to_dict()
# create an instance of UnbindProjectFromProjectGroupCommand from a dict
unbind_project_from_project_group_command_from_dict = UnbindProjectFromProjectGroupCommand.from_dict(unbind_project_from_project_group_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateProjectGroupCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**project_ids** | **List[int]** |  | [optional] 

## Example

```python
from taikunpycore.models.create_project_group_command import CreateProjectGroupCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectGroupCommand from a JSON string
create_project_group_command_instance = CreateProjectGroupCommand.from_json(json)
# print the JSON string representation of the object
print(CreateProjectGroupCommand.to_json())

# convert the object into a dict
create_project_group_command_dict = create_project_group_command_instance.to_dict()
# create an instance of CreateProjectGroupCommand from a dict
create_project_group_command_from_dict = CreateProjectGroupCommand.from_dict(create_project_group_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



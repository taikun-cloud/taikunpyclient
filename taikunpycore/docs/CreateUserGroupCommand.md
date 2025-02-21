# CreateUserGroupCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**user_ids** | **List[str]** |  | [optional] 

## Example

```python
from taikunpycore.models.create_user_group_command import CreateUserGroupCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserGroupCommand from a JSON string
create_user_group_command_instance = CreateUserGroupCommand.from_json(json)
# print the JSON string representation of the object
print(CreateUserGroupCommand.to_json())

# convert the object into a dict
create_user_group_command_dict = create_user_group_command_instance.to_dict()
# create an instance of CreateUserGroupCommand from a dict
create_user_group_command_from_dict = CreateUserGroupCommand.from_dict(create_user_group_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



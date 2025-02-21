# DeleteUserGroupCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_group_ids** | **List[int]** |  | [optional] 

## Example

```python
from taikunpycore.models.delete_user_group_command import DeleteUserGroupCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteUserGroupCommand from a JSON string
delete_user_group_command_instance = DeleteUserGroupCommand.from_json(json)
# print the JSON string representation of the object
print(DeleteUserGroupCommand.to_json())

# convert the object into a dict
delete_user_group_command_dict = delete_user_group_command_instance.to_dict()
# create an instance of DeleteUserGroupCommand from a dict
delete_user_group_command_from_dict = DeleteUserGroupCommand.from_dict(delete_user_group_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



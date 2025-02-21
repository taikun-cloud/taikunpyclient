# EditSshUserCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**ssh_public_key** | **str** |  | [optional] 
**access_profile_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.edit_ssh_user_command import EditSshUserCommand

# TODO update the JSON string below
json = "{}"
# create an instance of EditSshUserCommand from a JSON string
edit_ssh_user_command_instance = EditSshUserCommand.from_json(json)
# print the JSON string representation of the object
print(EditSshUserCommand.to_json())

# convert the object into a dict
edit_ssh_user_command_dict = edit_ssh_user_command_instance.to_dict()
# create an instance of EditSshUserCommand from a dict
edit_ssh_user_command_from_dict = EditSshUserCommand.from_dict(edit_ssh_user_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateSshUserCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**ssh_public_key** | **str** |  | [optional] 
**access_profile_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.create_ssh_user_command import CreateSshUserCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSshUserCommand from a JSON string
create_ssh_user_command_instance = CreateSshUserCommand.from_json(json)
# print the JSON string representation of the object
print(CreateSshUserCommand.to_json())

# convert the object into a dict
create_ssh_user_command_dict = create_ssh_user_command_instance.to_dict()
# create an instance of CreateSshUserCommand from a dict
create_ssh_user_command_from_dict = CreateSshUserCommand.from_dict(create_ssh_user_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



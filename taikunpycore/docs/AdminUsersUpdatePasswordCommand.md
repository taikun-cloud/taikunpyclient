# AdminUsersUpdatePasswordCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.admin_users_update_password_command import AdminUsersUpdatePasswordCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUsersUpdatePasswordCommand from a JSON string
admin_users_update_password_command_instance = AdminUsersUpdatePasswordCommand.from_json(json)
# print the JSON string representation of the object
print(AdminUsersUpdatePasswordCommand.to_json())

# convert the object into a dict
admin_users_update_password_command_dict = admin_users_update_password_command_instance.to_dict()
# create an instance of AdminUsersUpdatePasswordCommand from a dict
admin_users_update_password_command_from_dict = AdminUsersUpdatePasswordCommand.from_dict(admin_users_update_password_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



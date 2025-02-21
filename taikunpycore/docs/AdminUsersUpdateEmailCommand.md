# AdminUsersUpdateEmailCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.admin_users_update_email_command import AdminUsersUpdateEmailCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUsersUpdateEmailCommand from a JSON string
admin_users_update_email_command_instance = AdminUsersUpdateEmailCommand.from_json(json)
# print the JSON string representation of the object
print(AdminUsersUpdateEmailCommand.to_json())

# convert the object into a dict
admin_users_update_email_command_dict = admin_users_update_email_command_instance.to_dict()
# create an instance of AdminUsersUpdateEmailCommand from a dict
admin_users_update_email_command_from_dict = AdminUsersUpdateEmailCommand.from_dict(admin_users_update_email_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



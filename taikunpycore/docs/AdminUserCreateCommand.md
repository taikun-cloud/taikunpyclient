# AdminUserCreateCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**role** | [**UserRole**](UserRole.md) |  | [optional] 
**organization_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.admin_user_create_command import AdminUserCreateCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUserCreateCommand from a JSON string
admin_user_create_command_instance = AdminUserCreateCommand.from_json(json)
# print the JSON string representation of the object
print(AdminUserCreateCommand.to_json())

# convert the object into a dict
admin_user_create_command_dict = admin_user_create_command_instance.to_dict()
# create an instance of AdminUserCreateCommand from a dict
admin_user_create_command_from_dict = AdminUserCreateCommand.from_dict(admin_user_create_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



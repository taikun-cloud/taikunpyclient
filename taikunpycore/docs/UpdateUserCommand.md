# UpdateUserCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**role** | [**UserRole**](UserRole.md) |  | [optional] 
**force_to_reset_password** | **bool** |  | [optional] 
**disable** | **bool** |  | [optional] 
**is_approved_by_partner** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.update_user_command import UpdateUserCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserCommand from a JSON string
update_user_command_instance = UpdateUserCommand.from_json(json)
# print the JSON string representation of the object
print(UpdateUserCommand.to_json())

# convert the object into a dict
update_user_command_dict = update_user_command_instance.to_dict()
# create an instance of UpdateUserCommand from a dict
update_user_command_from_dict = UpdateUserCommand.from_dict(update_user_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



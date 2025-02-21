# CreateUserCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**role** | [**UserRole**](UserRole.md) |  | [optional] 

## Example

```python
from taikunpycore.models.create_user_command import CreateUserCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserCommand from a JSON string
create_user_command_instance = CreateUserCommand.from_json(json)
# print the JSON string representation of the object
print(CreateUserCommand.to_json())

# convert the object into a dict
create_user_command_dict = create_user_command_instance.to_dict()
# create an instance of CreateUserCommand from a dict
create_user_command_from_dict = CreateUserCommand.from_dict(create_user_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UserExistCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.user_exist_command import UserExistCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UserExistCommand from a JSON string
user_exist_command_instance = UserExistCommand.from_json(json)
# print the JSON string representation of the object
print(UserExistCommand.to_json())

# convert the object into a dict
user_exist_command_dict = user_exist_command_instance.to_dict()
# create an instance of UserExistCommand from a dict
user_exist_command_from_dict = UserExistCommand.from_dict(user_exist_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



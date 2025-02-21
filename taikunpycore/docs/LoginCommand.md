# LoginCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 
**access_key** | **str** |  | [optional] 
**secret_key** | **str** |  | [optional] 
**local** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.login_command import LoginCommand

# TODO update the JSON string below
json = "{}"
# create an instance of LoginCommand from a JSON string
login_command_instance = LoginCommand.from_json(json)
# print the JSON string representation of the object
print(LoginCommand.to_json())

# convert the object into a dict
login_command_dict = login_command_instance.to_dict()
# create an instance of LoginCommand from a dict
login_command_from_dict = LoginCommand.from_dict(login_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UserTokenCreateCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expire_date** | **datetime** |  | [optional] 
**is_readonly** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**endpoints** | [**List[AvailableEndpointData]**](AvailableEndpointData.md) |  | [optional] 
**bind_all** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.user_token_create_command import UserTokenCreateCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UserTokenCreateCommand from a JSON string
user_token_create_command_instance = UserTokenCreateCommand.from_json(json)
# print the JSON string representation of the object
print(UserTokenCreateCommand.to_json())

# convert the object into a dict
user_token_create_command_dict = user_token_create_command_instance.to_dict()
# create an instance of UserTokenCreateCommand from a dict
user_token_create_command_from_dict = UserTokenCreateCommand.from_dict(user_token_create_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



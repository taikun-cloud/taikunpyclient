# UsersSearchCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_term** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.users_search_command import UsersSearchCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UsersSearchCommand from a JSON string
users_search_command_instance = UsersSearchCommand.from_json(json)
# print the JSON string representation of the object
print(UsersSearchCommand.to_json())

# convert the object into a dict
users_search_command_dict = users_search_command_instance.to_dict()
# create an instance of UsersSearchCommand from a dict
users_search_command_from_dict = UsersSearchCommand.from_dict(users_search_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



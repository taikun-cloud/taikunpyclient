# AccessProfilesSearchCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_term** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.access_profiles_search_command import AccessProfilesSearchCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AccessProfilesSearchCommand from a JSON string
access_profiles_search_command_instance = AccessProfilesSearchCommand.from_json(json)
# print the JSON string representation of the object
print(AccessProfilesSearchCommand.to_json())

# convert the object into a dict
access_profiles_search_command_dict = access_profiles_search_command_instance.to_dict()
# create an instance of AccessProfilesSearchCommand from a dict
access_profiles_search_command_from_dict = AccessProfilesSearchCommand.from_dict(access_profiles_search_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



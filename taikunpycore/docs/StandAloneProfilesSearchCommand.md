# StandAloneProfilesSearchCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_term** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.stand_alone_profiles_search_command import StandAloneProfilesSearchCommand

# TODO update the JSON string below
json = "{}"
# create an instance of StandAloneProfilesSearchCommand from a JSON string
stand_alone_profiles_search_command_instance = StandAloneProfilesSearchCommand.from_json(json)
# print the JSON string representation of the object
print(StandAloneProfilesSearchCommand.to_json())

# convert the object into a dict
stand_alone_profiles_search_command_dict = stand_alone_profiles_search_command_instance.to_dict()
# create an instance of StandAloneProfilesSearchCommand from a dict
stand_alone_profiles_search_command_from_dict = StandAloneProfilesSearchCommand.from_dict(stand_alone_profiles_search_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



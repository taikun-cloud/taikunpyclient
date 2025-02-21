# PartnersSearchCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_term** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.partners_search_command import PartnersSearchCommand

# TODO update the JSON string below
json = "{}"
# create an instance of PartnersSearchCommand from a JSON string
partners_search_command_instance = PartnersSearchCommand.from_json(json)
# print the JSON string representation of the object
print(PartnersSearchCommand.to_json())

# convert the object into a dict
partners_search_command_dict = partners_search_command_instance.to_dict()
# create an instance of PartnersSearchCommand from a dict
partners_search_command_from_dict = PartnersSearchCommand.from_dict(partners_search_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



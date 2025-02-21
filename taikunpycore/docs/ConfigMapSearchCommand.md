# ConfigMapSearchCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_term** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.config_map_search_command import ConfigMapSearchCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigMapSearchCommand from a JSON string
config_map_search_command_instance = ConfigMapSearchCommand.from_json(json)
# print the JSON string representation of the object
print(ConfigMapSearchCommand.to_json())

# convert the object into a dict
config_map_search_command_dict = config_map_search_command_instance.to_dict()
# create an instance of ConfigMapSearchCommand from a dict
config_map_search_command_from_dict = ConfigMapSearchCommand.from_dict(config_map_search_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



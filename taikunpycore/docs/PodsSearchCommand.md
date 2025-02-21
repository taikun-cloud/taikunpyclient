# PodsSearchCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_term** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.pods_search_command import PodsSearchCommand

# TODO update the JSON string below
json = "{}"
# create an instance of PodsSearchCommand from a JSON string
pods_search_command_instance = PodsSearchCommand.from_json(json)
# print the JSON string representation of the object
print(PodsSearchCommand.to_json())

# convert the object into a dict
pods_search_command_dict = pods_search_command_instance.to_dict()
# create an instance of PodsSearchCommand from a dict
pods_search_command_from_dict = PodsSearchCommand.from_dict(pods_search_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



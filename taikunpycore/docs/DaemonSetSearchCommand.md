# DaemonSetSearchCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_term** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.daemon_set_search_command import DaemonSetSearchCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DaemonSetSearchCommand from a JSON string
daemon_set_search_command_instance = DaemonSetSearchCommand.from_json(json)
# print the JSON string representation of the object
print(DaemonSetSearchCommand.to_json())

# convert the object into a dict
daemon_set_search_command_dict = daemon_set_search_command_instance.to_dict()
# create an instance of DaemonSetSearchCommand from a dict
daemon_set_search_command_from_dict = DaemonSetSearchCommand.from_dict(daemon_set_search_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



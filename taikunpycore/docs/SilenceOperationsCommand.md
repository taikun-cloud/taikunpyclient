# SilenceOperationsCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.silence_operations_command import SilenceOperationsCommand

# TODO update the JSON string below
json = "{}"
# create an instance of SilenceOperationsCommand from a JSON string
silence_operations_command_instance = SilenceOperationsCommand.from_json(json)
# print the JSON string representation of the object
print(SilenceOperationsCommand.to_json())

# convert the object into a dict
silence_operations_command_dict = silence_operations_command_instance.to_dict()
# create an instance of SilenceOperationsCommand from a dict
silence_operations_command_from_dict = SilenceOperationsCommand.from_dict(silence_operations_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



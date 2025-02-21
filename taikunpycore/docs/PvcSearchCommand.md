# PvcSearchCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_term** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.pvc_search_command import PvcSearchCommand

# TODO update the JSON string below
json = "{}"
# create an instance of PvcSearchCommand from a JSON string
pvc_search_command_instance = PvcSearchCommand.from_json(json)
# print the JSON string representation of the object
print(PvcSearchCommand.to_json())

# convert the object into a dict
pvc_search_command_dict = pvc_search_command_instance.to_dict()
# create an instance of PvcSearchCommand from a dict
pvc_search_command_from_dict = PvcSearchCommand.from_dict(pvc_search_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



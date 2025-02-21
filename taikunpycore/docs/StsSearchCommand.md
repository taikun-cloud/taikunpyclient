# StsSearchCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_term** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.sts_search_command import StsSearchCommand

# TODO update the JSON string below
json = "{}"
# create an instance of StsSearchCommand from a JSON string
sts_search_command_instance = StsSearchCommand.from_json(json)
# print the JSON string representation of the object
print(StsSearchCommand.to_json())

# convert the object into a dict
sts_search_command_dict = sts_search_command_instance.to_dict()
# create an instance of StsSearchCommand from a dict
sts_search_command_from_dict = StsSearchCommand.from_dict(sts_search_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ServiceSearchCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_term** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.service_search_command import ServiceSearchCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSearchCommand from a JSON string
service_search_command_instance = ServiceSearchCommand.from_json(json)
# print the JSON string representation of the object
print(ServiceSearchCommand.to_json())

# convert the object into a dict
service_search_command_dict = service_search_command_instance.to_dict()
# create an instance of ServiceSearchCommand from a dict
service_search_command_from_dict = ServiceSearchCommand.from_dict(service_search_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



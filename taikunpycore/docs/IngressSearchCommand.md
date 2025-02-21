# IngressSearchCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_term** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.ingress_search_command import IngressSearchCommand

# TODO update the JSON string below
json = "{}"
# create an instance of IngressSearchCommand from a JSON string
ingress_search_command_instance = IngressSearchCommand.from_json(json)
# print the JSON string representation of the object
print(IngressSearchCommand.to_json())

# convert the object into a dict
ingress_search_command_dict = ingress_search_command_instance.to_dict()
# create an instance of IngressSearchCommand from a dict
ingress_search_command_from_dict = IngressSearchCommand.from_dict(ingress_search_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



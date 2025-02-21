# BindUnbindEndpointToTokenCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** |  | [optional] 
**endpoints** | [**List[AvailableEndpointData]**](AvailableEndpointData.md) |  | [optional] 
**bind_all** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.bind_unbind_endpoint_to_token_command import BindUnbindEndpointToTokenCommand

# TODO update the JSON string below
json = "{}"
# create an instance of BindUnbindEndpointToTokenCommand from a JSON string
bind_unbind_endpoint_to_token_command_instance = BindUnbindEndpointToTokenCommand.from_json(json)
# print the JSON string representation of the object
print(BindUnbindEndpointToTokenCommand.to_json())

# convert the object into a dict
bind_unbind_endpoint_to_token_command_dict = bind_unbind_endpoint_to_token_command_instance.to_dict()
# create an instance of BindUnbindEndpointToTokenCommand from a dict
bind_unbind_endpoint_to_token_command_from_dict = BindUnbindEndpointToTokenCommand.from_dict(bind_unbind_endpoint_to_token_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



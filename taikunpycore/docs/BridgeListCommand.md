# BridgeListCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**token_id** | **str** |  | [optional] 
**token_secret** | **str** |  | [optional] 
**hypervisor** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.bridge_list_command import BridgeListCommand

# TODO update the JSON string below
json = "{}"
# create an instance of BridgeListCommand from a JSON string
bridge_list_command_instance = BridgeListCommand.from_json(json)
# print the JSON string representation of the object
print(BridgeListCommand.to_json())

# convert the object into a dict
bridge_list_command_dict = bridge_list_command_instance.to_dict()
# create an instance of BridgeListCommand from a dict
bridge_list_command_from_dict = BridgeListCommand.from_dict(bridge_list_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



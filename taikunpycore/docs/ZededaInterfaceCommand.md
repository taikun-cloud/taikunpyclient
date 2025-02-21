# ZededaInterfaceCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_url** | **str** |  | [optional] 
**api_token** | **str** |  | [optional] 
**project** | **str** |  | [optional] 
**edge_node** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.zededa_interface_command import ZededaInterfaceCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ZededaInterfaceCommand from a JSON string
zededa_interface_command_instance = ZededaInterfaceCommand.from_json(json)
# print the JSON string representation of the object
print(ZededaInterfaceCommand.to_json())

# convert the object into a dict
zededa_interface_command_dict = zededa_interface_command_instance.to_dict()
# create an instance of ZededaInterfaceCommand from a dict
zededa_interface_command_from_dict = ZededaInterfaceCommand.from_dict(zededa_interface_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



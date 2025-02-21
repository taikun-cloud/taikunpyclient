# NetworkListCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**datacenter_id** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.network_list_command import NetworkListCommand

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkListCommand from a JSON string
network_list_command_instance = NetworkListCommand.from_json(json)
# print the JSON string representation of the object
print(NetworkListCommand.to_json())

# convert the object into a dict
network_list_command_dict = network_list_command_instance.to_dict()
# create an instance of NetworkListCommand from a dict
network_list_command_from_dict = NetworkListCommand.from_dict(network_list_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



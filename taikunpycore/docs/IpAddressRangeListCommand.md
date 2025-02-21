# IpAddressRangeListCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** |  | [optional] 
**net_mask** | **int** |  | [optional] 
**gateway** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.ip_address_range_list_command import IpAddressRangeListCommand

# TODO update the JSON string below
json = "{}"
# create an instance of IpAddressRangeListCommand from a JSON string
ip_address_range_list_command_instance = IpAddressRangeListCommand.from_json(json)
# print the JSON string representation of the object
print(IpAddressRangeListCommand.to_json())

# convert the object into a dict
ip_address_range_list_command_dict = ip_address_range_list_command_instance.to_dict()
# create an instance of IpAddressRangeListCommand from a dict
ip_address_range_list_command_from_dict = IpAddressRangeListCommand.from_dict(ip_address_range_list_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



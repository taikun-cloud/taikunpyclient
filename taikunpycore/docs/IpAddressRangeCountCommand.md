# IpAddressRangeCountCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin** | **str** |  | [optional] 
**end** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.ip_address_range_count_command import IpAddressRangeCountCommand

# TODO update the JSON string below
json = "{}"
# create an instance of IpAddressRangeCountCommand from a JSON string
ip_address_range_count_command_instance = IpAddressRangeCountCommand.from_json(json)
# print the JSON string representation of the object
print(IpAddressRangeCountCommand.to_json())

# convert the object into a dict
ip_address_range_count_command_dict = ip_address_range_count_command_instance.to_dict()
# create an instance of IpAddressRangeCountCommand from a dict
ip_address_range_count_command_from_dict = IpAddressRangeCountCommand.from_dict(ip_address_range_count_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



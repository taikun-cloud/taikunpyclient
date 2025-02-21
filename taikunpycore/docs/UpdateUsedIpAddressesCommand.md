# UpdateUsedIpAddressesCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **List[str]** |  | [optional] 

## Example

```python
from taikunpycore.models.update_used_ip_addresses_command import UpdateUsedIpAddressesCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUsedIpAddressesCommand from a JSON string
update_used_ip_addresses_command_instance = UpdateUsedIpAddressesCommand.from_json(json)
# print the JSON string representation of the object
print(UpdateUsedIpAddressesCommand.to_json())

# convert the object into a dict
update_used_ip_addresses_command_dict = update_used_ip_addresses_command_instance.to_dict()
# create an instance of UpdateUsedIpAddressesCommand from a dict
update_used_ip_addresses_command_from_dict = UpdateUsedIpAddressesCommand.from_dict(update_used_ip_addresses_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



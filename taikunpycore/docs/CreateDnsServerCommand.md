# CreateDnsServerCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**access_profile_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.create_dns_server_command import CreateDnsServerCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDnsServerCommand from a JSON string
create_dns_server_command_instance = CreateDnsServerCommand.from_json(json)
# print the JSON string representation of the object
print(CreateDnsServerCommand.to_json())

# convert the object into a dict
create_dns_server_command_dict = create_dns_server_command_instance.to_dict()
# create an instance of CreateDnsServerCommand from a dict
create_dns_server_command_from_dict = CreateDnsServerCommand.from_dict(create_dns_server_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



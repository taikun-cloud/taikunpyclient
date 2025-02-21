# DnsServersListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**address** | **str** |  | 
**access_profile_name** | **str** |  | 

## Example

```python
from taikunpycore.models.dns_servers_list_dto import DnsServersListDto

# TODO update the JSON string below
json = "{}"
# create an instance of DnsServersListDto from a JSON string
dns_servers_list_dto_instance = DnsServersListDto.from_json(json)
# print the JSON string representation of the object
print(DnsServersListDto.to_json())

# convert the object into a dict
dns_servers_list_dto_dict = dns_servers_list_dto_instance.to_dict()
# create an instance of DnsServersListDto from a dict
dns_servers_list_dto_from_dict = DnsServersListDto.from_dict(dns_servers_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DnsServerListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**address** | **str** |  | 

## Example

```python
from taikunpycore.models.dns_server_list_dto import DnsServerListDto

# TODO update the JSON string below
json = "{}"
# create an instance of DnsServerListDto from a JSON string
dns_server_list_dto_instance = DnsServerListDto.from_json(json)
# print the JSON string representation of the object
print(DnsServerListDto.to_json())

# convert the object into a dict
dns_server_list_dto_dict = dns_server_list_dto_instance.to_dict()
# create an instance of DnsServerListDto from a dict
dns_server_list_dto_from_dict = DnsServerListDto.from_dict(dns_server_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



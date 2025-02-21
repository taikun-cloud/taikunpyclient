# DnsServerCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.dns_server_create_dto import DnsServerCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of DnsServerCreateDto from a JSON string
dns_server_create_dto_instance = DnsServerCreateDto.from_json(json)
# print the JSON string representation of the object
print(DnsServerCreateDto.to_json())

# convert the object into a dict
dns_server_create_dto_dict = dns_server_create_dto_instance.to_dict()
# create an instance of DnsServerCreateDto from a dict
dns_server_create_dto_from_dict = DnsServerCreateDto.from_dict(dns_server_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



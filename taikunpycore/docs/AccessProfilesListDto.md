# AccessProfilesListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**http_proxy** | **str** |  | 
**organization_id** | **int** |  | 
**organization_name** | **str** |  | 
**is_locked** | **bool** |  | 
**dns_servers** | [**List[DnsServerListDto]**](DnsServerListDto.md) |  | 
**ntp_servers** | [**List[NtpServerListDto]**](NtpServerListDto.md) |  | 
**allowed_hosts** | [**List[AllowedHostListDto]**](AllowedHostListDto.md) |  | 
**projects** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**created_by** | **str** |  | 
**last_modified** | **str** |  | 
**last_modified_by** | **str** |  | 
**created_at** | **str** |  | 

## Example

```python
from taikunpycore.models.access_profiles_list_dto import AccessProfilesListDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccessProfilesListDto from a JSON string
access_profiles_list_dto_instance = AccessProfilesListDto.from_json(json)
# print the JSON string representation of the object
print(AccessProfilesListDto.to_json())

# convert the object into a dict
access_profiles_list_dto_dict = access_profiles_list_dto_instance.to_dict()
# create an instance of AccessProfilesListDto from a dict
access_profiles_list_dto_from_dict = AccessProfilesListDto.from_dict(access_profiles_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



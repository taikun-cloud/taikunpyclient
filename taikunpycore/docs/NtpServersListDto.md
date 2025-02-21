# NtpServersListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**address** | **str** |  | 
**access_profile_name** | **str** |  | 

## Example

```python
from taikunpycore.models.ntp_servers_list_dto import NtpServersListDto

# TODO update the JSON string below
json = "{}"
# create an instance of NtpServersListDto from a JSON string
ntp_servers_list_dto_instance = NtpServersListDto.from_json(json)
# print the JSON string representation of the object
print(NtpServersListDto.to_json())

# convert the object into a dict
ntp_servers_list_dto_dict = ntp_servers_list_dto_instance.to_dict()
# create an instance of NtpServersListDto from a dict
ntp_servers_list_dto_from_dict = NtpServersListDto.from_dict(ntp_servers_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



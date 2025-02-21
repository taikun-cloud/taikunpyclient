# NtpServerListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**address** | **str** |  | 

## Example

```python
from taikunpycore.models.ntp_server_list_dto import NtpServerListDto

# TODO update the JSON string below
json = "{}"
# create an instance of NtpServerListDto from a JSON string
ntp_server_list_dto_instance = NtpServerListDto.from_json(json)
# print the JSON string representation of the object
print(NtpServerListDto.to_json())

# convert the object into a dict
ntp_server_list_dto_dict = ntp_server_list_dto_instance.to_dict()
# create an instance of NtpServerListDto from a dict
ntp_server_list_dto_from_dict = NtpServerListDto.from_dict(ntp_server_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



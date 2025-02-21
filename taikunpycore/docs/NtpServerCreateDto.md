# NtpServerCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.ntp_server_create_dto import NtpServerCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of NtpServerCreateDto from a JSON string
ntp_server_create_dto_instance = NtpServerCreateDto.from_json(json)
# print the JSON string representation of the object
print(NtpServerCreateDto.to_json())

# convert the object into a dict
ntp_server_create_dto_dict = ntp_server_create_dto_instance.to_dict()
# create an instance of NtpServerCreateDto from a dict
ntp_server_create_dto_from_dict = NtpServerCreateDto.from_dict(ntp_server_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



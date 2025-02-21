# CreateAccessProfileCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**http_proxy** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**ssh_users** | [**List[SshUserCreateDto]**](SshUserCreateDto.md) |  | [optional] 
**dns_servers** | [**List[DnsServerCreateDto]**](DnsServerCreateDto.md) |  | [optional] 
**ntp_servers** | [**List[NtpServerCreateDto]**](NtpServerCreateDto.md) |  | [optional] 
**allowed_hosts** | [**List[AllowedHostCreateDto]**](AllowedHostCreateDto.md) |  | [optional] 

## Example

```python
from taikunpycore.models.create_access_profile_command import CreateAccessProfileCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccessProfileCommand from a JSON string
create_access_profile_command_instance = CreateAccessProfileCommand.from_json(json)
# print the JSON string representation of the object
print(CreateAccessProfileCommand.to_json())

# convert the object into a dict
create_access_profile_command_dict = create_access_profile_command_instance.to_dict()
# create an instance of CreateAccessProfileCommand from a dict
create_access_profile_command_from_dict = CreateAccessProfileCommand.from_dict(create_access_profile_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



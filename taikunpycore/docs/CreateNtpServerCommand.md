# CreateNtpServerCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**access_profile_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.create_ntp_server_command import CreateNtpServerCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNtpServerCommand from a JSON string
create_ntp_server_command_instance = CreateNtpServerCommand.from_json(json)
# print the JSON string representation of the object
print(CreateNtpServerCommand.to_json())

# convert the object into a dict
create_ntp_server_command_dict = create_ntp_server_command_instance.to_dict()
# create an instance of CreateNtpServerCommand from a dict
create_ntp_server_command_from_dict = CreateNtpServerCommand.from_dict(create_ntp_server_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



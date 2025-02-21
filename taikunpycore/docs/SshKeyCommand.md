# SshKeyCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssh_public_key** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.ssh_key_command import SshKeyCommand

# TODO update the JSON string below
json = "{}"
# create an instance of SshKeyCommand from a JSON string
ssh_key_command_instance = SshKeyCommand.from_json(json)
# print the JSON string representation of the object
print(SshKeyCommand.to_json())

# convert the object into a dict
ssh_key_command_dict = ssh_key_command_instance.to_dict()
# create an instance of SshKeyCommand from a dict
ssh_key_command_from_dict = SshKeyCommand.from_dict(ssh_key_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



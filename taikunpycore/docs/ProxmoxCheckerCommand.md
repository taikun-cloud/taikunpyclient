# ProxmoxCheckerCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**token_id** | **str** |  | [optional] 
**token_secret** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.proxmox_checker_command import ProxmoxCheckerCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ProxmoxCheckerCommand from a JSON string
proxmox_checker_command_instance = ProxmoxCheckerCommand.from_json(json)
# print the JSON string representation of the object
print(ProxmoxCheckerCommand.to_json())

# convert the object into a dict
proxmox_checker_command_dict = proxmox_checker_command_instance.to_dict()
# create an instance of ProxmoxCheckerCommand from a dict
proxmox_checker_command_from_dict = ProxmoxCheckerCommand.from_dict(proxmox_checker_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



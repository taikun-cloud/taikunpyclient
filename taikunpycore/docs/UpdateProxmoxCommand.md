# UpdateProxmoxCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**token_id** | **str** |  | [optional] 
**token_secret** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.update_proxmox_command import UpdateProxmoxCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProxmoxCommand from a JSON string
update_proxmox_command_instance = UpdateProxmoxCommand.from_json(json)
# print the JSON string representation of the object
print(UpdateProxmoxCommand.to_json())

# convert the object into a dict
update_proxmox_command_dict = update_proxmox_command_instance.to_dict()
# create an instance of UpdateProxmoxCommand from a dict
update_proxmox_command_from_dict = UpdateProxmoxCommand.from_dict(update_proxmox_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



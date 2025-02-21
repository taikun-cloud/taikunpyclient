# CreateProxmoxCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**token_id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**token_secret** | **str** |  | [optional] 
**storage** | **str** |  | [optional] 
**vm_template_name** | **str** |  | [optional] 
**continent** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**hypervisors** | **List[str]** |  | [optional] 
**public_network** | [**CreateProxmoxNetworkDto**](CreateProxmoxNetworkDto.md) |  | [optional] 
**private_network** | [**CreateProxmoxNetworkDto**](CreateProxmoxNetworkDto.md) |  | [optional] 
**skip_tls_flag** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.create_proxmox_command import CreateProxmoxCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProxmoxCommand from a JSON string
create_proxmox_command_instance = CreateProxmoxCommand.from_json(json)
# print the JSON string representation of the object
print(CreateProxmoxCommand.to_json())

# convert the object into a dict
create_proxmox_command_dict = create_proxmox_command_instance.to_dict()
# create an instance of CreateProxmoxCommand from a dict
create_proxmox_command_from_dict = CreateProxmoxCommand.from_dict(create_proxmox_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



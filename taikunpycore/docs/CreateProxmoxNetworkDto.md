# CreateProxmoxNetworkDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bridge** | **str** |  | [optional] 
**gateway** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**net_mask** | **int** |  | [optional] 
**begin_allocation_range** | **str** |  | [optional] 
**end_allocation_range** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.create_proxmox_network_dto import CreateProxmoxNetworkDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProxmoxNetworkDto from a JSON string
create_proxmox_network_dto_instance = CreateProxmoxNetworkDto.from_json(json)
# print the JSON string representation of the object
print(CreateProxmoxNetworkDto.to_json())

# convert the object into a dict
create_proxmox_network_dto_dict = create_proxmox_network_dto_instance.to_dict()
# create an instance of CreateProxmoxNetworkDto from a dict
create_proxmox_network_dto_from_dict = CreateProxmoxNetworkDto.from_dict(create_proxmox_network_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



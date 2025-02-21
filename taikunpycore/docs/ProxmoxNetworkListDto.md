# ProxmoxNetworkListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bridge** | **str** |  | 
**gateway** | **str** |  | 
**ip_address** | **str** |  | 
**net_mask** | **int** |  | 
**begin_allocation_range** | **str** |  | 
**end_allocation_range** | **str** |  | 
**is_private** | **bool** |  | 
**is_virtual_lb_network** | **bool** |  | 

## Example

```python
from taikunpycore.models.proxmox_network_list_dto import ProxmoxNetworkListDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProxmoxNetworkListDto from a JSON string
proxmox_network_list_dto_instance = ProxmoxNetworkListDto.from_json(json)
# print the JSON string representation of the object
print(ProxmoxNetworkListDto.to_json())

# convert the object into a dict
proxmox_network_list_dto_dict = proxmox_network_list_dto_instance.to_dict()
# create an instance of ProxmoxNetworkListDto from a dict
proxmox_network_list_dto_from_dict = ProxmoxNetworkListDto.from_dict(proxmox_network_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



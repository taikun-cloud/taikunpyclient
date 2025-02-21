# VsphereNetworkListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**gateway** | **str** |  | 
**ip_address** | **str** |  | 
**net_mask** | **int** |  | 
**begin_allocation_range** | **str** |  | 
**end_allocation_range** | **str** |  | 
**is_private** | **bool** |  | 
**is_virtual_lb_network** | **bool** |  | 

## Example

```python
from taikunpycore.models.vsphere_network_list_dto import VsphereNetworkListDto

# TODO update the JSON string below
json = "{}"
# create an instance of VsphereNetworkListDto from a JSON string
vsphere_network_list_dto_instance = VsphereNetworkListDto.from_json(json)
# print the JSON string representation of the object
print(VsphereNetworkListDto.to_json())

# convert the object into a dict
vsphere_network_list_dto_dict = vsphere_network_list_dto_instance.to_dict()
# create an instance of VsphereNetworkListDto from a dict
vsphere_network_list_dto_from_dict = VsphereNetworkListDto.from_dict(vsphere_network_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ZededaNetworkListDto


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
**vlan_id** | **int** |  | 

## Example

```python
from taikunpycore.models.zededa_network_list_dto import ZededaNetworkListDto

# TODO update the JSON string below
json = "{}"
# create an instance of ZededaNetworkListDto from a JSON string
zededa_network_list_dto_instance = ZededaNetworkListDto.from_json(json)
# print the JSON string representation of the object
print(ZededaNetworkListDto.to_json())

# convert the object into a dict
zededa_network_list_dto_dict = zededa_network_list_dto_instance.to_dict()
# create an instance of ZededaNetworkListDto from a dict
zededa_network_list_dto_from_dict = ZededaNetworkListDto.from_dict(zededa_network_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



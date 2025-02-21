# CreateVsphereNetworkDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**gateway** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**net_mask** | **int** |  | [optional] 
**begin_allocation_range** | **str** |  | [optional] 
**end_allocation_range** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.create_vsphere_network_dto import CreateVsphereNetworkDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVsphereNetworkDto from a JSON string
create_vsphere_network_dto_instance = CreateVsphereNetworkDto.from_json(json)
# print the JSON string representation of the object
print(CreateVsphereNetworkDto.to_json())

# convert the object into a dict
create_vsphere_network_dto_dict = create_vsphere_network_dto_instance.to_dict()
# create an instance of CreateVsphereNetworkDto from a dict
create_vsphere_network_dto_from_dict = CreateVsphereNetworkDto.from_dict(create_vsphere_network_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



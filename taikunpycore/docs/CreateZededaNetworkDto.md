# CreateZededaNetworkDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **str** |  | [optional] 
**gateway** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**net_mask** | **int** |  | [optional] 
**vlan_id** | **int** |  | [optional] 
**begin_allocation_range** | **str** |  | [optional] 
**end_allocation_range** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.create_zededa_network_dto import CreateZededaNetworkDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateZededaNetworkDto from a JSON string
create_zededa_network_dto_instance = CreateZededaNetworkDto.from_json(json)
# print the JSON string representation of the object
print(CreateZededaNetworkDto.to_json())

# convert the object into a dict
create_zededa_network_dto_dict = create_zededa_network_dto_instance.to_dict()
# create an instance of CreateZededaNetworkDto from a dict
create_zededa_network_dto_from_dict = CreateZededaNetworkDto.from_dict(create_zededa_network_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



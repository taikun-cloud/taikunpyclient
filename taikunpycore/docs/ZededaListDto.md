# ZededaListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**project_count** | **int** |  | 
**is_locked** | **bool** |  | 
**name** | **str** |  | 
**projects** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**created_by** | **str** |  | 
**created_at** | **str** |  | 
**last_modified** | **str** |  | 
**last_modified_by** | **str** |  | 
**is_default** | **bool** |  | 
**organization_id** | **int** |  | 
**organization_name** | **str** |  | 
**continent_name** | **str** |  | 
**edge_nodes** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**api_token** | **str** |  | 
**api_url** | **str** |  | 
**project** | **str** |  | 
**project_id** | **str** |  | 
**zededa_networks** | [**List[ZededaNetworkListDto]**](ZededaNetworkListDto.md) |  | 

## Example

```python
from taikunpycore.models.zededa_list_dto import ZededaListDto

# TODO update the JSON string below
json = "{}"
# create an instance of ZededaListDto from a JSON string
zededa_list_dto_instance = ZededaListDto.from_json(json)
# print the JSON string representation of the object
print(ZededaListDto.to_json())

# convert the object into a dict
zededa_list_dto_dict = zededa_list_dto_instance.to_dict()
# create an instance of ZededaListDto from a dict
zededa_list_dto_from_dict = ZededaListDto.from_dict(zededa_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



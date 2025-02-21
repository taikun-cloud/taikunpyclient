# TanzuCredentialsListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**project_count** | **int** |  | 
**is_locked** | **bool** |  | 
**name** | **str** |  | 
**username** | **str** |  | 
**url** | **str** |  | 
**volume_type** | **str** |  | 
**namespace** | **str** |  | 
**port** | **int** |  | 
**projects** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**created_by** | **str** |  | 
**created_at** | **str** |  | 
**last_modified** | **str** |  | 
**last_modified_by** | **str** |  | 
**is_default** | **bool** |  | 
**organization_id** | **int** |  | 
**organization_name** | **str** |  | 
**continent_name** | **str** |  | 

## Example

```python
from taikunpycore.models.tanzu_credentials_list_dto import TanzuCredentialsListDto

# TODO update the JSON string below
json = "{}"
# create an instance of TanzuCredentialsListDto from a JSON string
tanzu_credentials_list_dto_instance = TanzuCredentialsListDto.from_json(json)
# print the JSON string representation of the object
print(TanzuCredentialsListDto.to_json())

# convert the object into a dict
tanzu_credentials_list_dto_dict = tanzu_credentials_list_dto_instance.to_dict()
# create an instance of TanzuCredentialsListDto from a dict
tanzu_credentials_list_dto_from_dict = TanzuCredentialsListDto.from_dict(tanzu_credentials_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



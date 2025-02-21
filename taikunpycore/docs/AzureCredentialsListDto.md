# AzureCredentialsListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**project_count** | **int** |  | 
**is_locked** | **bool** |  | 
**name** | **str** |  | 
**tenant_id** | **str** |  | 
**location** | **str** |  | 
**availability_zones** | **List[str]** |  | 
**availability_zones_count** | **int** |  | 
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
from taikunpycore.models.azure_credentials_list_dto import AzureCredentialsListDto

# TODO update the JSON string below
json = "{}"
# create an instance of AzureCredentialsListDto from a JSON string
azure_credentials_list_dto_instance = AzureCredentialsListDto.from_json(json)
# print the JSON string representation of the object
print(AzureCredentialsListDto.to_json())

# convert the object into a dict
azure_credentials_list_dto_dict = azure_credentials_list_dto_instance.to_dict()
# create an instance of AzureCredentialsListDto from a dict
azure_credentials_list_dto_from_dict = AzureCredentialsListDto.from_dict(azure_credentials_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



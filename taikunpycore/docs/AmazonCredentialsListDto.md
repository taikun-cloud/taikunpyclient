# AmazonCredentialsListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**project_count** | **int** |  | 
**is_locked** | **bool** |  | 
**name** | **str** |  | 
**region** | **str** |  | 
**availability_zones** | **List[str]** |  | 
**availability_zones_count** | **int** |  | 
**projects** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**created_by** | **str** |  | 
**last_modified** | **str** |  | 
**last_modified_by** | **str** |  | 
**is_default** | **bool** |  | 
**organization_id** | **int** |  | 
**organization_name** | **str** |  | 
**created_at** | **str** |  | 
**continent_name** | **str** |  | 

## Example

```python
from taikunpycore.models.amazon_credentials_list_dto import AmazonCredentialsListDto

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonCredentialsListDto from a JSON string
amazon_credentials_list_dto_instance = AmazonCredentialsListDto.from_json(json)
# print the JSON string representation of the object
print(AmazonCredentialsListDto.to_json())

# convert the object into a dict
amazon_credentials_list_dto_dict = amazon_credentials_list_dto_instance.to_dict()
# create an instance of AmazonCredentialsListDto from a dict
amazon_credentials_list_dto_from_dict = AmazonCredentialsListDto.from_dict(amazon_credentials_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



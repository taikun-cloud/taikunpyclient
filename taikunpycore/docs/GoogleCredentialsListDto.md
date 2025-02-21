# GoogleCredentialsListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**projects** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**organization_id** | **int** |  | 
**organization_name** | **str** |  | 
**partner_logo** | **str** |  | 
**partner_name** | **str** |  | 
**folder_id** | **str** |  | 
**project_id** | **str** |  | 
**billing_account_id** | **str** |  | 
**zones** | **List[str]** |  | 
**availability_zones_count** | **int** |  | 
**region** | **str** |  | 
**is_locked** | **bool** |  | 
**is_default** | **bool** |  | 
**billing_account_name** | **str** |  | 
**created_at** | **str** |  | 
**continent_name** | **str** |  | 

## Example

```python
from taikunpycore.models.google_credentials_list_dto import GoogleCredentialsListDto

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCredentialsListDto from a JSON string
google_credentials_list_dto_instance = GoogleCredentialsListDto.from_json(json)
# print the JSON string representation of the object
print(GoogleCredentialsListDto.to_json())

# convert the object into a dict
google_credentials_list_dto_dict = google_credentials_list_dto_instance.to_dict()
# create an instance of GoogleCredentialsListDto from a dict
google_credentials_list_dto_from_dict = GoogleCredentialsListDto.from_dict(google_credentials_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



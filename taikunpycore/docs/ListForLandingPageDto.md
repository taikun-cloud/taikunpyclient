# ListForLandingPageDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**project_limit** | **int** |  | 
**server_limit** | **int** |  | 
**user_limit** | **int** |  | 
**cloud_credential_limit** | **int** |  | 
**monthly_price** | **float** |  | 
**yearly_price** | **float** |  | 
**tcu_price** | **float** |  | 
**is_deprecated** | **bool** |  | 
**currency** | **str** |  | 
**partner_id** | **int** |  | 
**trial_days** | **int** |  | 
**description** | **str** |  | 
**is_free** | **bool** |  | 
**is_enterprise** | **bool** |  | 

## Example

```python
from taikunpycore.models.list_for_landing_page_dto import ListForLandingPageDto

# TODO update the JSON string below
json = "{}"
# create an instance of ListForLandingPageDto from a JSON string
list_for_landing_page_dto_instance = ListForLandingPageDto.from_json(json)
# print the JSON string representation of the object
print(ListForLandingPageDto.to_json())

# convert the object into a dict
list_for_landing_page_dto_dict = list_for_landing_page_dto_instance.to_dict()
# create an instance of ListForLandingPageDto from a dict
list_for_landing_page_dto_from_dict = ListForLandingPageDto.from_dict(list_for_landing_page_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ListForPartnersDto


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
**is_enterprise** | **bool** |  | 
**partner** | [**PartnerDetailsForSubscription**](PartnerDetailsForSubscription.md) |  | 
**exceeded_user** | **bool** |  | 
**exceeded_project** | **bool** |  | 
**exceeded_cloud_credential** | **bool** |  | 
**exceeded_servers** | **bool** |  | 
**is_active** | **bool** |  | 
**is_yearly** | **bool** |  | 
**trial_days** | **int** |  | 
**description** | **str** |  | 
**is_demo** | **bool** |  | 

## Example

```python
from taikunpycore.models.list_for_partners_dto import ListForPartnersDto

# TODO update the JSON string below
json = "{}"
# create an instance of ListForPartnersDto from a JSON string
list_for_partners_dto_instance = ListForPartnersDto.from_json(json)
# print the JSON string representation of the object
print(ListForPartnersDto.to_json())

# convert the object into a dict
list_for_partners_dto_dict = list_for_partners_dto_instance.to_dict()
# create an instance of ListForPartnersDto from a dict
list_for_partners_dto_from_dict = ListForPartnersDto.from_dict(list_for_partners_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



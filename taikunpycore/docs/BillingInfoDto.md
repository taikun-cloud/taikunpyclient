# BillingInfoDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | 
**vat_number** | **str** |  | 
**legal_name** | **str** |  | 
**city** | **str** |  | 
**billing_email** | **str** |  | 
**address** | **str** |  | 

## Example

```python
from taikunpycore.models.billing_info_dto import BillingInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of BillingInfoDto from a JSON string
billing_info_dto_instance = BillingInfoDto.from_json(json)
# print the JSON string representation of the object
print(BillingInfoDto.to_json())

# convert the object into a dict
billing_info_dto_dict = billing_info_dto_instance.to_dict()
# create an instance of BillingInfoDto from a dict
billing_info_dto_from_dict = BillingInfoDto.from_dict(billing_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



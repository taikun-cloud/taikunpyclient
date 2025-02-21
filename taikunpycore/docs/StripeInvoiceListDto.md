# StripeInvoiceListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**invoice_status** | **str** |  | 
**charge_status** | **str** |  | 
**charge_reason** | **str** |  | 
**price** | **float** |  | 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 

## Example

```python
from taikunpycore.models.stripe_invoice_list_dto import StripeInvoiceListDto

# TODO update the JSON string below
json = "{}"
# create an instance of StripeInvoiceListDto from a JSON string
stripe_invoice_list_dto_instance = StripeInvoiceListDto.from_json(json)
# print the JSON string representation of the object
print(StripeInvoiceListDto.to_json())

# convert the object into a dict
stripe_invoice_list_dto_dict = stripe_invoice_list_dto_instance.to_dict()
# create an instance of StripeInvoiceListDto from a dict
stripe_invoice_list_dto_from_dict = StripeInvoiceListDto.from_dict(stripe_invoice_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



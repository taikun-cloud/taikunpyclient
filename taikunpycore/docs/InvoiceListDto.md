# InvoiceListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**start_date** | **str** |  | 
**end_date** | **str** |  | 
**required_payment_action** | **bool** |  | 
**is_paid** | **bool** |  | 
**invoice_id** | **str** |  | 
**subscription_type** | **str** |  | 
**subscription_name** | **str** |  | 
**price** | **float** |  | 
**organization_id** | **int** |  | 
**organization_name** | **str** |  | 
**invoice_number** | **str** |  | 
**organization_subscription_id** | **int** |  | 

## Example

```python
from taikunpycore.models.invoice_list_dto import InvoiceListDto

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceListDto from a JSON string
invoice_list_dto_instance = InvoiceListDto.from_json(json)
# print the JSON string representation of the object
print(InvoiceListDto.to_json())

# convert the object into a dict
invoice_list_dto_dict = invoice_list_dto_instance.to_dict()
# create an instance of InvoiceListDto from a dict
invoice_list_dto_from_dict = InvoiceListDto.from_dict(invoice_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



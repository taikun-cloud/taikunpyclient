# InvoiceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**document_number** | **str** |  | 
**organization_subscription_id** | **int** |  | 
**is_paid** | **bool** |  | 
**required_payment_action** | **bool** |  | 
**stripe_invoice_id** | **str** |  | 
**price** | **float** |  | 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 
**due_date** | **datetime** |  | 

## Example

```python
from taikunpycore.models.invoice_dto import InvoiceDto

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDto from a JSON string
invoice_dto_instance = InvoiceDto.from_json(json)
# print the JSON string representation of the object
print(InvoiceDto.to_json())

# convert the object into a dict
invoice_dto_dict = invoice_dto_instance.to_dict()
# create an instance of InvoiceDto from a dict
invoice_dto_from_dict = InvoiceDto.from_dict(invoice_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



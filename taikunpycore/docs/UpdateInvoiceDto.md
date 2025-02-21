# UpdateInvoiceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**organization_subscription_id** | **int** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**is_paid** | **bool** |  | [optional] 
**required_payment_action** | **bool** |  | [optional] 
**stripe_invoice_id** | **str** |  | [optional] 
**price** | **float** |  | [optional] 

## Example

```python
from taikunpycore.models.update_invoice_dto import UpdateInvoiceDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInvoiceDto from a JSON string
update_invoice_dto_instance = UpdateInvoiceDto.from_json(json)
# print the JSON string representation of the object
print(UpdateInvoiceDto.to_json())

# convert the object into a dict
update_invoice_dto_dict = update_invoice_dto_instance.to_dict()
# create an instance of UpdateInvoiceDto from a dict
update_invoice_dto_from_dict = UpdateInvoiceDto.from_dict(update_invoice_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



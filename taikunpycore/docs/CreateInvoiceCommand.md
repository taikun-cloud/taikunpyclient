# CreateInvoiceCommand


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
from taikunpycore.models.create_invoice_command import CreateInvoiceCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceCommand from a JSON string
create_invoice_command_instance = CreateInvoiceCommand.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceCommand.to_json())

# convert the object into a dict
create_invoice_command_dict = create_invoice_command_instance.to_dict()
# create an instance of CreateInvoiceCommand from a dict
create_invoice_command_from_dict = CreateInvoiceCommand.from_dict(create_invoice_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



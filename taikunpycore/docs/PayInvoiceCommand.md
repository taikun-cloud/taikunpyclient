# PayInvoiceCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.pay_invoice_command import PayInvoiceCommand

# TODO update the JSON string below
json = "{}"
# create an instance of PayInvoiceCommand from a JSON string
pay_invoice_command_instance = PayInvoiceCommand.from_json(json)
# print the JSON string representation of the object
print(PayInvoiceCommand.to_json())

# convert the object into a dict
pay_invoice_command_dict = pay_invoice_command_instance.to_dict()
# create an instance of PayInvoiceCommand from a dict
pay_invoice_command_from_dict = PayInvoiceCommand.from_dict(pay_invoice_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



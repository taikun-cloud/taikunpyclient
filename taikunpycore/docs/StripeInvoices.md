# StripeInvoices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[StripeInvoiceListDto]**](StripeInvoiceListDto.md) |  | 

## Example

```python
from taikunpycore.models.stripe_invoices import StripeInvoices

# TODO update the JSON string below
json = "{}"
# create an instance of StripeInvoices from a JSON string
stripe_invoices_instance = StripeInvoices.from_json(json)
# print the JSON string representation of the object
print(StripeInvoices.to_json())

# convert the object into a dict
stripe_invoices_dict = stripe_invoices_instance.to_dict()
# create an instance of StripeInvoices from a dict
stripe_invoices_from_dict = StripeInvoices.from_dict(stripe_invoices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



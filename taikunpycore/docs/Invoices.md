# Invoices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InvoiceListDto]**](InvoiceListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.invoices import Invoices

# TODO update the JSON string below
json = "{}"
# create an instance of Invoices from a JSON string
invoices_instance = Invoices.from_json(json)
# print the JSON string representation of the object
print(Invoices.to_json())

# convert the object into a dict
invoices_dict = invoices_instance.to_dict()
# create an instance of Invoices from a dict
invoices_from_dict = Invoices.from_dict(invoices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



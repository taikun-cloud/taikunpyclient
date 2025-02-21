# DownloadInvoiceCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.download_invoice_command import DownloadInvoiceCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadInvoiceCommand from a JSON string
download_invoice_command_instance = DownloadInvoiceCommand.from_json(json)
# print the JSON string representation of the object
print(DownloadInvoiceCommand.to_json())

# convert the object into a dict
download_invoice_command_dict = download_invoice_command_instance.to_dict()
# create an instance of DownloadInvoiceCommand from a dict
download_invoice_command_from_dict = DownloadInvoiceCommand.from_dict(download_invoice_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateBillingSummaryCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icu** | **int** |  | [optional] 
**begin_apply** | **datetime** |  | [optional] 
**project_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.create_billing_summary_command import CreateBillingSummaryCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBillingSummaryCommand from a JSON string
create_billing_summary_command_instance = CreateBillingSummaryCommand.from_json(json)
# print the JSON string representation of the object
print(CreateBillingSummaryCommand.to_json())

# convert the object into a dict
create_billing_summary_command_dict = create_billing_summary_command_instance.to_dict()
# create an instance of CreateBillingSummaryCommand from a dict
create_billing_summary_command_from_dict = CreateBillingSummaryCommand.from_dict(create_billing_summary_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



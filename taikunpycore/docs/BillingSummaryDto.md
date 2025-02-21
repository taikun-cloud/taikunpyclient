# BillingSummaryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**project_name** | **str** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**tcu** | **float** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.billing_summary_dto import BillingSummaryDto

# TODO update the JSON string below
json = "{}"
# create an instance of BillingSummaryDto from a JSON string
billing_summary_dto_instance = BillingSummaryDto.from_json(json)
# print the JSON string representation of the object
print(BillingSummaryDto.to_json())

# convert the object into a dict
billing_summary_dto_dict = billing_summary_dto_instance.to_dict()
# create an instance of BillingSummaryDto from a dict
billing_summary_dto_from_dict = BillingSummaryDto.from_dict(billing_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



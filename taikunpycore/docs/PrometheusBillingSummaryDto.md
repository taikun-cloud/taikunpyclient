# PrometheusBillingSummaryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** |  | 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 
**prometheus_rule_id** | **int** |  | 
**rule_name** | **str** |  | 
**created_by** | **str** |  | 
**last_modified** | **str** |  | 
**last_modified_by** | **str** |  | 

## Example

```python
from taikunpycore.models.prometheus_billing_summary_dto import PrometheusBillingSummaryDto

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusBillingSummaryDto from a JSON string
prometheus_billing_summary_dto_instance = PrometheusBillingSummaryDto.from_json(json)
# print the JSON string representation of the object
print(PrometheusBillingSummaryDto.to_json())

# convert the object into a dict
prometheus_billing_summary_dto_dict = prometheus_billing_summary_dto_instance.to_dict()
# create an instance of PrometheusBillingSummaryDto from a dict
prometheus_billing_summary_dto_from_dict = PrometheusBillingSummaryDto.from_dict(prometheus_billing_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



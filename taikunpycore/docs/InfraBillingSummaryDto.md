# InfraBillingSummaryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infra_product_id** | **int** |  | [optional] 
**infra_product_name** | **str** |  | [optional] 
**intervals** | [**List[DateInterval]**](DateInterval.md) |  | [optional] 
**total_price** | **float** |  | [optional] 

## Example

```python
from taikunpycore.models.infra_billing_summary_dto import InfraBillingSummaryDto

# TODO update the JSON string below
json = "{}"
# create an instance of InfraBillingSummaryDto from a JSON string
infra_billing_summary_dto_instance = InfraBillingSummaryDto.from_json(json)
# print the JSON string representation of the object
print(InfraBillingSummaryDto.to_json())

# convert the object into a dict
infra_billing_summary_dto_dict = infra_billing_summary_dto_instance.to_dict()
# create an instance of InfraBillingSummaryDto from a dict
infra_billing_summary_dto_from_dict = InfraBillingSummaryDto.from_dict(infra_billing_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



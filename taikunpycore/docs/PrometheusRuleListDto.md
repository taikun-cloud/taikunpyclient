# PrometheusRuleListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**password** | **str** |  | 
**user_name** | **str** |  | 
**url** | **str** |  | 
**metric_name** | **str** |  | 
**labels** | [**List[PrometheusLabelListDto]**](PrometheusLabelListDto.md) |  | 
**bound_organizations** | [**List[PrometheusOrganizationDiscountDto]**](PrometheusOrganizationDiscountDto.md) |  | 
**type** | [**PrometheusType**](PrometheusType.md) |  | 
**price** | **float** |  | 
**billing_start_date** | **str** |  | 
**created_at** | **str** |  | 
**partner** | [**PartnerEntity**](PartnerEntity.md) |  | 
**operation_credential** | [**OperationCredentialsForOrganizationEntity**](OperationCredentialsForOrganizationEntity.md) |  | 
**created_by** | **str** |  | 
**last_modified** | **str** |  | 
**last_modified_by** | **str** |  | 

## Example

```python
from taikunpycore.models.prometheus_rule_list_dto import PrometheusRuleListDto

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusRuleListDto from a JSON string
prometheus_rule_list_dto_instance = PrometheusRuleListDto.from_json(json)
# print the JSON string representation of the object
print(PrometheusRuleListDto.to_json())

# convert the object into a dict
prometheus_rule_list_dto_dict = prometheus_rule_list_dto_instance.to_dict()
# create an instance of PrometheusRuleListDto from a dict
prometheus_rule_list_dto_from_dict = PrometheusRuleListDto.from_dict(prometheus_rule_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



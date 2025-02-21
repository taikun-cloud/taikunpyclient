# RuleForUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**metric_name** | **str** |  | [optional] 
**type** | [**PrometheusType**](PrometheusType.md) |  | [optional] 
**price** | **float** |  | [optional] 
**labels** | [**List[PrometheusLabelListDto]**](PrometheusLabelListDto.md) |  | [optional] 
**operation_credential_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.rule_for_update_dto import RuleForUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of RuleForUpdateDto from a JSON string
rule_for_update_dto_instance = RuleForUpdateDto.from_json(json)
# print the JSON string representation of the object
print(RuleForUpdateDto.to_json())

# convert the object into a dict
rule_for_update_dto_dict = rule_for_update_dto_instance.to_dict()
# create an instance of RuleForUpdateDto from a dict
rule_for_update_dto_from_dict = RuleForUpdateDto.from_dict(rule_for_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



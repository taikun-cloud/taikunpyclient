# RuleCreateCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**metric_name** | **str** |  | [optional] 
**labels** | [**List[PrometheusLabelListDto]**](PrometheusLabelListDto.md) |  | [optional] 
**type** | [**PrometheusType**](PrometheusType.md) |  | [optional] 
**price** | **float** |  | [optional] 
**partner_id** | **int** |  | [optional] 
**operation_credential_id** | **int** |  | [optional] 
**organization_id** | **List[int]** |  | [optional] 
**rule_discount_rate** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.rule_create_command import RuleCreateCommand

# TODO update the JSON string below
json = "{}"
# create an instance of RuleCreateCommand from a JSON string
rule_create_command_instance = RuleCreateCommand.from_json(json)
# print the JSON string representation of the object
print(RuleCreateCommand.to_json())

# convert the object into a dict
rule_create_command_dict = rule_create_command_instance.to_dict()
# create an instance of RuleCreateCommand from a dict
rule_create_command_from_dict = RuleCreateCommand.from_dict(rule_create_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Rule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**query** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**labels** | [**RuleLabels**](RuleLabels.md) |  | [optional] 
**annotations** | [**Annotations**](Annotations.md) |  | [optional] 
**alerts** | [**List[Alert]**](Alert.md) |  | [optional] 
**health** | **str** |  | [optional] 
**evaluation_time** | **float** |  | [optional] 
**last_evaluation** | **datetime** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.rule import Rule

# TODO update the JSON string below
json = "{}"
# create an instance of Rule from a JSON string
rule_instance = Rule.from_json(json)
# print the JSON string representation of the object
print(Rule.to_json())

# convert the object into a dict
rule_dict = rule_instance.to_dict()
# create an instance of Rule from a dict
rule_from_dict = Rule.from_dict(rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



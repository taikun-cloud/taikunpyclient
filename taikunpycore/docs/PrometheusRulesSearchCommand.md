# PrometheusRulesSearchCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_term** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.prometheus_rules_search_command import PrometheusRulesSearchCommand

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusRulesSearchCommand from a JSON string
prometheus_rules_search_command_instance = PrometheusRulesSearchCommand.from_json(json)
# print the JSON string representation of the object
print(PrometheusRulesSearchCommand.to_json())

# convert the object into a dict
prometheus_rules_search_command_dict = prometheus_rules_search_command_instance.to_dict()
# create an instance of PrometheusRulesSearchCommand from a dict
prometheus_rules_search_command_from_dict = PrometheusRulesSearchCommand.from_dict(prometheus_rules_search_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



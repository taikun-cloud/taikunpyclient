# PrometheusRulesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PrometheusRuleListDto]**](PrometheusRuleListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.prometheus_rules_list import PrometheusRulesList

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusRulesList from a JSON string
prometheus_rules_list_instance = PrometheusRulesList.from_json(json)
# print the JSON string representation of the object
print(PrometheusRulesList.to_json())

# convert the object into a dict
prometheus_rules_list_dict = prometheus_rules_list_instance.to_dict()
# create an instance of PrometheusRulesList from a dict
prometheus_rules_list_from_dict = PrometheusRulesList.from_dict(prometheus_rules_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



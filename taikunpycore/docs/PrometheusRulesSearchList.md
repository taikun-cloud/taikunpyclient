# PrometheusRulesSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PrometheusRulesSearchResponseData]**](PrometheusRulesSearchResponseData.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.prometheus_rules_search_list import PrometheusRulesSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusRulesSearchList from a JSON string
prometheus_rules_search_list_instance = PrometheusRulesSearchList.from_json(json)
# print the JSON string representation of the object
print(PrometheusRulesSearchList.to_json())

# convert the object into a dict
prometheus_rules_search_list_dict = prometheus_rules_search_list_instance.to_dict()
# create an instance of PrometheusRulesSearchList from a dict
prometheus_rules_search_list_from_dict = PrometheusRulesSearchList.from_dict(prometheus_rules_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



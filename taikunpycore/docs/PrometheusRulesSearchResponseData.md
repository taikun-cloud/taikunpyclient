# PrometheusRulesSearchResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**partner** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.prometheus_rules_search_response_data import PrometheusRulesSearchResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusRulesSearchResponseData from a JSON string
prometheus_rules_search_response_data_instance = PrometheusRulesSearchResponseData.from_json(json)
# print the JSON string representation of the object
print(PrometheusRulesSearchResponseData.to_json())

# convert the object into a dict
prometheus_rules_search_response_data_dict = prometheus_rules_search_response_data_instance.to_dict()
# create an instance of PrometheusRulesSearchResponseData from a dict
prometheus_rules_search_response_data_from_dict = PrometheusRulesSearchResponseData.from_dict(prometheus_rules_search_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



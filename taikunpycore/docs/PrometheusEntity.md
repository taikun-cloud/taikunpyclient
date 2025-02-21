# PrometheusEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prometheus_rule_id** | **int** |  | 
**prometheus_rule_name** | **str** |  | 
**rule_discount_rate** | **float** |  | 

## Example

```python
from taikunpycore.models.prometheus_entity import PrometheusEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusEntity from a JSON string
prometheus_entity_instance = PrometheusEntity.from_json(json)
# print the JSON string representation of the object
print(PrometheusEntity.to_json())

# convert the object into a dict
prometheus_entity_dict = prometheus_entity_instance.to_dict()
# create an instance of PrometheusEntity from a dict
prometheus_entity_from_dict = PrometheusEntity.from_dict(prometheus_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



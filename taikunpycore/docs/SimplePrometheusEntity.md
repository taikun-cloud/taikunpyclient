# SimplePrometheusEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prometheus_rule_id** | **int** |  | 
**prometheus_rule_name** | **str** |  | 

## Example

```python
from taikunpycore.models.simple_prometheus_entity import SimplePrometheusEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SimplePrometheusEntity from a JSON string
simple_prometheus_entity_instance = SimplePrometheusEntity.from_json(json)
# print the JSON string representation of the object
print(SimplePrometheusEntity.to_json())

# convert the object into a dict
simple_prometheus_entity_dict = simple_prometheus_entity_instance.to_dict()
# create an instance of SimplePrometheusEntity from a dict
simple_prometheus_entity_from_dict = SimplePrometheusEntity.from_dict(simple_prometheus_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



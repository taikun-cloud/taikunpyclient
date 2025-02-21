# PrometheusMetricsCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**parameters** | **str** |  | [optional] 
**time** | **datetime** |  | [optional] 
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**is_graph_enabled** | **bool** |  | [optional] 
**step** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.prometheus_metrics_command import PrometheusMetricsCommand

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusMetricsCommand from a JSON string
prometheus_metrics_command_instance = PrometheusMetricsCommand.from_json(json)
# print the JSON string representation of the object
print(PrometheusMetricsCommand.to_json())

# convert the object into a dict
prometheus_metrics_command_dict = prometheus_metrics_command_instance.to_dict()
# create an instance of PrometheusMetricsCommand from a dict
prometheus_metrics_command_from_dict = PrometheusMetricsCommand.from_dict(prometheus_metrics_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PrometheusMetricListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**MetricData**](MetricData.md) |  | [optional] 

## Example

```python
from taikunpycore.models.prometheus_metric_list_dto import PrometheusMetricListDto

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusMetricListDto from a JSON string
prometheus_metric_list_dto_instance = PrometheusMetricListDto.from_json(json)
# print the JSON string representation of the object
print(PrometheusMetricListDto.to_json())

# convert the object into a dict
prometheus_metric_list_dto_dict = prometheus_metric_list_dto_instance.to_dict()
# create an instance of PrometheusMetricListDto from a dict
prometheus_metric_list_dto_from_dict = PrometheusMetricListDto.from_dict(prometheus_metric_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



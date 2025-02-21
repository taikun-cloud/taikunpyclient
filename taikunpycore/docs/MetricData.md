# MetricData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_type** | **str** |  | [optional] 
**result** | [**List[MetricResult]**](MetricResult.md) |  | [optional] 

## Example

```python
from taikunpycore.models.metric_data import MetricData

# TODO update the JSON string below
json = "{}"
# create an instance of MetricData from a JSON string
metric_data_instance = MetricData.from_json(json)
# print the JSON string representation of the object
print(MetricData.to_json())

# convert the object into a dict
metric_data_dict = metric_data_instance.to_dict()
# create an instance of MetricData from a dict
metric_data_from_dict = MetricData.from_dict(metric_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



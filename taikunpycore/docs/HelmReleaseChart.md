# HelmReleaseChart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**HelmReleaseChartSpec**](HelmReleaseChartSpec.md) |  | [optional] 

## Example

```python
from taikunpycore.models.helm_release_chart import HelmReleaseChart

# TODO update the JSON string below
json = "{}"
# create an instance of HelmReleaseChart from a JSON string
helm_release_chart_instance = HelmReleaseChart.from_json(json)
# print the JSON string representation of the object
print(HelmReleaseChart.to_json())

# convert the object into a dict
helm_release_chart_dict = helm_release_chart_instance.to_dict()
# create an instance of HelmReleaseChart from a dict
helm_release_chart_from_dict = HelmReleaseChart.from_dict(helm_release_chart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



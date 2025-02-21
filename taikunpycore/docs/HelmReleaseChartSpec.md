# HelmReleaseChartSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**source_ref** | [**HelmReleaseSourceRef**](HelmReleaseSourceRef.md) |  | [optional] 

## Example

```python
from taikunpycore.models.helm_release_chart_spec import HelmReleaseChartSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HelmReleaseChartSpec from a JSON string
helm_release_chart_spec_instance = HelmReleaseChartSpec.from_json(json)
# print the JSON string representation of the object
print(HelmReleaseChartSpec.to_json())

# convert the object into a dict
helm_release_chart_spec_dict = helm_release_chart_spec_instance.to_dict()
# create an instance of HelmReleaseChartSpec from a dict
helm_release_chart_spec_from_dict = HelmReleaseChartSpec.from_dict(helm_release_chart_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



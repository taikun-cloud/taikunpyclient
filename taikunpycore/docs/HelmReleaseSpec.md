# HelmReleaseSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_namespace** | **str** |  | [optional] 
**chart** | [**HelmReleaseChart**](HelmReleaseChart.md) |  | [optional] 

## Example

```python
from taikunpycore.models.helm_release_spec import HelmReleaseSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HelmReleaseSpec from a JSON string
helm_release_spec_instance = HelmReleaseSpec.from_json(json)
# print the JSON string representation of the object
print(HelmReleaseSpec.to_json())

# convert the object into a dict
helm_release_spec_dict = helm_release_spec_instance.to_dict()
# create an instance of HelmReleaseSpec from a dict
helm_release_spec_from_dict = HelmReleaseSpec.from_dict(helm_release_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



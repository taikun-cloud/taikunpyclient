# HelmReleaseSourceRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.helm_release_source_ref import HelmReleaseSourceRef

# TODO update the JSON string below
json = "{}"
# create an instance of HelmReleaseSourceRef from a JSON string
helm_release_source_ref_instance = HelmReleaseSourceRef.from_json(json)
# print the JSON string representation of the object
print(HelmReleaseSourceRef.to_json())

# convert the object into a dict
helm_release_source_ref_dict = helm_release_source_ref_instance.to_dict()
# create an instance of HelmReleaseSourceRef from a dict
helm_release_source_ref_from_dict = HelmReleaseSourceRef.from_dict(helm_release_source_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



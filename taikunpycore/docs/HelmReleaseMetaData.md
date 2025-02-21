# HelmReleaseMetaData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_timestamp** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.helm_release_meta_data import HelmReleaseMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of HelmReleaseMetaData from a JSON string
helm_release_meta_data_instance = HelmReleaseMetaData.from_json(json)
# print the JSON string representation of the object
print(HelmReleaseMetaData.to_json())

# convert the object into a dict
helm_release_meta_data_dict = helm_release_meta_data_instance.to_dict()
# create an instance of HelmReleaseMetaData from a dict
helm_release_meta_data_from_dict = HelmReleaseMetaData.from_dict(helm_release_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# HelmReleaseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**metadata** | [**HelmReleaseMetaData**](HelmReleaseMetaData.md) |  | [optional] 
**spec** | [**HelmReleaseSpec**](HelmReleaseSpec.md) |  | [optional] 
**status** | [**HelmStatus**](HelmStatus.md) |  | [optional] 

## Example

```python
from taikunpycore.models.helm_release_dto import HelmReleaseDto

# TODO update the JSON string below
json = "{}"
# create an instance of HelmReleaseDto from a JSON string
helm_release_dto_instance = HelmReleaseDto.from_json(json)
# print the JSON string representation of the object
print(HelmReleaseDto.to_json())

# convert the object into a dict
helm_release_dto_dict = helm_release_dto_instance.to_dict()
# create an instance of HelmReleaseDto from a dict
helm_release_dto_from_dict = HelmReleaseDto.from_dict(helm_release_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



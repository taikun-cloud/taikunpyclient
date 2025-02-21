# HelmReleasesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[HelmReleaseDto]**](HelmReleaseDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.helm_releases_list import HelmReleasesList

# TODO update the JSON string below
json = "{}"
# create an instance of HelmReleasesList from a JSON string
helm_releases_list_instance = HelmReleasesList.from_json(json)
# print the JSON string representation of the object
print(HelmReleasesList.to_json())

# convert the object into a dict
helm_releases_list_dict = helm_releases_list_instance.to_dict()
# create an instance of HelmReleasesList from a dict
helm_releases_list_from_dict = HelmReleasesList.from_dict(helm_releases_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



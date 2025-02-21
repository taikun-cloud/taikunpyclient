# PodDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_name** | **str** |  | 
**status** | **str** |  | 
**restart_count** | **int** |  | 
**namespace** | **str** |  | 
**age** | **datetime** |  | 
**node** | **str** |  | 
**phase** | **str** |  | 

## Example

```python
from taikunpycore.models.pod_dto import PodDto

# TODO update the JSON string below
json = "{}"
# create an instance of PodDto from a JSON string
pod_dto_instance = PodDto.from_json(json)
# print the JSON string representation of the object
print(PodDto.to_json())

# convert the object into a dict
pod_dto_dict = pod_dto_instance.to_dict()
# create an instance of PodDto from a dict
pod_dto_from_dict = PodDto.from_dict(pod_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



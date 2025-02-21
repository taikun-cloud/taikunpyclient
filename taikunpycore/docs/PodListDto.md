# PodListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_name** | **str** |  | 
**restart_count** | **int** |  | 
**namespace** | **str** |  | 
**node** | **str** |  | 
**age** | **str** |  | 
**status** | **str** |  | [optional] 
**container** | **List[str]** |  | 
**state** | [**KubernetesStateDto**](KubernetesStateDto.md) |  | [optional] 
**type** | **object** |  | [optional] 

## Example

```python
from taikunpycore.models.pod_list_dto import PodListDto

# TODO update the JSON string below
json = "{}"
# create an instance of PodListDto from a JSON string
pod_list_dto_instance = PodListDto.from_json(json)
# print the JSON string representation of the object
print(PodListDto.to_json())

# convert the object into a dict
pod_list_dto_dict = pod_list_dto_instance.to_dict()
# create an instance of PodListDto from a dict
pod_list_dto_from_dict = PodListDto.from_dict(pod_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



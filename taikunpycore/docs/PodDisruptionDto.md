# PodDisruptionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**namespace** | **str** |  | 
**min_available** | **object** |  | 
**max_available** | **object** |  | 
**allowed_disruptions** | **object** |  | 
**created_at** | **str** |  | 

## Example

```python
from taikunpycore.models.pod_disruption_dto import PodDisruptionDto

# TODO update the JSON string below
json = "{}"
# create an instance of PodDisruptionDto from a JSON string
pod_disruption_dto_instance = PodDisruptionDto.from_json(json)
# print the JSON string representation of the object
print(PodDisruptionDto.to_json())

# convert the object into a dict
pod_disruption_dto_dict = pod_disruption_dto_instance.to_dict()
# create an instance of PodDisruptionDto from a dict
pod_disruption_dto_from_dict = PodDisruptionDto.from_dict(pod_disruption_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PodDisruptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PodDisruptionDto]**](PodDisruptionDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.pod_disruptions import PodDisruptions

# TODO update the JSON string below
json = "{}"
# create an instance of PodDisruptions from a JSON string
pod_disruptions_instance = PodDisruptions.from_json(json)
# print the JSON string representation of the object
print(PodDisruptions.to_json())

# convert the object into a dict
pod_disruptions_dict = pod_disruptions_instance.to_dict()
# create an instance of PodDisruptions from a dict
pod_disruptions_from_dict = PodDisruptions.from_dict(pod_disruptions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



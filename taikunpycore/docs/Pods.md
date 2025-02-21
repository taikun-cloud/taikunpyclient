# Pods


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PodListDto]**](PodListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.pods import Pods

# TODO update the JSON string below
json = "{}"
# create an instance of Pods from a JSON string
pods_instance = Pods.from_json(json)
# print the JSON string representation of the object
print(Pods.to_json())

# convert the object into a dict
pods_dict = pods_instance.to_dict()
# create an instance of Pods from a dict
pods_from_dict = Pods.from_dict(pods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



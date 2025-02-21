# DaemonSets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DaemonSetDto]**](DaemonSetDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.daemon_sets import DaemonSets

# TODO update the JSON string below
json = "{}"
# create an instance of DaemonSets from a JSON string
daemon_sets_instance = DaemonSets.from_json(json)
# print the JSON string representation of the object
print(DaemonSets.to_json())

# convert the object into a dict
daemon_sets_dict = daemon_sets_instance.to_dict()
# create an instance of DaemonSets from a dict
daemon_sets_from_dict = DaemonSets.from_dict(daemon_sets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



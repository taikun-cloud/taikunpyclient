# DaemonSetDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_name** | **str** |  | 
**status** | **str** |  | 
**namespace** | **str** |  | 
**age** | **str** |  | 

## Example

```python
from taikunpycore.models.daemon_set_dto import DaemonSetDto

# TODO update the JSON string below
json = "{}"
# create an instance of DaemonSetDto from a JSON string
daemon_set_dto_instance = DaemonSetDto.from_json(json)
# print the JSON string representation of the object
print(DaemonSetDto.to_json())

# convert the object into a dict
daemon_set_dto_dict = daemon_set_dto_instance.to_dict()
# create an instance of DaemonSetDto from a dict
daemon_set_dto_from_dict = DaemonSetDto.from_dict(daemon_set_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



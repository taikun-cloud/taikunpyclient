# EnableAutoscalingCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**autoscaling_group_name** | **str** |  | [optional] 
**min_size** | **int** |  | [optional] 
**max_size** | **int** |  | [optional] 
**disk_size** | **float** |  | [optional] 
**flavor** | **str** |  | [optional] 
**spot_enabled** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.enable_autoscaling_command import EnableAutoscalingCommand

# TODO update the JSON string below
json = "{}"
# create an instance of EnableAutoscalingCommand from a JSON string
enable_autoscaling_command_instance = EnableAutoscalingCommand.from_json(json)
# print the JSON string representation of the object
print(EnableAutoscalingCommand.to_json())

# convert the object into a dict
enable_autoscaling_command_dict = enable_autoscaling_command_instance.to_dict()
# create an instance of EnableAutoscalingCommand from a dict
enable_autoscaling_command_from_dict = EnableAutoscalingCommand.from_dict(enable_autoscaling_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



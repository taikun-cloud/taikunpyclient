# UpdateExecutorHealthStatusCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executor_id** | **int** |  | [optional] 
**health** | [**ExecutorHealth**](ExecutorHealth.md) |  | [optional] 

## Example

```python
from taikunpycore.models.update_executor_health_status_command import UpdateExecutorHealthStatusCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateExecutorHealthStatusCommand from a JSON string
update_executor_health_status_command_instance = UpdateExecutorHealthStatusCommand.from_json(json)
# print the JSON string representation of the object
print(UpdateExecutorHealthStatusCommand.to_json())

# convert the object into a dict
update_executor_health_status_command_dict = update_executor_health_status_command_instance.to_dict()
# create an instance of UpdateExecutorHealthStatusCommand from a dict
update_executor_health_status_command_from_dict = UpdateExecutorHealthStatusCommand.from_dict(update_executor_health_status_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



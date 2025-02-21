# UpdateHealthStatusCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**health** | [**ProjectHealth**](ProjectHealth.md) |  | [optional] 

## Example

```python
from taikunpycore.models.update_health_status_command import UpdateHealthStatusCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHealthStatusCommand from a JSON string
update_health_status_command_instance = UpdateHealthStatusCommand.from_json(json)
# print the JSON string representation of the object
print(UpdateHealthStatusCommand.to_json())

# convert the object into a dict
update_health_status_command_dict = update_health_status_command_instance.to_dict()
# create an instance of UpdateHealthStatusCommand from a dict
update_health_status_command_from_dict = UpdateHealthStatusCommand.from_dict(update_health_status_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



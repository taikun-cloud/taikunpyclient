# ResetServerStatusCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**server_ids** | **List[int]** |  | [optional] 
**status** | [**CloudStatus**](CloudStatus.md) |  | [optional] 

## Example

```python
from taikunpycore.models.reset_server_status_command import ResetServerStatusCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ResetServerStatusCommand from a JSON string
reset_server_status_command_instance = ResetServerStatusCommand.from_json(json)
# print the JSON string representation of the object
print(ResetServerStatusCommand.to_json())

# convert the object into a dict
reset_server_status_command_dict = reset_server_status_command_instance.to_dict()
# create an instance of ResetServerStatusCommand from a dict
reset_server_status_command_from_dict = ResetServerStatusCommand.from_dict(reset_server_status_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



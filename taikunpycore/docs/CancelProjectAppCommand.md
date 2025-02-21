# CancelProjectAppCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_app_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.cancel_project_app_command import CancelProjectAppCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CancelProjectAppCommand from a JSON string
cancel_project_app_command_instance = CancelProjectAppCommand.from_json(json)
# print the JSON string representation of the object
print(CancelProjectAppCommand.to_json())

# convert the object into a dict
cancel_project_app_command_dict = cancel_project_app_command_instance.to_dict()
# create an instance of CancelProjectAppCommand from a dict
cancel_project_app_command_from_dict = CancelProjectAppCommand.from_dict(cancel_project_app_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



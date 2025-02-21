# CronjobActionCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | 
**name** | **str** |  | 
**namespace** | **str** |  | 
**action** | [**ECronJobAction**](ECronJobAction.md) |  | 

## Example

```python
from taikunpycore.models.cronjob_action_command import CronjobActionCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CronjobActionCommand from a JSON string
cronjob_action_command_instance = CronjobActionCommand.from_json(json)
# print the JSON string representation of the object
print(CronjobActionCommand.to_json())

# convert the object into a dict
cronjob_action_command_dict = cronjob_action_command_instance.to_dict()
# create an instance of CronjobActionCommand from a dict
cronjob_action_command_from_dict = CronjobActionCommand.from_dict(cronjob_action_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



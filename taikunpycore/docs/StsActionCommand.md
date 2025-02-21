# StsActionCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | 
**name** | **str** |  | 
**namespace** | **str** |  | 
**scale_replica_count** | **int** |  | [optional] 
**action** | [**EStsAction**](EStsAction.md) |  | 

## Example

```python
from taikunpycore.models.sts_action_command import StsActionCommand

# TODO update the JSON string below
json = "{}"
# create an instance of StsActionCommand from a JSON string
sts_action_command_instance = StsActionCommand.from_json(json)
# print the JSON string representation of the object
print(StsActionCommand.to_json())

# convert the object into a dict
sts_action_command_dict = sts_action_command_instance.to_dict()
# create an instance of StsActionCommand from a dict
sts_action_command_from_dict = StsActionCommand.from_dict(sts_action_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# NotifyOwnersCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.notify_owners_command import NotifyOwnersCommand

# TODO update the JSON string below
json = "{}"
# create an instance of NotifyOwnersCommand from a JSON string
notify_owners_command_instance = NotifyOwnersCommand.from_json(json)
# print the JSON string representation of the object
print(NotifyOwnersCommand.to_json())

# convert the object into a dict
notify_owners_command_dict = notify_owners_command_instance.to_dict()
# create an instance of NotifyOwnersCommand from a dict
notify_owners_command_from_dict = NotifyOwnersCommand.from_dict(notify_owners_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



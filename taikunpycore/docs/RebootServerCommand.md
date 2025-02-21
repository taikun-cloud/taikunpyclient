# RebootServerCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.reboot_server_command import RebootServerCommand

# TODO update the JSON string below
json = "{}"
# create an instance of RebootServerCommand from a JSON string
reboot_server_command_instance = RebootServerCommand.from_json(json)
# print the JSON string representation of the object
print(RebootServerCommand.to_json())

# convert the object into a dict
reboot_server_command_dict = reboot_server_command_instance.to_dict()
# create an instance of RebootServerCommand from a dict
reboot_server_command_from_dict = RebootServerCommand.from_dict(reboot_server_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



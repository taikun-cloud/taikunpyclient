# VmConsoleScreenshotCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.vm_console_screenshot_command import VmConsoleScreenshotCommand

# TODO update the JSON string below
json = "{}"
# create an instance of VmConsoleScreenshotCommand from a JSON string
vm_console_screenshot_command_instance = VmConsoleScreenshotCommand.from_json(json)
# print the JSON string representation of the object
print(VmConsoleScreenshotCommand.to_json())

# convert the object into a dict
vm_console_screenshot_command_dict = vm_console_screenshot_command_instance.to_dict()
# create an instance of VmConsoleScreenshotCommand from a dict
vm_console_screenshot_command_from_dict = VmConsoleScreenshotCommand.from_dict(vm_console_screenshot_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



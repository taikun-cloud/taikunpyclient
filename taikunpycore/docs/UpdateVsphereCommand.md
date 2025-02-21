# UpdateVsphereCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.update_vsphere_command import UpdateVsphereCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVsphereCommand from a JSON string
update_vsphere_command_instance = UpdateVsphereCommand.from_json(json)
# print the JSON string representation of the object
print(UpdateVsphereCommand.to_json())

# convert the object into a dict
update_vsphere_command_dict = update_vsphere_command_instance.to_dict()
# create an instance of UpdateVsphereCommand from a dict
update_vsphere_command_from_dict = UpdateVsphereCommand.from_dict(update_vsphere_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



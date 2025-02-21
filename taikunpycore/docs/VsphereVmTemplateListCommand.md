# VsphereVmTemplateListCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**datacenter_id** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.vsphere_vm_template_list_command import VsphereVmTemplateListCommand

# TODO update the JSON string below
json = "{}"
# create an instance of VsphereVmTemplateListCommand from a JSON string
vsphere_vm_template_list_command_instance = VsphereVmTemplateListCommand.from_json(json)
# print the JSON string representation of the object
print(VsphereVmTemplateListCommand.to_json())

# convert the object into a dict
vsphere_vm_template_list_command_dict = vsphere_vm_template_list_command_instance.to_dict()
# create an instance of VsphereVmTemplateListCommand from a dict
vsphere_vm_template_list_command_from_dict = VsphereVmTemplateListCommand.from_dict(vsphere_vm_template_list_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



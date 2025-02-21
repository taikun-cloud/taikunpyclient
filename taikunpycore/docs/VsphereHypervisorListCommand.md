# VsphereHypervisorListCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**datacenter_id** | **str** |  | [optional] 
**cloud_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.vsphere_hypervisor_list_command import VsphereHypervisorListCommand

# TODO update the JSON string below
json = "{}"
# create an instance of VsphereHypervisorListCommand from a JSON string
vsphere_hypervisor_list_command_instance = VsphereHypervisorListCommand.from_json(json)
# print the JSON string representation of the object
print(VsphereHypervisorListCommand.to_json())

# convert the object into a dict
vsphere_hypervisor_list_command_dict = vsphere_hypervisor_list_command_instance.to_dict()
# create an instance of VsphereHypervisorListCommand from a dict
vsphere_hypervisor_list_command_from_dict = VsphereHypervisorListCommand.from_dict(vsphere_hypervisor_list_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



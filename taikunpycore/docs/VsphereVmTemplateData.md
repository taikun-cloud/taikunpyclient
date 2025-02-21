# VsphereVmTemplateData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**uuid** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.vsphere_vm_template_data import VsphereVmTemplateData

# TODO update the JSON string below
json = "{}"
# create an instance of VsphereVmTemplateData from a JSON string
vsphere_vm_template_data_instance = VsphereVmTemplateData.from_json(json)
# print the JSON string representation of the object
print(VsphereVmTemplateData.to_json())

# convert the object into a dict
vsphere_vm_template_data_dict = vsphere_vm_template_data_instance.to_dict()
# create an instance of VsphereVmTemplateData from a dict
vsphere_vm_template_data_from_dict = VsphereVmTemplateData.from_dict(vsphere_vm_template_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



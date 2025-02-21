# VmTemplateListCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_id** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**token_id** | **str** |  | [optional] 
**token_secret** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.vm_template_list_command import VmTemplateListCommand

# TODO update the JSON string below
json = "{}"
# create an instance of VmTemplateListCommand from a JSON string
vm_template_list_command_instance = VmTemplateListCommand.from_json(json)
# print the JSON string representation of the object
print(VmTemplateListCommand.to_json())

# convert the object into a dict
vm_template_list_command_dict = vm_template_list_command_instance.to_dict()
# create an instance of VmTemplateListCommand from a dict
vm_template_list_command_from_dict = VmTemplateListCommand.from_dict(vm_template_list_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



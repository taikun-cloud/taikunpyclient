# CheckOpenstackCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_stack_user** | **str** |  | [optional] 
**open_stack_password** | **str** |  | [optional] 
**open_stack_url** | **str** |  | [optional] 
**open_stack_domain** | **str** |  | [optional] 
**is_admin** | **bool** |  | [optional] 
**application_cred_enabled** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.check_openstack_command import CheckOpenstackCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CheckOpenstackCommand from a JSON string
check_openstack_command_instance = CheckOpenstackCommand.from_json(json)
# print the JSON string representation of the object
print(CheckOpenstackCommand.to_json())

# convert the object into a dict
check_openstack_command_dict = check_openstack_command_instance.to_dict()
# create an instance of CheckOpenstackCommand from a dict
check_openstack_command_from_dict = CheckOpenstackCommand.from_dict(check_openstack_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



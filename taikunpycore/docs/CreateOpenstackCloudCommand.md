# CreateOpenstackCloudCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**open_stack_user** | **str** |  | [optional] 
**open_stack_password** | **str** |  | [optional] 
**open_stack_url** | **str** |  | [optional] 
**open_stack_project** | **str** |  | [optional] 
**open_stack_public_network** | **str** |  | [optional] 
**open_stack_availability_zone** | **str** |  | [optional] 
**open_stack_domain** | **str** |  | [optional] 
**open_stack_region** | **str** |  | [optional] 
**open_stack_continent** | **str** |  | [optional] 
**open_stack_volume_type** | **str** |  | [optional] 
**open_stack_import_network** | **bool** |  | [optional] 
**open_stack_internal_subnet_id** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**application_cred_enabled** | **bool** |  | [optional] 
**is_admin** | **bool** |  | [optional] 
**skip_tls_flag** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.create_openstack_cloud_command import CreateOpenstackCloudCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOpenstackCloudCommand from a JSON string
create_openstack_cloud_command_instance = CreateOpenstackCloudCommand.from_json(json)
# print the JSON string representation of the object
print(CreateOpenstackCloudCommand.to_json())

# convert the object into a dict
create_openstack_cloud_command_dict = create_openstack_cloud_command_instance.to_dict()
# create an instance of CreateOpenstackCloudCommand from a dict
create_openstack_cloud_command_from_dict = CreateOpenstackCloudCommand.from_dict(create_openstack_cloud_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



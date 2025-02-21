# OpenstackVolumeTypeListQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**open_stack_user** | **str** |  | [optional] 
**open_stack_password** | **str** |  | [optional] 
**open_stack_url** | **str** |  | [optional] 
**open_stack_domain** | **str** |  | [optional] 
**open_stack_region** | **str** |  | [optional] 
**application_cred_enabled** | **bool** |  | [optional] 
**is_admin** | **bool** |  | [optional] 
**openstack_project** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.openstack_volume_type_list_query import OpenstackVolumeTypeListQuery

# TODO update the JSON string below
json = "{}"
# create an instance of OpenstackVolumeTypeListQuery from a JSON string
openstack_volume_type_list_query_instance = OpenstackVolumeTypeListQuery.from_json(json)
# print the JSON string representation of the object
print(OpenstackVolumeTypeListQuery.to_json())

# convert the object into a dict
openstack_volume_type_list_query_dict = openstack_volume_type_list_query_instance.to_dict()
# create an instance of OpenstackVolumeTypeListQuery from a dict
openstack_volume_type_list_query_from_dict = OpenstackVolumeTypeListQuery.from_dict(openstack_volume_type_list_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



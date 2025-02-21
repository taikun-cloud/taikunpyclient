# OpenstackSubnetListQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_stack_user** | **str** |  | [optional] 
**open_stack_password** | **str** |  | [optional] 
**open_stack_url** | **str** |  | [optional] 
**open_stack_project** | **str** |  | [optional] 
**open_stack_project_id** | **str** |  | [optional] 
**open_stack_domain** | **str** |  | [optional] 
**open_stack_region** | **str** |  | [optional] 
**application_cred_enabled** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.openstack_subnet_list_query import OpenstackSubnetListQuery

# TODO update the JSON string below
json = "{}"
# create an instance of OpenstackSubnetListQuery from a JSON string
openstack_subnet_list_query_instance = OpenstackSubnetListQuery.from_json(json)
# print the JSON string representation of the object
print(OpenstackSubnetListQuery.to_json())

# convert the object into a dict
openstack_subnet_list_query_dict = openstack_subnet_list_query_instance.to_dict()
# create an instance of OpenstackSubnetListQuery from a dict
openstack_subnet_list_query_from_dict = OpenstackSubnetListQuery.from_dict(openstack_subnet_list_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



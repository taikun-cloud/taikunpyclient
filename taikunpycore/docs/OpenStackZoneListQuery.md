# OpenStackZoneListQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from taikunpycore.models.open_stack_zone_list_query import OpenStackZoneListQuery

# TODO update the JSON string below
json = "{}"
# create an instance of OpenStackZoneListQuery from a JSON string
open_stack_zone_list_query_instance = OpenStackZoneListQuery.from_json(json)
# print the JSON string representation of the object
print(OpenStackZoneListQuery.to_json())

# convert the object into a dict
open_stack_zone_list_query_dict = open_stack_zone_list_query_instance.to_dict()
# create an instance of OpenStackZoneListQuery from a dict
open_stack_zone_list_query_from_dict = OpenStackZoneListQuery.from_dict(open_stack_zone_list_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



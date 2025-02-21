# OpenStackProjectListQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_stack_user** | **str** |  | [optional] 
**open_stack_password** | **str** |  | [optional] 
**open_stack_url** | **str** |  | [optional] 
**open_stack_domain** | **str** |  | [optional] 
**application_cred_enabled** | **bool** |  | [optional] 
**is_admin** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.open_stack_project_list_query import OpenStackProjectListQuery

# TODO update the JSON string below
json = "{}"
# create an instance of OpenStackProjectListQuery from a JSON string
open_stack_project_list_query_instance = OpenStackProjectListQuery.from_json(json)
# print the JSON string representation of the object
print(OpenStackProjectListQuery.to_json())

# convert the object into a dict
open_stack_project_list_query_dict = open_stack_project_list_query_instance.to_dict()
# create an instance of OpenStackProjectListQuery from a dict
open_stack_project_list_query_from_dict = OpenStackProjectListQuery.from_dict(open_stack_project_list_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



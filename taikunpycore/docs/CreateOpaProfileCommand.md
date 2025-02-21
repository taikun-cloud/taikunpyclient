# CreateOpaProfileCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**forbid_node_port** | **bool** |  | [optional] 
**forbid_http_ingress** | **bool** |  | [optional] 
**require_probe** | **bool** |  | [optional] 
**unique_ingresses** | **bool** |  | [optional] 
**unique_service_selector** | **bool** |  | [optional] 
**force_pod_resource** | **bool** |  | [optional] 
**is_node_name_forbidden_in_vc** | **bool** |  | [optional] 
**is_master_taint_enforced** | **bool** |  | [optional] 
**allowed_repo** | **List[str]** |  | [optional] 
**forbid_specific_tags** | **List[str]** |  | [optional] 
**ingress_whitelist** | **List[str]** |  | [optional] 
**whitelist_master_taint_namespaces** | **List[str]** |  | [optional] 
**organization_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.create_opa_profile_command import CreateOpaProfileCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOpaProfileCommand from a JSON string
create_opa_profile_command_instance = CreateOpaProfileCommand.from_json(json)
# print the JSON string representation of the object
print(CreateOpaProfileCommand.to_json())

# convert the object into a dict
create_opa_profile_command_dict = create_opa_profile_command_instance.to_dict()
# create an instance of CreateOpaProfileCommand from a dict
create_opa_profile_command_from_dict = CreateOpaProfileCommand.from_dict(create_opa_profile_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



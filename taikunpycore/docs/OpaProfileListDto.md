# OpaProfileListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**forbid_node_port** | **bool** |  | 
**forbid_http_ingress** | **bool** |  | 
**require_probe** | **bool** |  | 
**unique_ingresses** | **bool** |  | 
**unique_service_selector** | **bool** |  | 
**force_pod_resource** | **bool** |  | 
**is_node_name_forbidden_in_vc** | **bool** |  | 
**is_master_taint_enforced** | **bool** |  | 
**whitelist_master_taint_namespaces** | **List[str]** |  | 
**allowed_repo** | **List[str]** |  | 
**forbid_specific_tags** | **List[str]** |  | 
**ingress_whitelist** | **List[str]** |  | 
**is_locked** | **bool** |  | 
**revision** | **int** |  | 
**organization_id** | **int** |  | 
**organization_name** | **str** |  | 
**created_at** | **str** |  | 
**is_default** | **bool** |  | 
**projects** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 

## Example

```python
from taikunpycore.models.opa_profile_list_dto import OpaProfileListDto

# TODO update the JSON string below
json = "{}"
# create an instance of OpaProfileListDto from a JSON string
opa_profile_list_dto_instance = OpaProfileListDto.from_json(json)
# print the JSON string representation of the object
print(OpaProfileListDto.to_json())

# convert the object into a dict
opa_profile_list_dto_dict = opa_profile_list_dto_instance.to_dict()
# create an instance of OpaProfileListDto from a dict
opa_profile_list_dto_from_dict = OpaProfileListDto.from_dict(opa_profile_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



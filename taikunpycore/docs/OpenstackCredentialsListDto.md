# OpenstackCredentialsListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**project_count** | **int** |  | 
**is_locked** | **bool** |  | 
**name** | **str** |  | 
**user** | **str** |  | 
**url** | **str** |  | 
**project** | **str** |  | 
**domain** | **str** |  | 
**region** | **str** |  | 
**public_network** | **str** |  | 
**import_network** | **bool** |  | 
**tenant_id** | **str** |  | 
**availability_zone** | **str** |  | 
**volume_type** | **str** |  | 
**internal_subnet_id** | **str** |  | 
**projects** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**created_by** | **str** |  | 
**last_modified** | **str** |  | 
**last_modified_by** | **str** |  | 
**is_default** | **bool** |  | 
**organization_id** | **int** |  | 
**organization_name** | **str** |  | 
**created_at** | **str** |  | 
**continent_name** | **str** |  | 
**is_admin** | **bool** |  | 
**is_infra** | **bool** |  | 
**application_cred_enabled** | **bool** |  | 
**skip_tls_flag** | **bool** |  | 

## Example

```python
from taikunpycore.models.openstack_credentials_list_dto import OpenstackCredentialsListDto

# TODO update the JSON string below
json = "{}"
# create an instance of OpenstackCredentialsListDto from a JSON string
openstack_credentials_list_dto_instance = OpenstackCredentialsListDto.from_json(json)
# print the JSON string representation of the object
print(OpenstackCredentialsListDto.to_json())

# convert the object into a dict
openstack_credentials_list_dto_dict = openstack_credentials_list_dto_instance.to_dict()
# create an instance of OpenstackCredentialsListDto from a dict
openstack_credentials_list_dto_from_dict = OpenstackCredentialsListDto.from_dict(openstack_credentials_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



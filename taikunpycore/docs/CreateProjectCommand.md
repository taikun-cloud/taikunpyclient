# CreateProjectCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**kubernetes_version** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**cloud_credential_id** | **int** |  | [optional] 
**s3_credential_id** | **int** |  | [optional] 
**access_profile_id** | **int** |  | [optional] 
**opa_profile_id** | **int** |  | [optional] 
**kubernetes_profile_id** | **int** |  | [optional] 
**is_kubernetes** | **bool** |  | [optional] 
**is_auto_upgrade** | **bool** |  | [optional] 
**is_backup_enabled** | **bool** |  | [optional] 
**is_monitoring_enabled** | **bool** |  | [optional] 
**ai_enabled** | **bool** |  | [optional] 
**ai_credential_id** | **int** |  | [optional] 
**flavors** | **List[str]** |  | [optional] 
**users** | **List[str]** |  | [optional] 
**alerting_profile_id** | **int** |  | [optional] 
**taikun_lb_flavor** | **str** |  | [optional] 
**router_id_start_range** | **int** |  | [optional] 
**router_id_end_range** | **int** |  | [optional] 
**expired_at** | **datetime** |  | [optional] 
**delete_on_expiration** | **bool** |  | [optional] 
**allow_full_spot_kubernetes** | **bool** |  | [optional] 
**allow_spot_workers** | **bool** |  | [optional] 
**allow_spot_vms** | **bool** |  | [optional] 
**max_spot_price** | **float** |  | [optional] 
**autoscaling_enabled** | **bool** |  | [optional] 
**autoscaling_group_name** | **str** |  | [optional] 
**min_size** | **int** |  | [optional] 
**max_size** | **int** |  | [optional] 
**disk_size** | **float** |  | [optional] 
**autoscaling_flavor** | **str** |  | [optional] 
**autoscaling_spot_enabled** | **bool** |  | [optional] 
**cidr** | **str** |  | [optional] 
**net_mask** | **int** |  | [optional] 
**save_as_template** | **bool** |  | [optional] 
**template_name** | **str** |  | [optional] 
**server_templates** | [**List[ServerTemplateDto]**](ServerTemplateDto.md) |  | [optional] 

## Example

```python
from taikunpycore.models.create_project_command import CreateProjectCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectCommand from a JSON string
create_project_command_instance = CreateProjectCommand.from_json(json)
# print the JSON string representation of the object
print(CreateProjectCommand.to_json())

# convert the object into a dict
create_project_command_dict = create_project_command_instance.to_dict()
# create an instance of CreateProjectCommand from a dict
create_project_command_from_dict = CreateProjectCommand.from_dict(create_project_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



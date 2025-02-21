# ProjectListForAlert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**token** | **str** |  | 
**status** | **str** |  | 
**organization_id** | **int** |  | 
**health** | **str** |  | 
**is_kubernetes** | **bool** |  | 
**is_locked** | **bool** |  | 
**is_monitoring_enabled** | **bool** |  | 
**has_kube_config_file** | **bool** |  | 
**monitoring_credential** | [**MonitoringCredentialsListDto**](MonitoringCredentialsListDto.md) |  | 
**kubernetes_alerts** | [**List[KubernetesAlertDtoForPoller]**](KubernetesAlertDtoForPoller.md) |  | 
**kubernetes_current_version** | **str** |  | 
**total_servers_count** | **int** |  | 

## Example

```python
from taikunpycore.models.project_list_for_alert import ProjectListForAlert

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectListForAlert from a JSON string
project_list_for_alert_instance = ProjectListForAlert.from_json(json)
# print the JSON string representation of the object
print(ProjectListForAlert.to_json())

# convert the object into a dict
project_list_for_alert_dict = project_list_for_alert_instance.to_dict()
# create an instance of ProjectListForAlert from a dict
project_list_for_alert_from_dict = ProjectListForAlert.from_dict(project_list_for_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



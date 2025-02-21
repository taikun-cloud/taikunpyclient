# KubernetesAlertDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**labels** | **object** |  | 
**description** | **str** |  | 
**title** | **str** |  | 
**severity** | **str** |  | 
**fingerprint** | **str** |  | 
**status** | **str** |  | 
**starts_at** | **str** |  | 
**end_at** | **str** |  | 
**is_solved** | **bool** |  | 
**project_id** | **int** |  | 
**project_name** | **str** |  | 
**is_silenced** | **bool** |  | 
**silence_reason** | **str** |  | 
**last_modified_by** | **str** |  | 
**is_monitoring_enabled** | **bool** |  | 

## Example

```python
from taikunpycore.models.kubernetes_alert_dto import KubernetesAlertDto

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesAlertDto from a JSON string
kubernetes_alert_dto_instance = KubernetesAlertDto.from_json(json)
# print the JSON string representation of the object
print(KubernetesAlertDto.to_json())

# convert the object into a dict
kubernetes_alert_dto_dict = kubernetes_alert_dto_instance.to_dict()
# create an instance of KubernetesAlertDto from a dict
kubernetes_alert_dto_from_dict = KubernetesAlertDto.from_dict(kubernetes_alert_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



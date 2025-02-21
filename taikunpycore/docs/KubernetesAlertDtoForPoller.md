# KubernetesAlertDtoForPoller


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

## Example

```python
from taikunpycore.models.kubernetes_alert_dto_for_poller import KubernetesAlertDtoForPoller

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesAlertDtoForPoller from a JSON string
kubernetes_alert_dto_for_poller_instance = KubernetesAlertDtoForPoller.from_json(json)
# print the JSON string representation of the object
print(KubernetesAlertDtoForPoller.to_json())

# convert the object into a dict
kubernetes_alert_dto_for_poller_dict = kubernetes_alert_dto_for_poller_instance.to_dict()
# create an instance of KubernetesAlertDtoForPoller from a dict
kubernetes_alert_dto_for_poller_from_dict = KubernetesAlertDtoForPoller.from_dict(kubernetes_alert_dto_for_poller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



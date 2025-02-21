# KubernetesAlertCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**labels** | **object** |  | [optional] 
**annotations** | [**KubernetesAnnotations**](KubernetesAnnotations.md) |  | [optional] 
**starts_at** | **datetime** |  | [optional] 
**ends_at** | **datetime** |  | [optional] 
**fingerprint** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.kubernetes_alert_create_dto import KubernetesAlertCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesAlertCreateDto from a JSON string
kubernetes_alert_create_dto_instance = KubernetesAlertCreateDto.from_json(json)
# print the JSON string representation of the object
print(KubernetesAlertCreateDto.to_json())

# convert the object into a dict
kubernetes_alert_create_dto_dict = kubernetes_alert_create_dto_instance.to_dict()
# create an instance of KubernetesAlertCreateDto from a dict
kubernetes_alert_create_dto_from_dict = KubernetesAlertCreateDto.from_dict(kubernetes_alert_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



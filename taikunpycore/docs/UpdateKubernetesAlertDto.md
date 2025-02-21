# UpdateKubernetesAlertDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**labels** | **object** |  | [optional] 
**starts_at** | **datetime** |  | [optional] 
**ends_at** | **datetime** |  | [optional] 
**fingerprint** | **str** |  | [optional] 
**is_silenced** | **bool** |  | [optional] 
**silence_reason** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.update_kubernetes_alert_dto import UpdateKubernetesAlertDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateKubernetesAlertDto from a JSON string
update_kubernetes_alert_dto_instance = UpdateKubernetesAlertDto.from_json(json)
# print the JSON string representation of the object
print(UpdateKubernetesAlertDto.to_json())

# convert the object into a dict
update_kubernetes_alert_dto_dict = update_kubernetes_alert_dto_instance.to_dict()
# create an instance of UpdateKubernetesAlertDto from a dict
update_kubernetes_alert_dto_from_dict = UpdateKubernetesAlertDto.from_dict(update_kubernetes_alert_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



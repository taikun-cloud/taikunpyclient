# KubernetesAlertList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[KubernetesAlertDto]**](KubernetesAlertDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.kubernetes_alert_list import KubernetesAlertList

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesAlertList from a JSON string
kubernetes_alert_list_instance = KubernetesAlertList.from_json(json)
# print the JSON string representation of the object
print(KubernetesAlertList.to_json())

# convert the object into a dict
kubernetes_alert_list_dict = kubernetes_alert_list_instance.to_dict()
# create an instance of KubernetesAlertList from a dict
kubernetes_alert_list_from_dict = KubernetesAlertList.from_dict(kubernetes_alert_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



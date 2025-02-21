# KubernetesActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**namespace** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.kubernetes_action_request import KubernetesActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesActionRequest from a JSON string
kubernetes_action_request_instance = KubernetesActionRequest.from_json(json)
# print the JSON string representation of the object
print(KubernetesActionRequest.to_json())

# convert the object into a dict
kubernetes_action_request_dict = kubernetes_action_request_instance.to_dict()
# create an instance of KubernetesActionRequest from a dict
kubernetes_action_request_from_dict = KubernetesActionRequest.from_dict(kubernetes_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



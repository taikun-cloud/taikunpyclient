# KubernetesActionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**succeeded** | **List[str]** |  | [optional] 
**failed** | **List[str]** |  | [optional] 

## Example

```python
from taikunpycore.models.kubernetes_action_response import KubernetesActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesActionResponse from a JSON string
kubernetes_action_response_instance = KubernetesActionResponse.from_json(json)
# print the JSON string representation of the object
print(KubernetesActionResponse.to_json())

# convert the object into a dict
kubernetes_action_response_dict = kubernetes_action_response_instance.to_dict()
# create an instance of KubernetesActionResponse from a dict
kubernetes_action_response_from_dict = KubernetesActionResponse.from_dict(kubernetes_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



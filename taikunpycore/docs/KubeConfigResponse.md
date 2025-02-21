# KubeConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | 

## Example

```python
from taikunpycore.models.kube_config_response import KubeConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KubeConfigResponse from a JSON string
kube_config_response_instance = KubeConfigResponse.from_json(json)
# print the JSON string representation of the object
print(KubeConfigResponse.to_json())

# convert the object into a dict
kube_config_response_dict = kube_config_response_instance.to_dict()
# create an instance of KubeConfigResponse from a dict
kube_config_response_from_dict = KubeConfigResponse.from_dict(kube_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



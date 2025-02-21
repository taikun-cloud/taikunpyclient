# KubeConfigRoleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.kube_config_role_response import KubeConfigRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KubeConfigRoleResponse from a JSON string
kube_config_role_response_instance = KubeConfigRoleResponse.from_json(json)
# print the JSON string representation of the object
print(KubeConfigRoleResponse.to_json())

# convert the object into a dict
kube_config_role_response_dict = kube_config_role_response_instance.to_dict()
# create an instance of KubeConfigRoleResponse from a dict
kube_config_role_response_from_dict = KubeConfigRoleResponse.from_dict(kube_config_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



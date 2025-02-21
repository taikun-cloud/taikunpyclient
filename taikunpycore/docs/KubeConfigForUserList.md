# KubeConfigForUserList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[KubeConfigForUserDto]**](KubeConfigForUserDto.md) |  | 
**total_count** | **int** |  | 
**can_add** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 

## Example

```python
from taikunpycore.models.kube_config_for_user_list import KubeConfigForUserList

# TODO update the JSON string below
json = "{}"
# create an instance of KubeConfigForUserList from a JSON string
kube_config_for_user_list_instance = KubeConfigForUserList.from_json(json)
# print the JSON string representation of the object
print(KubeConfigForUserList.to_json())

# convert the object into a dict
kube_config_for_user_list_dict = kube_config_for_user_list_instance.to_dict()
# create an instance of KubeConfigForUserList from a dict
kube_config_for_user_list_from_dict = KubeConfigForUserList.from_dict(kube_config_for_user_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



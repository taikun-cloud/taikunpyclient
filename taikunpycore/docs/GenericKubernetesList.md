# GenericKubernetesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GenericKubernetesListDto]**](GenericKubernetesListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.generic_kubernetes_list import GenericKubernetesList

# TODO update the JSON string below
json = "{}"
# create an instance of GenericKubernetesList from a JSON string
generic_kubernetes_list_instance = GenericKubernetesList.from_json(json)
# print the JSON string representation of the object
print(GenericKubernetesList.to_json())

# convert the object into a dict
generic_kubernetes_list_dict = generic_kubernetes_list_instance.to_dict()
# create an instance of GenericKubernetesList from a dict
generic_kubernetes_list_from_dict = GenericKubernetesList.from_dict(generic_kubernetes_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



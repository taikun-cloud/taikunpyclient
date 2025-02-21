# KubernetesAnnotations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.kubernetes_annotations import KubernetesAnnotations

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesAnnotations from a JSON string
kubernetes_annotations_instance = KubernetesAnnotations.from_json(json)
# print the JSON string representation of the object
print(KubernetesAnnotations.to_json())

# convert the object into a dict
kubernetes_annotations_dict = kubernetes_annotations_instance.to_dict()
# create an instance of KubernetesAnnotations from a dict
kubernetes_annotations_from_dict = KubernetesAnnotations.from_dict(kubernetes_annotations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



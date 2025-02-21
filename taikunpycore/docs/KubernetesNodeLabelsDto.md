# KubernetesNodeLabelsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from taikunpycore.models.kubernetes_node_labels_dto import KubernetesNodeLabelsDto

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesNodeLabelsDto from a JSON string
kubernetes_node_labels_dto_instance = KubernetesNodeLabelsDto.from_json(json)
# print the JSON string representation of the object
print(KubernetesNodeLabelsDto.to_json())

# convert the object into a dict
kubernetes_node_labels_dto_dict = kubernetes_node_labels_dto_instance.to_dict()
# create an instance of KubernetesNodeLabelsDto from a dict
kubernetes_node_labels_dto_from_dict = KubernetesNodeLabelsDto.from_dict(kubernetes_node_labels_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



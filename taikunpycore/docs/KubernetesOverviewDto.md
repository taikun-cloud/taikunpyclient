# KubernetesOverviewDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | 
**project_name** | **str** |  | 
**healthy_pods** | **int** |  | 
**unhealthy_pods** | **int** |  | 
**healthy_nodes** | **int** |  | 
**unhealthy_nodes** | **int** |  | 
**alerts_count** | **int** |  | 
**kubernetes_health** | **str** |  | 

## Example

```python
from taikunpycore.models.kubernetes_overview_dto import KubernetesOverviewDto

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesOverviewDto from a JSON string
kubernetes_overview_dto_instance = KubernetesOverviewDto.from_json(json)
# print the JSON string representation of the object
print(KubernetesOverviewDto.to_json())

# convert the object into a dict
kubernetes_overview_dto_dict = kubernetes_overview_dto_instance.to_dict()
# create an instance of KubernetesOverviewDto from a dict
kubernetes_overview_dto_from_dict = KubernetesOverviewDto.from_dict(kubernetes_overview_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



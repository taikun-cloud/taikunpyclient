# KubernetesDashboardDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pods** | [**List[PodDto]**](PodDto.md) |  | 
**nodes** | [**List[NodeDto]**](NodeDto.md) |  | 

## Example

```python
from taikunpycore.models.kubernetes_dashboard_dto import KubernetesDashboardDto

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesDashboardDto from a JSON string
kubernetes_dashboard_dto_instance = KubernetesDashboardDto.from_json(json)
# print the JSON string representation of the object
print(KubernetesDashboardDto.to_json())

# convert the object into a dict
kubernetes_dashboard_dto_dict = kubernetes_dashboard_dto_instance.to_dict()
# create an instance of KubernetesDashboardDto from a dict
kubernetes_dashboard_dto_from_dict = KubernetesDashboardDto.from_dict(kubernetes_dashboard_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



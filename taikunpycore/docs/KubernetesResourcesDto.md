# KubernetesResourcesDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pods** | **int** |  | 
**crds** | **int** |  | 
**helmreleases** | **int** |  | 
**daemon_sets** | **int** |  | 
**deployments** | **int** |  | 
**stateful_sets** | **int** |  | 
**jobs** | **int** |  | 
**cron_jobs** | **int** |  | 
**config_maps** | **int** |  | 
**namespaces** | **int** |  | 
**nodes** | **int** |  | 
**pvcs** | **int** |  | 
**secrets** | **int** |  | 
**services** | **int** |  | 
**ingresses** | **int** |  | 
**network_policies** | **int** |  | 
**pdbs** | **int** |  | 
**storage_classes** | **int** |  | 

## Example

```python
from taikunpycore.models.kubernetes_resources_dto import KubernetesResourcesDto

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesResourcesDto from a JSON string
kubernetes_resources_dto_instance = KubernetesResourcesDto.from_json(json)
# print the JSON string representation of the object
print(KubernetesResourcesDto.to_json())

# convert the object into a dict
kubernetes_resources_dto_dict = kubernetes_resources_dto_instance.to_dict()
# create an instance of KubernetesResourcesDto from a dict
kubernetes_resources_dto_from_dict = KubernetesResourcesDto.from_dict(kubernetes_resources_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



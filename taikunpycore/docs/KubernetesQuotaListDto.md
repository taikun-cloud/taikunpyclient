# KubernetesQuotaListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sum_of_cpu** | **float** |  | 
**sum_of_ram_in_gb** | **float** |  | 
**sum_of_cpu_usage** | **float** |  | 
**sum_of_ram_usage** | **float** |  | 
**pods_capacity** | **int** |  | 
**pods_total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.kubernetes_quota_list_dto import KubernetesQuotaListDto

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesQuotaListDto from a JSON string
kubernetes_quota_list_dto_instance = KubernetesQuotaListDto.from_json(json)
# print the JSON string representation of the object
print(KubernetesQuotaListDto.to_json())

# convert the object into a dict
kubernetes_quota_list_dto_dict = kubernetes_quota_list_dto_instance.to_dict()
# create an instance of KubernetesQuotaListDto from a dict
kubernetes_quota_list_dto_from_dict = KubernetesQuotaListDto.from_dict(kubernetes_quota_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



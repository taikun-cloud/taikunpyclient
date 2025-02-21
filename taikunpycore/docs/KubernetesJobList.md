# KubernetesJobList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[KubernetesJobDto]**](KubernetesJobDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.kubernetes_job_list import KubernetesJobList

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesJobList from a JSON string
kubernetes_job_list_instance = KubernetesJobList.from_json(json)
# print the JSON string representation of the object
print(KubernetesJobList.to_json())

# convert the object into a dict
kubernetes_job_list_dict = kubernetes_job_list_instance.to_dict()
# create an instance of KubernetesJobList from a dict
kubernetes_job_list_from_dict = KubernetesJobList.from_dict(kubernetes_job_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



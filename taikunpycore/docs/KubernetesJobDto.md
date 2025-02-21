# KubernetesJobDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_name** | **str** |  | 
**namespace** | **str** |  | 
**age** | **str** |  | 
**completions** | **int** |  | 
**conditions** | **str** |  | 

## Example

```python
from taikunpycore.models.kubernetes_job_dto import KubernetesJobDto

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesJobDto from a JSON string
kubernetes_job_dto_instance = KubernetesJobDto.from_json(json)
# print the JSON string representation of the object
print(KubernetesJobDto.to_json())

# convert the object into a dict
kubernetes_job_dto_dict = kubernetes_job_dto_instance.to_dict()
# create an instance of KubernetesJobDto from a dict
kubernetes_job_dto_from_dict = KubernetesJobDto.from_dict(kubernetes_job_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



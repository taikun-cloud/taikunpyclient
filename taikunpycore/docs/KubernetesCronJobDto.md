# KubernetesCronJobDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_name** | **str** |  | 
**last_schedule** | **str** |  | 
**suspend** | **bool** |  | 
**schedule** | **str** |  | 
**namespace** | **str** |  | 
**age** | **str** |  | 

## Example

```python
from taikunpycore.models.kubernetes_cron_job_dto import KubernetesCronJobDto

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesCronJobDto from a JSON string
kubernetes_cron_job_dto_instance = KubernetesCronJobDto.from_json(json)
# print the JSON string representation of the object
print(KubernetesCronJobDto.to_json())

# convert the object into a dict
kubernetes_cron_job_dto_dict = kubernetes_cron_job_dto_instance.to_dict()
# create an instance of KubernetesCronJobDto from a dict
kubernetes_cron_job_dto_from_dict = KubernetesCronJobDto.from_dict(kubernetes_cron_job_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



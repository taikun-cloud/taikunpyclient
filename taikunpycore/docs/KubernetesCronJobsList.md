# KubernetesCronJobsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[KubernetesCronJobDto]**](KubernetesCronJobDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.kubernetes_cron_jobs_list import KubernetesCronJobsList

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesCronJobsList from a JSON string
kubernetes_cron_jobs_list_instance = KubernetesCronJobsList.from_json(json)
# print the JSON string representation of the object
print(KubernetesCronJobsList.to_json())

# convert the object into a dict
kubernetes_cron_jobs_list_dict = kubernetes_cron_jobs_list_instance.to_dict()
# create an instance of KubernetesCronJobsList from a dict
kubernetes_cron_jobs_list_from_dict = KubernetesCronJobsList.from_dict(kubernetes_cron_jobs_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



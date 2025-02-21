# KubernetesPodLogsCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**container** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.kubernetes_pod_logs_command import KubernetesPodLogsCommand

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesPodLogsCommand from a JSON string
kubernetes_pod_logs_command_instance = KubernetesPodLogsCommand.from_json(json)
# print the JSON string representation of the object
print(KubernetesPodLogsCommand.to_json())

# convert the object into a dict
kubernetes_pod_logs_command_dict = kubernetes_pod_logs_command_instance.to_dict()
# create an instance of KubernetesPodLogsCommand from a dict
kubernetes_pod_logs_command_from_dict = KubernetesPodLogsCommand.from_dict(kubernetes_pod_logs_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



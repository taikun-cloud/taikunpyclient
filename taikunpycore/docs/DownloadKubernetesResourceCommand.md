# DownloadKubernetesResourceCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | 
**name** | **str** |  | 
**namespace** | **str** |  | [optional] 
**kind** | [**EKubernetesResource**](EKubernetesResource.md) |  | 

## Example

```python
from taikunpycore.models.download_kubernetes_resource_command import DownloadKubernetesResourceCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadKubernetesResourceCommand from a JSON string
download_kubernetes_resource_command_instance = DownloadKubernetesResourceCommand.from_json(json)
# print the JSON string representation of the object
print(DownloadKubernetesResourceCommand.to_json())

# convert the object into a dict
download_kubernetes_resource_command_dict = download_kubernetes_resource_command_instance.to_dict()
# create an instance of DownloadKubernetesResourceCommand from a dict
download_kubernetes_resource_command_from_dict = DownloadKubernetesResourceCommand.from_dict(download_kubernetes_resource_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



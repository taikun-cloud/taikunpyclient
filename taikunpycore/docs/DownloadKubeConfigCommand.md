# DownloadKubeConfigCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.download_kube_config_command import DownloadKubeConfigCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadKubeConfigCommand from a JSON string
download_kube_config_command_instance = DownloadKubeConfigCommand.from_json(json)
# print the JSON string representation of the object
print(DownloadKubeConfigCommand.to_json())

# convert the object into a dict
download_kube_config_command_dict = download_kube_config_command_instance.to_dict()
# create an instance of DownloadKubeConfigCommand from a dict
download_kube_config_command_from_dict = DownloadKubeConfigCommand.from_dict(download_kube_config_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



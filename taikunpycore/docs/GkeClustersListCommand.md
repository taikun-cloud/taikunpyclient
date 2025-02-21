# GkeClustersListCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.gke_clusters_list_command import GkeClustersListCommand

# TODO update the JSON string below
json = "{}"
# create an instance of GkeClustersListCommand from a JSON string
gke_clusters_list_command_instance = GkeClustersListCommand.from_json(json)
# print the JSON string representation of the object
print(GkeClustersListCommand.to_json())

# convert the object into a dict
gke_clusters_list_command_dict = gke_clusters_list_command_instance.to_dict()
# create an instance of GkeClustersListCommand from a dict
gke_clusters_list_command_from_dict = GkeClustersListCommand.from_dict(gke_clusters_list_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



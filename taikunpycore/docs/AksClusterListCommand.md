# AksClusterListCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.aks_cluster_list_command import AksClusterListCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AksClusterListCommand from a JSON string
aks_cluster_list_command_instance = AksClusterListCommand.from_json(json)
# print the JSON string representation of the object
print(AksClusterListCommand.to_json())

# convert the object into a dict
aks_cluster_list_command_dict = aks_cluster_list_command_instance.to_dict()
# create an instance of AksClusterListCommand from a dict
aks_cluster_list_command_from_dict = AksClusterListCommand.from_dict(aks_cluster_list_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DeleteVirtualClusterCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.delete_virtual_cluster_command import DeleteVirtualClusterCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteVirtualClusterCommand from a JSON string
delete_virtual_cluster_command_instance = DeleteVirtualClusterCommand.from_json(json)
# print the JSON string representation of the object
print(DeleteVirtualClusterCommand.to_json())

# convert the object into a dict
delete_virtual_cluster_command_dict = delete_virtual_cluster_command_instance.to_dict()
# create an instance of DeleteVirtualClusterCommand from a dict
delete_virtual_cluster_command_from_dict = DeleteVirtualClusterCommand.from_dict(delete_virtual_cluster_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateVirtualClusterCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**expired_at** | **datetime** |  | [optional] 
**delete_on_expiration** | **bool** |  | [optional] 
**alerting_profile_id** | **int** |  | [optional] 
**expose_hostname** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.create_virtual_cluster_command import CreateVirtualClusterCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVirtualClusterCommand from a JSON string
create_virtual_cluster_command_instance = CreateVirtualClusterCommand.from_json(json)
# print the JSON string representation of the object
print(CreateVirtualClusterCommand.to_json())

# convert the object into a dict
create_virtual_cluster_command_dict = create_virtual_cluster_command_instance.to_dict()
# create an instance of CreateVirtualClusterCommand from a dict
create_virtual_cluster_command_from_dict = CreateVirtualClusterCommand.from_dict(create_virtual_cluster_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



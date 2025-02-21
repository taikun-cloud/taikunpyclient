# CloudLockManagerCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.cloud_lock_manager_command import CloudLockManagerCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CloudLockManagerCommand from a JSON string
cloud_lock_manager_command_instance = CloudLockManagerCommand.from_json(json)
# print the JSON string representation of the object
print(CloudLockManagerCommand.to_json())

# convert the object into a dict
cloud_lock_manager_command_dict = cloud_lock_manager_command_instance.to_dict()
# create an instance of CloudLockManagerCommand from a dict
cloud_lock_manager_command_from_dict = CloudLockManagerCommand.from_dict(cloud_lock_manager_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



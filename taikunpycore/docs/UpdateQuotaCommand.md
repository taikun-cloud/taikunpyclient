# UpdateQuotaCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quota_id** | **int** |  | [optional] 
**server_cpu** | **int** |  | [optional] 
**server_ram** | **float** |  | [optional] 
**server_disk_size** | **float** |  | [optional] 
**vm_cpu** | **int** |  | [optional] 
**vm_ram** | **float** |  | [optional] 
**vm_volume_size** | **float** |  | [optional] 

## Example

```python
from taikunpycore.models.update_quota_command import UpdateQuotaCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateQuotaCommand from a JSON string
update_quota_command_instance = UpdateQuotaCommand.from_json(json)
# print the JSON string representation of the object
print(UpdateQuotaCommand.to_json())

# convert the object into a dict
update_quota_command_dict = update_quota_command_instance.to_dict()
# create an instance of UpdateQuotaCommand from a dict
update_quota_command_from_dict = UpdateQuotaCommand.from_dict(update_quota_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



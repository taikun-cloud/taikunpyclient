# ListAllDeleteBackupRequests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CDeleteBackupRequestDto]**](CDeleteBackupRequestDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.list_all_delete_backup_requests import ListAllDeleteBackupRequests

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllDeleteBackupRequests from a JSON string
list_all_delete_backup_requests_instance = ListAllDeleteBackupRequests.from_json(json)
# print the JSON string representation of the object
print(ListAllDeleteBackupRequests.to_json())

# convert the object into a dict
list_all_delete_backup_requests_dict = list_all_delete_backup_requests_instance.to_dict()
# create an instance of ListAllDeleteBackupRequests from a dict
list_all_delete_backup_requests_from_dict = ListAllDeleteBackupRequests.from_dict(list_all_delete_backup_requests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



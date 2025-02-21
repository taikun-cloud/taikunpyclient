# ListAllBackups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CBackupDto]**](CBackupDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.list_all_backups import ListAllBackups

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllBackups from a JSON string
list_all_backups_instance = ListAllBackups.from_json(json)
# print the JSON string representation of the object
print(ListAllBackups.to_json())

# convert the object into a dict
list_all_backups_dict = list_all_backups_instance.to_dict()
# create an instance of ListAllBackups from a dict
list_all_backups_from_dict = ListAllBackups.from_dict(list_all_backups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



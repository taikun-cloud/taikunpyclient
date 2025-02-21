# BackupCredentialsSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CommonSearchResponseData]**](CommonSearchResponseData.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.backup_credentials_search_list import BackupCredentialsSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of BackupCredentialsSearchList from a JSON string
backup_credentials_search_list_instance = BackupCredentialsSearchList.from_json(json)
# print the JSON string representation of the object
print(BackupCredentialsSearchList.to_json())

# convert the object into a dict
backup_credentials_search_list_dict = backup_credentials_search_list_instance.to_dict()
# create an instance of BackupCredentialsSearchList from a dict
backup_credentials_search_list_from_dict = BackupCredentialsSearchList.from_dict(backup_credentials_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



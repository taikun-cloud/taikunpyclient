# BackupCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BackupCredentialsListDto]**](BackupCredentialsListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.backup_credentials import BackupCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of BackupCredentials from a JSON string
backup_credentials_instance = BackupCredentials.from_json(json)
# print the JSON string representation of the object
print(BackupCredentials.to_json())

# convert the object into a dict
backup_credentials_dict = backup_credentials_instance.to_dict()
# create an instance of BackupCredentials from a dict
backup_credentials_from_dict = BackupCredentials.from_dict(backup_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



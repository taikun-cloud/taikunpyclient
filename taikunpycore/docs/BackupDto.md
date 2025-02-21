# BackupDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**included_namespace** | **List[str]** |  | 
**excluded_namespace** | **List[str]** |  | 

## Example

```python
from taikunpycore.models.backup_dto import BackupDto

# TODO update the JSON string below
json = "{}"
# create an instance of BackupDto from a JSON string
backup_dto_instance = BackupDto.from_json(json)
# print the JSON string representation of the object
print(BackupDto.to_json())

# convert the object into a dict
backup_dto_dict = backup_dto_instance.to_dict()
# create an instance of BackupDto from a dict
backup_dto_from_dict = BackupDto.from_dict(backup_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



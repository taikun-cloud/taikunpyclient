# BackupCredentialsListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**s3_name** | **str** |  | 
**s3_access_key_id** | **str** |  | 
**s3_endpoint** | **str** |  | 
**s3_region** | **str** |  | 
**organization_id** | **int** |  | 
**organization_name** | **str** |  | 
**projects** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**is_locked** | **bool** |  | 
**created_by** | **str** |  | 
**last_modified** | **str** |  | 
**last_modified_by** | **str** |  | 
**created_at** | **str** |  | 
**is_default** | **bool** |  | 
**is_infra** | **bool** |  | 

## Example

```python
from taikunpycore.models.backup_credentials_list_dto import BackupCredentialsListDto

# TODO update the JSON string below
json = "{}"
# create an instance of BackupCredentialsListDto from a JSON string
backup_credentials_list_dto_instance = BackupCredentialsListDto.from_json(json)
# print the JSON string representation of the object
print(BackupCredentialsListDto.to_json())

# convert the object into a dict
backup_credentials_list_dto_dict = backup_credentials_list_dto_instance.to_dict()
# create an instance of BackupCredentialsListDto from a dict
backup_credentials_list_dto_from_dict = BackupCredentialsListDto.from_dict(backup_credentials_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AzureQuotaListRecordDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_cores** | **int** |  | [optional] 
**current_usage** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.azure_quota_list_record_dto import AzureQuotaListRecordDto

# TODO update the JSON string below
json = "{}"
# create an instance of AzureQuotaListRecordDto from a JSON string
azure_quota_list_record_dto_instance = AzureQuotaListRecordDto.from_json(json)
# print the JSON string representation of the object
print(AzureQuotaListRecordDto.to_json())

# convert the object into a dict
azure_quota_list_record_dto_dict = azure_quota_list_record_dto_instance.to_dict()
# create an instance of AzureQuotaListRecordDto from a dict
azure_quota_list_record_dto_from_dict = AzureQuotaListRecordDto.from_dict(azure_quota_list_record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



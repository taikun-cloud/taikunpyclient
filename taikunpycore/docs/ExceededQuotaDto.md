# ExceededQuotaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from taikunpycore.models.exceeded_quota_dto import ExceededQuotaDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExceededQuotaDto from a JSON string
exceeded_quota_dto_instance = ExceededQuotaDto.from_json(json)
# print the JSON string representation of the object
print(ExceededQuotaDto.to_json())

# convert the object into a dict
exceeded_quota_dto_dict = exceeded_quota_dto_instance.to_dict()
# create an instance of ExceededQuotaDto from a dict
exceeded_quota_dto_from_dict = ExceededQuotaDto.from_dict(exceeded_quota_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



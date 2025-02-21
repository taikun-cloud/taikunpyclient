# ExceededQuotaList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ExceededQuotaDto]**](ExceededQuotaDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.exceeded_quota_list import ExceededQuotaList

# TODO update the JSON string below
json = "{}"
# create an instance of ExceededQuotaList from a JSON string
exceeded_quota_list_instance = ExceededQuotaList.from_json(json)
# print the JSON string representation of the object
print(ExceededQuotaList.to_json())

# convert the object into a dict
exceeded_quota_list_dict = exceeded_quota_list_instance.to_dict()
# create an instance of ExceededQuotaList from a dict
exceeded_quota_list_from_dict = ExceededQuotaList.from_dict(exceeded_quota_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ProjectQuotaList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ProjectQuotaListDto]**](ProjectQuotaListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.project_quota_list import ProjectQuotaList

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectQuotaList from a JSON string
project_quota_list_instance = ProjectQuotaList.from_json(json)
# print the JSON string representation of the object
print(ProjectQuotaList.to_json())

# convert the object into a dict
project_quota_list_dict = project_quota_list_instance.to_dict()
# create an instance of ProjectQuotaList from a dict
project_quota_list_from_dict = ProjectQuotaList.from_dict(project_quota_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



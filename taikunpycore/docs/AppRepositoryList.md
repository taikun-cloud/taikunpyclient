# AppRepositoryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ArtifactRepositoryDto]**](ArtifactRepositoryDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.app_repository_list import AppRepositoryList

# TODO update the JSON string below
json = "{}"
# create an instance of AppRepositoryList from a JSON string
app_repository_list_instance = AppRepositoryList.from_json(json)
# print the JSON string representation of the object
print(AppRepositoryList.to_json())

# convert the object into a dict
app_repository_list_dict = app_repository_list_instance.to_dict()
# create an instance of AppRepositoryList from a dict
app_repository_list_from_dict = AppRepositoryList.from_dict(app_repository_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



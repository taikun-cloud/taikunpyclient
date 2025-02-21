# ListAllRestores


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CRestoreDto]**](CRestoreDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.list_all_restores import ListAllRestores

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllRestores from a JSON string
list_all_restores_instance = ListAllRestores.from_json(json)
# print the JSON string representation of the object
print(ListAllRestores.to_json())

# convert the object into a dict
list_all_restores_dict = list_all_restores_instance.to_dict()
# create an instance of ListAllRestores from a dict
list_all_restores_from_dict = ListAllRestores.from_dict(list_all_restores_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



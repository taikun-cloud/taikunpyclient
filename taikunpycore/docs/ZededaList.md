# ZededaList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ZededaListDto]**](ZededaListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.zededa_list import ZededaList

# TODO update the JSON string below
json = "{}"
# create an instance of ZededaList from a JSON string
zededa_list_instance = ZededaList.from_json(json)
# print the JSON string representation of the object
print(ZededaList.to_json())

# convert the object into a dict
zededa_list_dict = zededa_list_instance.to_dict()
# create an instance of ZededaList from a dict
zededa_list_from_dict = ZededaList.from_dict(zededa_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



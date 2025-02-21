# PartnersSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PartnersSearchResponseData]**](PartnersSearchResponseData.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.partners_search_list import PartnersSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of PartnersSearchList from a JSON string
partners_search_list_instance = PartnersSearchList.from_json(json)
# print the JSON string representation of the object
print(PartnersSearchList.to_json())

# convert the object into a dict
partners_search_list_dict = partners_search_list_instance.to_dict()
# create an instance of PartnersSearchList from a dict
partners_search_list_from_dict = PartnersSearchList.from_dict(partners_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PartnersSearchResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.partners_search_response_data import PartnersSearchResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PartnersSearchResponseData from a JSON string
partners_search_response_data_instance = PartnersSearchResponseData.from_json(json)
# print the JSON string representation of the object
print(PartnersSearchResponseData.to_json())

# convert the object into a dict
partners_search_response_data_dict = partners_search_response_data_instance.to_dict()
# create an instance of PartnersSearchResponseData from a dict
partners_search_response_data_from_dict = PartnersSearchResponseData.from_dict(partners_search_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CommonSearchResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**organization_name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.common_search_response_data import CommonSearchResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CommonSearchResponseData from a JSON string
common_search_response_data_instance = CommonSearchResponseData.from_json(json)
# print the JSON string representation of the object
print(CommonSearchResponseData.to_json())

# convert the object into a dict
common_search_response_data_dict = common_search_response_data_instance.to_dict()
# create an instance of CommonSearchResponseData from a dict
common_search_response_data_from_dict = CommonSearchResponseData.from_dict(common_search_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



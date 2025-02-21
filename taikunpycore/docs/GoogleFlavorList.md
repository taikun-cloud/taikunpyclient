# GoogleFlavorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GoogleFlavorDto]**](GoogleFlavorDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.google_flavor_list import GoogleFlavorList

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleFlavorList from a JSON string
google_flavor_list_instance = GoogleFlavorList.from_json(json)
# print the JSON string representation of the object
print(GoogleFlavorList.to_json())

# convert the object into a dict
google_flavor_list_dict = google_flavor_list_instance.to_dict()
# create an instance of GoogleFlavorList from a dict
google_flavor_list_from_dict = GoogleFlavorList.from_dict(google_flavor_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



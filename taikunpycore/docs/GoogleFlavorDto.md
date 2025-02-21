# GoogleFlavorDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**cpu** | **int** |  | 
**ram** | **float** |  | 
**description** | **object** |  | 
**linux_price** | **float** |  | 
**windows_price** | **float** |  | 
**linux_spot_price** | **float** |  | 
**windows_spot_price** | **float** |  | 

## Example

```python
from taikunpycore.models.google_flavor_dto import GoogleFlavorDto

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleFlavorDto from a JSON string
google_flavor_dto_instance = GoogleFlavorDto.from_json(json)
# print the JSON string representation of the object
print(GoogleFlavorDto.to_json())

# convert the object into a dict
google_flavor_dto_dict = google_flavor_dto_instance.to_dict()
# create an instance of GoogleFlavorDto from a dict
google_flavor_dto_from_dict = GoogleFlavorDto.from_dict(google_flavor_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



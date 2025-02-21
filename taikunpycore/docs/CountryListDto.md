# CountryListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**is_eu** | **bool** |  | 

## Example

```python
from taikunpycore.models.country_list_dto import CountryListDto

# TODO update the JSON string below
json = "{}"
# create an instance of CountryListDto from a JSON string
country_list_dto_instance = CountryListDto.from_json(json)
# print the JSON string representation of the object
print(CountryListDto.to_json())

# convert the object into a dict
country_list_dto_dict = country_list_dto_instance.to_dict()
# create an instance of CountryListDto from a dict
country_list_dto_from_dict = CountryListDto.from_dict(country_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



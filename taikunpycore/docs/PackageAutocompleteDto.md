# PackageAutocompleteDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | [**ParameterType**](ParameterType.md) |  | [optional] 
**is_question** | **bool** |  | [optional] 
**options** | **List[str]** |  | [optional] 
**is_taikun_link** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.package_autocomplete_dto import PackageAutocompleteDto

# TODO update the JSON string below
json = "{}"
# create an instance of PackageAutocompleteDto from a JSON string
package_autocomplete_dto_instance = PackageAutocompleteDto.from_json(json)
# print the JSON string representation of the object
print(PackageAutocompleteDto.to_json())

# convert the object into a dict
package_autocomplete_dto_dict = package_autocomplete_dto_instance.to_dict()
# create an instance of PackageAutocompleteDto from a dict
package_autocomplete_dto_from_dict = PackageAutocompleteDto.from_dict(package_autocomplete_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



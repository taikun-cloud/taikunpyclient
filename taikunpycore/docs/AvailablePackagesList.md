# AvailablePackagesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AvailablePackagesDto]**](AvailablePackagesDto.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.available_packages_list import AvailablePackagesList

# TODO update the JSON string below
json = "{}"
# create an instance of AvailablePackagesList from a JSON string
available_packages_list_instance = AvailablePackagesList.from_json(json)
# print the JSON string representation of the object
print(AvailablePackagesList.to_json())

# convert the object into a dict
available_packages_list_dict = available_packages_list_instance.to_dict()
# create an instance of AvailablePackagesList from a dict
available_packages_list_from_dict = AvailablePackagesList.from_dict(available_packages_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TanzuFlavorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TanzuFlavorsListDto]**](TanzuFlavorsListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.tanzu_flavor_list import TanzuFlavorList

# TODO update the JSON string below
json = "{}"
# create an instance of TanzuFlavorList from a JSON string
tanzu_flavor_list_instance = TanzuFlavorList.from_json(json)
# print the JSON string representation of the object
print(TanzuFlavorList.to_json())

# convert the object into a dict
tanzu_flavor_list_dict = tanzu_flavor_list_instance.to_dict()
# create an instance of TanzuFlavorList from a dict
tanzu_flavor_list_from_dict = TanzuFlavorList.from_dict(tanzu_flavor_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



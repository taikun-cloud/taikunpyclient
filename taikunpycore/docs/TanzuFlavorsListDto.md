# TanzuFlavorsListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**cpu** | **int** |  | 
**ram** | **float** |  | 

## Example

```python
from taikunpycore.models.tanzu_flavors_list_dto import TanzuFlavorsListDto

# TODO update the JSON string below
json = "{}"
# create an instance of TanzuFlavorsListDto from a JSON string
tanzu_flavors_list_dto_instance = TanzuFlavorsListDto.from_json(json)
# print the JSON string representation of the object
print(TanzuFlavorsListDto.to_json())

# convert the object into a dict
tanzu_flavors_list_dto_dict = tanzu_flavors_list_dto_instance.to_dict()
# create an instance of TanzuFlavorsListDto from a dict
tanzu_flavors_list_dto_from_dict = TanzuFlavorsListDto.from_dict(tanzu_flavors_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FlavorsListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ram** | **float** |  | 
**cpu** | **int** |  | 
**name** | **str** |  | 
**description** | **object** |  | 
**max_data_disk_count** | **float** |  | 

## Example

```python
from taikunpycore.models.flavors_list_dto import FlavorsListDto

# TODO update the JSON string below
json = "{}"
# create an instance of FlavorsListDto from a JSON string
flavors_list_dto_instance = FlavorsListDto.from_json(json)
# print the JSON string representation of the object
print(FlavorsListDto.to_json())

# convert the object into a dict
flavors_list_dto_dict = flavors_list_dto_instance.to_dict()
# create an instance of FlavorsListDto from a dict
flavors_list_dto_from_dict = FlavorsListDto.from_dict(flavors_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AllFlavorsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FlavorsListDto]**](FlavorsListDto.md) |  | 
**total_count** | **int** |  | 
**cloud_type** | **str** |  | 

## Example

```python
from taikunpycore.models.all_flavors_list import AllFlavorsList

# TODO update the JSON string below
json = "{}"
# create an instance of AllFlavorsList from a JSON string
all_flavors_list_instance = AllFlavorsList.from_json(json)
# print the JSON string representation of the object
print(AllFlavorsList.to_json())

# convert the object into a dict
all_flavors_list_dict = all_flavors_list_instance.to_dict()
# create an instance of AllFlavorsList from a dict
all_flavors_list_from_dict = AllFlavorsList.from_dict(all_flavors_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



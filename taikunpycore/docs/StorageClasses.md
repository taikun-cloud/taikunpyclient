# StorageClasses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[StorageClassDto]**](StorageClassDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.storage_classes import StorageClasses

# TODO update the JSON string below
json = "{}"
# create an instance of StorageClasses from a JSON string
storage_classes_instance = StorageClasses.from_json(json)
# print the JSON string representation of the object
print(StorageClasses.to_json())

# convert the object into a dict
storage_classes_dict = storage_classes_instance.to_dict()
# create an instance of StorageClasses from a dict
storage_classes_from_dict = StorageClasses.from_dict(storage_classes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



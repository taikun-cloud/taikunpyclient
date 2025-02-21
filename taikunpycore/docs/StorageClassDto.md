# StorageClassDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_name** | **str** |  | 
**age** | **str** |  | 
**provisioner** | **str** |  | 
**reclaim_policy** | **str** |  | 
**volume_binding_mode** | **str** |  | 
**allow_volume_expansion** | **bool** |  | 

## Example

```python
from taikunpycore.models.storage_class_dto import StorageClassDto

# TODO update the JSON string below
json = "{}"
# create an instance of StorageClassDto from a JSON string
storage_class_dto_instance = StorageClassDto.from_json(json)
# print the JSON string representation of the object
print(StorageClassDto.to_json())

# convert the object into a dict
storage_class_dto_dict = storage_class_dto_instance.to_dict()
# create an instance of StorageClassDto from a dict
storage_class_dto_from_dict = StorageClassDto.from_dict(storage_class_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



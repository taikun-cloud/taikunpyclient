# PvcDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_name** | **str** |  | 
**phase** | **str** |  | 
**size** | **str** |  | 
**namespace** | **str** |  | 
**storage_class_name** | **str** |  | 
**age** | **str** |  | 

## Example

```python
from taikunpycore.models.pvc_dto import PvcDto

# TODO update the JSON string below
json = "{}"
# create an instance of PvcDto from a JSON string
pvc_dto_instance = PvcDto.from_json(json)
# print the JSON string representation of the object
print(PvcDto.to_json())

# convert the object into a dict
pvc_dto_dict = pvc_dto_instance.to_dict()
# create an instance of PvcDto from a dict
pvc_dto_from_dict = PvcDto.from_dict(pvc_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



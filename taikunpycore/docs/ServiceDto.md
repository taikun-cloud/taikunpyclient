# ServiceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_name** | **str** |  | 
**namespace** | **str** |  | 
**age** | **str** |  | 
**type** | **str** |  | 
**ip** | **object** |  | 

## Example

```python
from taikunpycore.models.service_dto import ServiceDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDto from a JSON string
service_dto_instance = ServiceDto.from_json(json)
# print the JSON string representation of the object
print(ServiceDto.to_json())

# convert the object into a dict
service_dto_dict = service_dto_instance.to_dict()
# create an instance of ServiceDto from a dict
service_dto_from_dict = ServiceDto.from_dict(service_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



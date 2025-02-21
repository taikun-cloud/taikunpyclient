# AllowedHostCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**mask_bits** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.allowed_host_create_dto import AllowedHostCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AllowedHostCreateDto from a JSON string
allowed_host_create_dto_instance = AllowedHostCreateDto.from_json(json)
# print the JSON string representation of the object
print(AllowedHostCreateDto.to_json())

# convert the object into a dict
allowed_host_create_dto_dict = allowed_host_create_dto_instance.to_dict()
# create an instance of AllowedHostCreateDto from a dict
allowed_host_create_dto_from_dict = AllowedHostCreateDto.from_dict(allowed_host_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



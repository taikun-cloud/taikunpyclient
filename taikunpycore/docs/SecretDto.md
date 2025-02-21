# SecretDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_name** | **str** |  | 
**namespace** | **str** |  | 
**age** | **str** |  | 

## Example

```python
from taikunpycore.models.secret_dto import SecretDto

# TODO update the JSON string below
json = "{}"
# create an instance of SecretDto from a JSON string
secret_dto_instance = SecretDto.from_json(json)
# print the JSON string representation of the object
print(SecretDto.to_json())

# convert the object into a dict
secret_dto_dict = secret_dto_instance.to_dict()
# create an instance of SecretDto from a dict
secret_dto_from_dict = SecretDto.from_dict(secret_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



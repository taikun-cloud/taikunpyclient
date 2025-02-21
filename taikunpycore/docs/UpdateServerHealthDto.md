# UpdateServerHealthDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** |  | [optional] 
**server_health** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.update_server_health_dto import UpdateServerHealthDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateServerHealthDto from a JSON string
update_server_health_dto_instance = UpdateServerHealthDto.from_json(json)
# print the JSON string representation of the object
print(UpdateServerHealthDto.to_json())

# convert the object into a dict
update_server_health_dto_dict = update_server_health_dto_instance.to_dict()
# create an instance of UpdateServerHealthDto from a dict
update_server_health_dto_from_dict = UpdateServerHealthDto.from_dict(update_server_health_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



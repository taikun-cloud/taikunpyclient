# CommonAvailabilityDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.common_availability_dto import CommonAvailabilityDto

# TODO update the JSON string below
json = "{}"
# create an instance of CommonAvailabilityDto from a JSON string
common_availability_dto_instance = CommonAvailabilityDto.from_json(json)
# print the JSON string representation of the object
print(CommonAvailabilityDto.to_json())

# convert the object into a dict
common_availability_dto_dict = common_availability_dto_instance.to_dict()
# create an instance of CommonAvailabilityDto from a dict
common_availability_dto_from_dict = CommonAvailabilityDto.from_dict(common_availability_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



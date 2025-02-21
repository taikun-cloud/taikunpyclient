# StandAloneMetaDataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.stand_alone_meta_data_dto import StandAloneMetaDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of StandAloneMetaDataDto from a JSON string
stand_alone_meta_data_dto_instance = StandAloneMetaDataDto.from_json(json)
# print the JSON string representation of the object
print(StandAloneMetaDataDto.to_json())

# convert the object into a dict
stand_alone_meta_data_dto_dict = stand_alone_meta_data_dto_instance.to_dict()
# create an instance of StandAloneMetaDataDto from a dict
stand_alone_meta_data_dto_from_dict = StandAloneMetaDataDto.from_dict(stand_alone_meta_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



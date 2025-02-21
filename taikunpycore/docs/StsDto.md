# StsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_name** | **str** |  | 
**status** | **str** |  | 
**namespace** | **str** |  | 
**age** | **str** |  | 

## Example

```python
from taikunpycore.models.sts_dto import StsDto

# TODO update the JSON string below
json = "{}"
# create an instance of StsDto from a JSON string
sts_dto_instance = StsDto.from_json(json)
# print the JSON string representation of the object
print(StsDto.to_json())

# convert the object into a dict
sts_dto_dict = sts_dto_instance.to_dict()
# create an instance of StsDto from a dict
sts_dto_from_dict = StsDto.from_dict(sts_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



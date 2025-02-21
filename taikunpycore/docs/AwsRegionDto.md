# AwsRegionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**region** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.aws_region_dto import AwsRegionDto

# TODO update the JSON string below
json = "{}"
# create an instance of AwsRegionDto from a JSON string
aws_region_dto_instance = AwsRegionDto.from_json(json)
# print the JSON string representation of the object
print(AwsRegionDto.to_json())

# convert the object into a dict
aws_region_dto_dict = aws_region_dto_instance.to_dict()
# create an instance of AwsRegionDto from a dict
aws_region_dto_from_dict = AwsRegionDto.from_dict(aws_region_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



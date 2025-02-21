# AwsFlavorListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ram** | **float** |  | [optional] 
**cpu** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **object** |  | [optional] 
**linux_price** | **str** |  | [optional] 
**windows_price** | **str** |  | [optional] 
**windows_spot_price** | **str** |  | [optional] 
**linux_spot_price** | **str** |  | [optional] 
**zones** | **List[str]** |  | [optional] 

## Example

```python
from taikunpycore.models.aws_flavor_list_dto import AwsFlavorListDto

# TODO update the JSON string below
json = "{}"
# create an instance of AwsFlavorListDto from a JSON string
aws_flavor_list_dto_instance = AwsFlavorListDto.from_json(json)
# print the JSON string representation of the object
print(AwsFlavorListDto.to_json())

# convert the object into a dict
aws_flavor_list_dto_dict = aws_flavor_list_dto_instance.to_dict()
# create an instance of AwsFlavorListDto from a dict
aws_flavor_list_dto_from_dict = AwsFlavorListDto.from_dict(aws_flavor_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



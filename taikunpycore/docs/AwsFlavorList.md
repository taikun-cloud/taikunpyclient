# AwsFlavorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AwsFlavorListDto]**](AwsFlavorListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.aws_flavor_list import AwsFlavorList

# TODO update the JSON string below
json = "{}"
# create an instance of AwsFlavorList from a JSON string
aws_flavor_list_instance = AwsFlavorList.from_json(json)
# print the JSON string representation of the object
print(AwsFlavorList.to_json())

# convert the object into a dict
aws_flavor_list_dict = aws_flavor_list_instance.to_dict()
# create an instance of AwsFlavorList from a dict
aws_flavor_list_from_dict = AwsFlavorList.from_dict(aws_flavor_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



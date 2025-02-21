# UserResourceChartDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_name** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**disk_size** | **int** |  | [optional] 
**ram** | **int** |  | [optional] 
**cpu** | **int** |  | [optional] 
**max_ram** | **int** |  | [optional] 
**max_cpu** | **int** |  | [optional] 
**max_disk_size** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.user_resource_chart_dto import UserResourceChartDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserResourceChartDto from a JSON string
user_resource_chart_dto_instance = UserResourceChartDto.from_json(json)
# print the JSON string representation of the object
print(UserResourceChartDto.to_json())

# convert the object into a dict
user_resource_chart_dto_dict = user_resource_chart_dto_instance.to_dict()
# create an instance of UserResourceChartDto from a dict
user_resource_chart_dto_from_dict = UserResourceChartDto.from_dict(user_resource_chart_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



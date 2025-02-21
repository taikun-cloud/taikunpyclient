# ProjectChartDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**succeeded** | [**List[ProjectCommonRecordDto]**](ProjectCommonRecordDto.md) |  | [optional] 
**updating** | [**List[ProjectCommonRecordDto]**](ProjectCommonRecordDto.md) |  | [optional] 
**total_count** | **int** |  | [optional] 
**failed** | [**List[ProjectCommonRecordDto]**](ProjectCommonRecordDto.md) |  | [optional] 
**purging** | [**List[ProjectCommonRecordDto]**](ProjectCommonRecordDto.md) |  | [optional] 
**deleting** | [**List[ProjectCommonRecordDto]**](ProjectCommonRecordDto.md) |  | [optional] 
**importing** | [**List[ProjectCommonRecordDto]**](ProjectCommonRecordDto.md) |  | [optional] 
**failed_to_import** | [**List[ProjectCommonRecordDto]**](ProjectCommonRecordDto.md) |  | [optional] 

## Example

```python
from taikunpycore.models.project_chart_dto import ProjectChartDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectChartDto from a JSON string
project_chart_dto_instance = ProjectChartDto.from_json(json)
# print the JSON string representation of the object
print(ProjectChartDto.to_json())

# convert the object into a dict
project_chart_dto_dict = project_chart_dto_instance.to_dict()
# create an instance of ProjectChartDto from a dict
project_chart_dto_from_dict = ProjectChartDto.from_dict(project_chart_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



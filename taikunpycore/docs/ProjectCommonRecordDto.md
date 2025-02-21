# ProjectCommonRecordDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**expired_at** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.project_common_record_dto import ProjectCommonRecordDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCommonRecordDto from a JSON string
project_common_record_dto_instance = ProjectCommonRecordDto.from_json(json)
# print the JSON string representation of the object
print(ProjectCommonRecordDto.to_json())

# convert the object into a dict
project_common_record_dto_dict = project_common_record_dto_instance.to_dict()
# create an instance of ProjectCommonRecordDto from a dict
project_common_record_dto_from_dict = ProjectCommonRecordDto.from_dict(project_common_record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



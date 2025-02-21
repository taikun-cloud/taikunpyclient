# ProjectDetailsErrorListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ProjectDetailsErrorType**](ProjectDetailsErrorType.md) |  | [optional] 
**message** | **List[str]** |  | [optional] 
**kind** | [**ProjectType**](ProjectType.md) |  | [optional] 

## Example

```python
from taikunpycore.models.project_details_error_list_dto import ProjectDetailsErrorListDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDetailsErrorListDto from a JSON string
project_details_error_list_dto_instance = ProjectDetailsErrorListDto.from_json(json)
# print the JSON string representation of the object
print(ProjectDetailsErrorListDto.to_json())

# convert the object into a dict
project_details_error_list_dto_dict = project_details_error_list_dto_instance.to_dict()
# create an instance of ProjectDetailsErrorListDto from a dict
project_details_error_list_dto_from_dict = ProjectDetailsErrorListDto.from_dict(project_details_error_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



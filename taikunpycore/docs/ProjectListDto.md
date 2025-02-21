# ProjectListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from taikunpycore.models.project_list_dto import ProjectListDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectListDto from a JSON string
project_list_dto_instance = ProjectListDto.from_json(json)
# print the JSON string representation of the object
print(ProjectListDto.to_json())

# convert the object into a dict
project_list_dto_dict = project_list_dto_instance.to_dict()
# create an instance of ProjectListDto from a dict
project_list_dto_from_dict = ProjectListDto.from_dict(project_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



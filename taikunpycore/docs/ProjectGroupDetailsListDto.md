# ProjectGroupDetailsListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**organization_id** | **int** |  | 
**organization_name** | **str** |  | 
**projects** | [**List[ProjectListDto]**](ProjectListDto.md) |  | 
**user_groups** | [**List[UserGroupEntityListDto]**](UserGroupEntityListDto.md) |  | 

## Example

```python
from taikunpycore.models.project_group_details_list_dto import ProjectGroupDetailsListDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectGroupDetailsListDto from a JSON string
project_group_details_list_dto_instance = ProjectGroupDetailsListDto.from_json(json)
# print the JSON string representation of the object
print(ProjectGroupDetailsListDto.to_json())

# convert the object into a dict
project_group_details_list_dto_dict = project_group_details_list_dto_instance.to_dict()
# create an instance of ProjectGroupDetailsListDto from a dict
project_group_details_list_dto_from_dict = ProjectGroupDetailsListDto.from_dict(project_group_details_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



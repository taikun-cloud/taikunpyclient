# ProjectGroupEntityListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from taikunpycore.models.project_group_entity_list_dto import ProjectGroupEntityListDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectGroupEntityListDto from a JSON string
project_group_entity_list_dto_instance = ProjectGroupEntityListDto.from_json(json)
# print the JSON string representation of the object
print(ProjectGroupEntityListDto.to_json())

# convert the object into a dict
project_group_entity_list_dto_dict = project_group_entity_list_dto_instance.to_dict()
# create an instance of ProjectGroupEntityListDto from a dict
project_group_entity_list_dto_from_dict = ProjectGroupEntityListDto.from_dict(project_group_entity_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



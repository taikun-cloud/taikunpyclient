# ProjectTemplateDropdownListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**can_commit** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.project_template_dropdown_list_dto import ProjectTemplateDropdownListDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplateDropdownListDto from a JSON string
project_template_dropdown_list_dto_instance = ProjectTemplateDropdownListDto.from_json(json)
# print the JSON string representation of the object
print(ProjectTemplateDropdownListDto.to_json())

# convert the object into a dict
project_template_dropdown_list_dto_dict = project_template_dropdown_list_dto_instance.to_dict()
# create an instance of ProjectTemplateDropdownListDto from a dict
project_template_dropdown_list_dto_from_dict = ProjectTemplateDropdownListDto.from_dict(project_template_dropdown_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



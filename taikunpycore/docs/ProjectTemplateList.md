# ProjectTemplateList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ProjectTemplateListDto]**](ProjectTemplateListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.project_template_list import ProjectTemplateList

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplateList from a JSON string
project_template_list_instance = ProjectTemplateList.from_json(json)
# print the JSON string representation of the object
print(ProjectTemplateList.to_json())

# convert the object into a dict
project_template_list_dict = project_template_list_instance.to_dict()
# create an instance of ProjectTemplateList from a dict
project_template_list_from_dict = ProjectTemplateList.from_dict(project_template_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



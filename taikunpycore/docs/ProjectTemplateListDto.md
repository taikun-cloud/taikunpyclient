# ProjectTemplateListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**monitoring_enabled** | **bool** |  | 
**backup_enabled** | **bool** |  | 
**allow_full_spot_kubernetes** | **bool** |  | 
**allow_spot_vms** | **bool** |  | 
**allow_spot_workers** | **bool** |  | 
**kubernetes_version** | **str** |  | 
**organization_name** | **str** |  | 
**organization_id** | **int** |  | 

## Example

```python
from taikunpycore.models.project_template_list_dto import ProjectTemplateListDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplateListDto from a JSON string
project_template_list_dto_instance = ProjectTemplateListDto.from_json(json)
# print the JSON string representation of the object
print(ProjectTemplateListDto.to_json())

# convert the object into a dict
project_template_list_dto_dict = project_template_list_dto_instance.to_dict()
# create an instance of ProjectTemplateListDto from a dict
project_template_list_dto_from_dict = ProjectTemplateListDto.from_dict(project_template_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



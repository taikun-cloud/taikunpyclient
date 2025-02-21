# ProjectsForBillingDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**created_at** | **datetime** |  | 
**billing_start_date** | **datetime** |  | 
**organization_name** | **str** |  | 
**price** | **float** |  | 
**servers** | [**List[ServersForBillingDto]**](ServersForBillingDto.md) |  | 
**standalone_vms** | [**List[StandaloneVmsForBillingDto]**](StandaloneVmsForBillingDto.md) |  | 
**billing_enabled** | **bool** |  | 

## Example

```python
from taikunpycore.models.projects_for_billing_dto import ProjectsForBillingDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsForBillingDto from a JSON string
projects_for_billing_dto_instance = ProjectsForBillingDto.from_json(json)
# print the JSON string representation of the object
print(ProjectsForBillingDto.to_json())

# convert the object into a dict
projects_for_billing_dto_dict = projects_for_billing_dto_instance.to_dict()
# create an instance of ProjectsForBillingDto from a dict
projects_for_billing_dto_from_dict = ProjectsForBillingDto.from_dict(projects_for_billing_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



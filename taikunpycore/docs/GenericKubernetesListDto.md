# GenericKubernetesListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**project_count** | **int** |  | 
**is_locked** | **bool** |  | 
**name** | **str** |  | 
**main_project** | [**MainProjectDto**](MainProjectDto.md) |  | 
**associated_v_clusters** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**created_by** | **str** |  | 
**created_at** | **str** |  | 
**last_modified** | **str** |  | 
**last_modified_by** | **str** |  | 
**is_default** | **bool** |  | 
**organization_id** | **int** |  | 
**organization_name** | **str** |  | 
**continent_name** | **str** |  | 

## Example

```python
from taikunpycore.models.generic_kubernetes_list_dto import GenericKubernetesListDto

# TODO update the JSON string below
json = "{}"
# create an instance of GenericKubernetesListDto from a JSON string
generic_kubernetes_list_dto_instance = GenericKubernetesListDto.from_json(json)
# print the JSON string representation of the object
print(GenericKubernetesListDto.to_json())

# convert the object into a dict
generic_kubernetes_list_dto_dict = generic_kubernetes_list_dto_instance.to_dict()
# create an instance of GenericKubernetesListDto from a dict
generic_kubernetes_list_dto_from_dict = GenericKubernetesListDto.from_dict(generic_kubernetes_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



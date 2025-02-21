# ListForOrganizationEditDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.list_for_organization_edit_dto import ListForOrganizationEditDto

# TODO update the JSON string below
json = "{}"
# create an instance of ListForOrganizationEditDto from a JSON string
list_for_organization_edit_dto_instance = ListForOrganizationEditDto.from_json(json)
# print the JSON string representation of the object
print(ListForOrganizationEditDto.to_json())

# convert the object into a dict
list_for_organization_edit_dto_dict = list_for_organization_edit_dto_instance.to_dict()
# create an instance of ListForOrganizationEditDto from a dict
list_for_organization_edit_dto_from_dict = ListForOrganizationEditDto.from_dict(list_for_organization_edit_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



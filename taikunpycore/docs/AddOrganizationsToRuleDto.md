# AddOrganizationsToRuleDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **int** |  | [optional] 
**rule_discount_rate** | **float** |  | [optional] 

## Example

```python
from taikunpycore.models.add_organizations_to_rule_dto import AddOrganizationsToRuleDto

# TODO update the JSON string below
json = "{}"
# create an instance of AddOrganizationsToRuleDto from a JSON string
add_organizations_to_rule_dto_instance = AddOrganizationsToRuleDto.from_json(json)
# print the JSON string representation of the object
print(AddOrganizationsToRuleDto.to_json())

# convert the object into a dict
add_organizations_to_rule_dto_dict = add_organizations_to_rule_dto_instance.to_dict()
# create an instance of AddOrganizationsToRuleDto from a dict
add_organizations_to_rule_dto_from_dict = AddOrganizationsToRuleDto.from_dict(add_organizations_to_rule_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# OrganizationSearchCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_term** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.organization_search_command import OrganizationSearchCommand

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationSearchCommand from a JSON string
organization_search_command_instance = OrganizationSearchCommand.from_json(json)
# print the JSON string representation of the object
print(OrganizationSearchCommand.to_json())

# convert the object into a dict
organization_search_command_dict = organization_search_command_instance.to_dict()
# create an instance of OrganizationSearchCommand from a dict
organization_search_command_from_dict = OrganizationSearchCommand.from_dict(organization_search_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



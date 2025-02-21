# OrganizationsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OrganizationDetailsDto]**](OrganizationDetailsDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.organizations_list import OrganizationsList

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationsList from a JSON string
organizations_list_instance = OrganizationsList.from_json(json)
# print the JSON string representation of the object
print(OrganizationsList.to_json())

# convert the object into a dict
organizations_list_dict = organizations_list_instance.to_dict()
# create an instance of OrganizationsList from a dict
organizations_list_from_dict = OrganizationsList.from_dict(organizations_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



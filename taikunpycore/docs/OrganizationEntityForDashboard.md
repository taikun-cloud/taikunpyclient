# OrganizationEntityForDashboard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**users** | **int** |  | 

## Example

```python
from taikunpycore.models.organization_entity_for_dashboard import OrganizationEntityForDashboard

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationEntityForDashboard from a JSON string
organization_entity_for_dashboard_instance = OrganizationEntityForDashboard.from_json(json)
# print the JSON string representation of the object
print(OrganizationEntityForDashboard.to_json())

# convert the object into a dict
organization_entity_for_dashboard_dict = organization_entity_for_dashboard_instance.to_dict()
# create an instance of OrganizationEntityForDashboard from a dict
organization_entity_for_dashboard_from_dict = OrganizationEntityForDashboard.from_dict(organization_entity_for_dashboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



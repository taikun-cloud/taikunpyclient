# OrganizationCreateCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**billing_email** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**vat_number** | **str** |  | [optional] 
**discount_rate** | **float** |  | [optional] 
**is_eligible_update_subscription** | **bool** |  | [optional] 
**admin_cloud_credential_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.organization_create_command import OrganizationCreateCommand

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationCreateCommand from a JSON string
organization_create_command_instance = OrganizationCreateCommand.from_json(json)
# print the JSON string representation of the object
print(OrganizationCreateCommand.to_json())

# convert the object into a dict
organization_create_command_dict = organization_create_command_instance.to_dict()
# create an instance of OrganizationCreateCommand from a dict
organization_create_command_from_dict = OrganizationCreateCommand.from_dict(organization_create_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



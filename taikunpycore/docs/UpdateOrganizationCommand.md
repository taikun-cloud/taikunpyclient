# UpdateOrganizationCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**vat_number** | **str** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**billing_email** | **str** |  | [optional] 
**discount_rate** | **float** |  | [optional] 
**is_eligible_update_subscription** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.update_organization_command import UpdateOrganizationCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrganizationCommand from a JSON string
update_organization_command_instance = UpdateOrganizationCommand.from_json(json)
# print the JSON string representation of the object
print(UpdateOrganizationCommand.to_json())

# convert the object into a dict
update_organization_command_dict = update_organization_command_instance.to_dict()
# create an instance of UpdateOrganizationCommand from a dict
update_organization_command_from_dict = UpdateOrganizationCommand.from_dict(update_organization_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



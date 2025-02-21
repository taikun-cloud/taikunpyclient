# AdminBillingOperationCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_credential_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.admin_billing_operation_command import AdminBillingOperationCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AdminBillingOperationCommand from a JSON string
admin_billing_operation_command_instance = AdminBillingOperationCommand.from_json(json)
# print the JSON string representation of the object
print(AdminBillingOperationCommand.to_json())

# convert the object into a dict
admin_billing_operation_command_dict = admin_billing_operation_command_instance.to_dict()
# create an instance of AdminBillingOperationCommand from a dict
admin_billing_operation_command_from_dict = AdminBillingOperationCommand.from_dict(admin_billing_operation_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



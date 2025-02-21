# AdminAddBalanceCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** |  | [optional] 
**balance** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.admin_add_balance_command import AdminAddBalanceCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AdminAddBalanceCommand from a JSON string
admin_add_balance_command_instance = AdminAddBalanceCommand.from_json(json)
# print the JSON string representation of the object
print(AdminAddBalanceCommand.to_json())

# convert the object into a dict
admin_add_balance_command_dict = admin_add_balance_command_instance.to_dict()
# create an instance of AdminAddBalanceCommand from a dict
admin_add_balance_command_from_dict = AdminAddBalanceCommand.from_dict(admin_add_balance_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



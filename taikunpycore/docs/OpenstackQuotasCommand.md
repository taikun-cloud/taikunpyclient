# OpenstackQuotasCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.openstack_quotas_command import OpenstackQuotasCommand

# TODO update the JSON string below
json = "{}"
# create an instance of OpenstackQuotasCommand from a JSON string
openstack_quotas_command_instance = OpenstackQuotasCommand.from_json(json)
# print the JSON string representation of the object
print(OpenstackQuotasCommand.to_json())

# convert the object into a dict
openstack_quotas_command_dict = openstack_quotas_command_instance.to_dict()
# create an instance of OpenstackQuotasCommand from a dict
openstack_quotas_command_from_dict = OpenstackQuotasCommand.from_dict(openstack_quotas_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



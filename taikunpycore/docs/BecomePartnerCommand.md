# BecomePartnerCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.become_partner_command import BecomePartnerCommand

# TODO update the JSON string below
json = "{}"
# create an instance of BecomePartnerCommand from a JSON string
become_partner_command_instance = BecomePartnerCommand.from_json(json)
# print the JSON string representation of the object
print(BecomePartnerCommand.to_json())

# convert the object into a dict
become_partner_command_dict = become_partner_command_instance.to_dict()
# create an instance of BecomePartnerCommand from a dict
become_partner_command_from_dict = BecomePartnerCommand.from_dict(become_partner_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ContactUsCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**business_email** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.contact_us_command import ContactUsCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ContactUsCommand from a JSON string
contact_us_command_instance = ContactUsCommand.from_json(json)
# print the JSON string representation of the object
print(ContactUsCommand.to_json())

# convert the object into a dict
contact_us_command_dict = contact_us_command_instance.to_dict()
# create an instance of ContactUsCommand from a dict
contact_us_command_from_dict = ContactUsCommand.from_dict(contact_us_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



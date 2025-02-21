# WhiteListDomainCreateCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**white_list_domains** | [**List[WhiteListDomainCreateDto]**](WhiteListDomainCreateDto.md) |  | [optional] 
**partner_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.white_list_domain_create_command import WhiteListDomainCreateCommand

# TODO update the JSON string below
json = "{}"
# create an instance of WhiteListDomainCreateCommand from a JSON string
white_list_domain_create_command_instance = WhiteListDomainCreateCommand.from_json(json)
# print the JSON string representation of the object
print(WhiteListDomainCreateCommand.to_json())

# convert the object into a dict
white_list_domain_create_command_dict = white_list_domain_create_command_instance.to_dict()
# create an instance of WhiteListDomainCreateCommand from a dict
white_list_domain_create_command_from_dict = WhiteListDomainCreateCommand.from_dict(white_list_domain_create_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



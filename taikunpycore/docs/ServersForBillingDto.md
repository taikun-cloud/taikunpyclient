# ServersForBillingDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **int** |  | 
**ram** | **int** |  | 

## Example

```python
from taikunpycore.models.servers_for_billing_dto import ServersForBillingDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServersForBillingDto from a JSON string
servers_for_billing_dto_instance = ServersForBillingDto.from_json(json)
# print the JSON string representation of the object
print(ServersForBillingDto.to_json())

# convert the object into a dict
servers_for_billing_dto_dict = servers_for_billing_dto_instance.to_dict()
# create an instance of ServersForBillingDto from a dict
servers_for_billing_dto_from_dict = ServersForBillingDto.from_dict(servers_for_billing_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



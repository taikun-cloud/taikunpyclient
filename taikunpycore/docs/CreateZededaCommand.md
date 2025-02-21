# CreateZededaCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**api_token** | **str** |  | [optional] 
**api_url** | **str** |  | [optional] 
**project** | **str** |  | [optional] 
**continent** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**edge_nodes** | **List[str]** |  | [optional] 
**public_network** | [**CreateZededaNetworkDto**](CreateZededaNetworkDto.md) |  | [optional] 
**private_network** | [**CreateZededaNetworkDto**](CreateZededaNetworkDto.md) |  | [optional] 

## Example

```python
from taikunpycore.models.create_zededa_command import CreateZededaCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateZededaCommand from a JSON string
create_zededa_command_instance = CreateZededaCommand.from_json(json)
# print the JSON string representation of the object
print(CreateZededaCommand.to_json())

# convert the object into a dict
create_zededa_command_dict = create_zededa_command_instance.to_dict()
# create an instance of CreateZededaCommand from a dict
create_zededa_command_from_dict = CreateZededaCommand.from_dict(create_zededa_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



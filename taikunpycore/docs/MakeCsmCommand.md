# MakeCsmCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.make_csm_command import MakeCsmCommand

# TODO update the JSON string below
json = "{}"
# create an instance of MakeCsmCommand from a JSON string
make_csm_command_instance = MakeCsmCommand.from_json(json)
# print the JSON string representation of the object
print(MakeCsmCommand.to_json())

# convert the object into a dict
make_csm_command_dict = make_csm_command_instance.to_dict()
# create an instance of MakeCsmCommand from a dict
make_csm_command_from_dict = MakeCsmCommand.from_dict(make_csm_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



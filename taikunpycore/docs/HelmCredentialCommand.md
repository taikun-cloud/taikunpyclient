# HelmCredentialCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.helm_credential_command import HelmCredentialCommand

# TODO update the JSON string below
json = "{}"
# create an instance of HelmCredentialCommand from a JSON string
helm_credential_command_instance = HelmCredentialCommand.from_json(json)
# print the JSON string representation of the object
print(HelmCredentialCommand.to_json())

# convert the object into a dict
helm_credential_command_dict = helm_credential_command_instance.to_dict()
# create an instance of HelmCredentialCommand from a dict
helm_credential_command_from_dict = HelmCredentialCommand.from_dict(helm_credential_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



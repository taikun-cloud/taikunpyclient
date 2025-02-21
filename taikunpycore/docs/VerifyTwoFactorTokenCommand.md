# VerifyTwoFactorTokenCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**two_factor_temp_key** | **str** |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.verify_two_factor_token_command import VerifyTwoFactorTokenCommand

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyTwoFactorTokenCommand from a JSON string
verify_two_factor_token_command_instance = VerifyTwoFactorTokenCommand.from_json(json)
# print the JSON string representation of the object
print(VerifyTwoFactorTokenCommand.to_json())

# convert the object into a dict
verify_two_factor_token_command_dict = verify_two_factor_token_command_instance.to_dict()
# create an instance of VerifyTwoFactorTokenCommand from a dict
verify_two_factor_token_command_from_dict = VerifyTwoFactorTokenCommand.from_dict(verify_two_factor_token_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



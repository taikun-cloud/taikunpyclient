# VerifySlackCredentialsCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**channel** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.verify_slack_credentials_command import VerifySlackCredentialsCommand

# TODO update the JSON string below
json = "{}"
# create an instance of VerifySlackCredentialsCommand from a JSON string
verify_slack_credentials_command_instance = VerifySlackCredentialsCommand.from_json(json)
# print the JSON string representation of the object
print(VerifySlackCredentialsCommand.to_json())

# convert the object into a dict
verify_slack_credentials_command_dict = verify_slack_credentials_command_instance.to_dict()
# create an instance of VerifySlackCredentialsCommand from a dict
verify_slack_credentials_command_from_dict = VerifySlackCredentialsCommand.from_dict(verify_slack_credentials_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



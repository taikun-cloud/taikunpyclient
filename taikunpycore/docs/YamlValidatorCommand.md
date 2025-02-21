# YamlValidatorCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**yaml** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.yaml_validator_command import YamlValidatorCommand

# TODO update the JSON string below
json = "{}"
# create an instance of YamlValidatorCommand from a JSON string
yaml_validator_command_instance = YamlValidatorCommand.from_json(json)
# print the JSON string representation of the object
print(YamlValidatorCommand.to_json())

# convert the object into a dict
yaml_validator_command_dict = yaml_validator_command_instance.to_dict()
# create an instance of YamlValidatorCommand from a dict
yaml_validator_command_from_dict = YamlValidatorCommand.from_dict(yaml_validator_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



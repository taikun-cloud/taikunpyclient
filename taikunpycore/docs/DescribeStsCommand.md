# DescribeStsCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.describe_sts_command import DescribeStsCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeStsCommand from a JSON string
describe_sts_command_instance = DescribeStsCommand.from_json(json)
# print the JSON string representation of the object
print(DescribeStsCommand.to_json())

# convert the object into a dict
describe_sts_command_dict = describe_sts_command_instance.to_dict()
# create an instance of DescribeStsCommand from a dict
describe_sts_command_from_dict = DescribeStsCommand.from_dict(describe_sts_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



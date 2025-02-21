# CheckAzureCpuQuotaCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.check_azure_cpu_quota_command import CheckAzureCpuQuotaCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CheckAzureCpuQuotaCommand from a JSON string
check_azure_cpu_quota_command_instance = CheckAzureCpuQuotaCommand.from_json(json)
# print the JSON string representation of the object
print(CheckAzureCpuQuotaCommand.to_json())

# convert the object into a dict
check_azure_cpu_quota_command_dict = check_azure_cpu_quota_command_instance.to_dict()
# create an instance of CheckAzureCpuQuotaCommand from a dict
check_azure_cpu_quota_command_from_dict = CheckAzureCpuQuotaCommand.from_dict(check_azure_cpu_quota_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateAzureCloudCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**azure_subscription_id** | **str** |  | [optional] 
**azure_client_id** | **str** |  | [optional] 
**azure_client_secret** | **str** |  | [optional] 
**azure_tenant_id** | **str** |  | [optional] 
**azure_location** | **str** |  | [optional] 
**az_count** | **int** |  | [optional] 
**organization_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.create_azure_cloud_command import CreateAzureCloudCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAzureCloudCommand from a JSON string
create_azure_cloud_command_instance = CreateAzureCloudCommand.from_json(json)
# print the JSON string representation of the object
print(CreateAzureCloudCommand.to_json())

# convert the object into a dict
create_azure_cloud_command_dict = create_azure_cloud_command_instance.to_dict()
# create an instance of CreateAzureCloudCommand from a dict
create_azure_cloud_command_from_dict = CreateAzureCloudCommand.from_dict(create_azure_cloud_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



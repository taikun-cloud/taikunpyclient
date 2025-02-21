# AzureAksClusterDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_group_name** | **str** |  | [optional] 
**cluster_name** | **str** |  | [optional] 
**location** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.azure_aks_cluster_dto import AzureAksClusterDto

# TODO update the JSON string below
json = "{}"
# create an instance of AzureAksClusterDto from a JSON string
azure_aks_cluster_dto_instance = AzureAksClusterDto.from_json(json)
# print the JSON string representation of the object
print(AzureAksClusterDto.to_json())

# convert the object into a dict
azure_aks_cluster_dto_dict = azure_aks_cluster_dto_instance.to_dict()
# create an instance of AzureAksClusterDto from a dict
azure_aks_cluster_dto_from_dict = AzureAksClusterDto.from_dict(azure_aks_cluster_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



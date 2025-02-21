# DeploymentSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CommonSearchKubernetesResponseData]**](CommonSearchKubernetesResponseData.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.deployment_search_list import DeploymentSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentSearchList from a JSON string
deployment_search_list_instance = DeploymentSearchList.from_json(json)
# print the JSON string representation of the object
print(DeploymentSearchList.to_json())

# convert the object into a dict
deployment_search_list_dict = deployment_search_list_instance.to_dict()
# create an instance of DeploymentSearchList from a dict
deployment_search_list_from_dict = DeploymentSearchList.from_dict(deployment_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



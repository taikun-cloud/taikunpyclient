# SecretSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CommonSearchKubernetesResponseData]**](CommonSearchKubernetesResponseData.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.secret_search_list import SecretSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of SecretSearchList from a JSON string
secret_search_list_instance = SecretSearchList.from_json(json)
# print the JSON string representation of the object
print(SecretSearchList.to_json())

# convert the object into a dict
secret_search_list_dict = secret_search_list_instance.to_dict()
# create an instance of SecretSearchList from a dict
secret_search_list_from_dict = SecretSearchList.from_dict(secret_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



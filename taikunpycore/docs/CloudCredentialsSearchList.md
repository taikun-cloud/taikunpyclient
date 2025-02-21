# CloudCredentialsSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CloudCredentialsResponseData]**](CloudCredentialsResponseData.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.cloud_credentials_search_list import CloudCredentialsSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of CloudCredentialsSearchList from a JSON string
cloud_credentials_search_list_instance = CloudCredentialsSearchList.from_json(json)
# print the JSON string representation of the object
print(CloudCredentialsSearchList.to_json())

# convert the object into a dict
cloud_credentials_search_list_dict = cloud_credentials_search_list_instance.to_dict()
# create an instance of CloudCredentialsSearchList from a dict
cloud_credentials_search_list_from_dict = CloudCredentialsSearchList.from_dict(cloud_credentials_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



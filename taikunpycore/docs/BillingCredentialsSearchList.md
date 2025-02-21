# BillingCredentialsSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CommonSearchResponseData]**](CommonSearchResponseData.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.billing_credentials_search_list import BillingCredentialsSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of BillingCredentialsSearchList from a JSON string
billing_credentials_search_list_instance = BillingCredentialsSearchList.from_json(json)
# print the JSON string representation of the object
print(BillingCredentialsSearchList.to_json())

# convert the object into a dict
billing_credentials_search_list_dict = billing_credentials_search_list_instance.to_dict()
# create an instance of BillingCredentialsSearchList from a dict
billing_credentials_search_list_from_dict = BillingCredentialsSearchList.from_dict(billing_credentials_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



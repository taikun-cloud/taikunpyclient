# OrganizationSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CommonSearchResponseData]**](CommonSearchResponseData.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.organization_search_list import OrganizationSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationSearchList from a JSON string
organization_search_list_instance = OrganizationSearchList.from_json(json)
# print the JSON string representation of the object
print(OrganizationSearchList.to_json())

# convert the object into a dict
organization_search_list_dict = organization_search_list_instance.to_dict()
# create an instance of OrganizationSearchList from a dict
organization_search_list_from_dict = OrganizationSearchList.from_dict(organization_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



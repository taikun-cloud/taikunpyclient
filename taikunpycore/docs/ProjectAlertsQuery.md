# ProjectAlertsQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**mode** | [**ProjectType**](ProjectType.md) |  | [optional] 

## Example

```python
from taikunpycore.models.project_alerts_query import ProjectAlertsQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectAlertsQuery from a JSON string
project_alerts_query_instance = ProjectAlertsQuery.from_json(json)
# print the JSON string representation of the object
print(ProjectAlertsQuery.to_json())

# convert the object into a dict
project_alerts_query_dict = project_alerts_query_instance.to_dict()
# create an instance of ProjectAlertsQuery from a dict
project_alerts_query_from_dict = ProjectAlertsQuery.from_dict(project_alerts_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



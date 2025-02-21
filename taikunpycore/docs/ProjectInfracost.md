# ProjectInfracost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**metadata** | [**ProjectMetadata**](ProjectMetadata.md) |  | [optional] 
**past_breakdown** | [**Breakdown**](Breakdown.md) |  | [optional] 
**breakdown** | [**Breakdown**](Breakdown.md) |  | [optional] 
**diff** | [**Diff**](Diff.md) |  | [optional] 
**summary** | [**Summary**](Summary.md) |  | [optional] 

## Example

```python
from taikunpycore.models.project_infracost import ProjectInfracost

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectInfracost from a JSON string
project_infracost_instance = ProjectInfracost.from_json(json)
# print the JSON string representation of the object
print(ProjectInfracost.to_json())

# convert the object into a dict
project_infracost_dict = project_infracost_instance.to_dict()
# create an instance of ProjectInfracost from a dict
project_infracost_from_dict = ProjectInfracost.from_dict(project_infracost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



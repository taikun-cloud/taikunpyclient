# AdminProjectsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**organization_name** | **str** |  | 
**is_locked** | **bool** |  | 
**kubernetes_current_version** | **str** |  | 
**kubespray_current_version** | **str** |  | 
**status** | [**ProjectStatus**](ProjectStatus.md) |  | 
**servers_count** | **int** |  | 
**tcu** | **int** |  | 
**created_at** | **str** |  | 
**cloud_type** | [**CloudType**](CloudType.md) |  | 

## Example

```python
from taikunpycore.models.admin_projects_response_data import AdminProjectsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of AdminProjectsResponseData from a JSON string
admin_projects_response_data_instance = AdminProjectsResponseData.from_json(json)
# print the JSON string representation of the object
print(AdminProjectsResponseData.to_json())

# convert the object into a dict
admin_projects_response_data_dict = admin_projects_response_data_instance.to_dict()
# create an instance of AdminProjectsResponseData from a dict
admin_projects_response_data_from_dict = AdminProjectsResponseData.from_dict(admin_projects_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



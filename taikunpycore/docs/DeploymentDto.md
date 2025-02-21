# DeploymentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_name** | **str** |  | 
**status** | **str** |  | 
**namespace** | **str** |  | 
**age** | **str** |  | 

## Example

```python
from taikunpycore.models.deployment_dto import DeploymentDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentDto from a JSON string
deployment_dto_instance = DeploymentDto.from_json(json)
# print the JSON string representation of the object
print(DeploymentDto.to_json())

# convert the object into a dict
deployment_dto_dict = deployment_dto_instance.to_dict()
# create an instance of DeploymentDto from a dict
deployment_dto_from_dict = DeploymentDto.from_dict(deployment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



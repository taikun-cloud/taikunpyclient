# NetworkPolicyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_name** | **str** |  | 
**pod_selector** | **Dict[str, str]** |  | 
**namespace** | **str** |  | 
**age** | **str** |  | 

## Example

```python
from taikunpycore.models.network_policy_dto import NetworkPolicyDto

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkPolicyDto from a JSON string
network_policy_dto_instance = NetworkPolicyDto.from_json(json)
# print the JSON string representation of the object
print(NetworkPolicyDto.to_json())

# convert the object into a dict
network_policy_dto_dict = network_policy_dto_instance.to_dict()
# create an instance of NetworkPolicyDto from a dict
network_policy_dto_from_dict = NetworkPolicyDto.from_dict(network_policy_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# OpenstackCredentialList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OpenstackCredentialsListDto]**](OpenstackCredentialsListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.openstack_credential_list import OpenstackCredentialList

# TODO update the JSON string below
json = "{}"
# create an instance of OpenstackCredentialList from a JSON string
openstack_credential_list_instance = OpenstackCredentialList.from_json(json)
# print the JSON string representation of the object
print(OpenstackCredentialList.to_json())

# convert the object into a dict
openstack_credential_list_dict = openstack_credential_list_instance.to_dict()
# create an instance of OpenstackCredentialList from a dict
openstack_credential_list_from_dict = OpenstackCredentialList.from_dict(openstack_credential_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AwsCredentialList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AmazonCredentialsListDto]**](AmazonCredentialsListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.aws_credential_list import AwsCredentialList

# TODO update the JSON string below
json = "{}"
# create an instance of AwsCredentialList from a JSON string
aws_credential_list_instance = AwsCredentialList.from_json(json)
# print the JSON string representation of the object
print(AwsCredentialList.to_json())

# convert the object into a dict
aws_credential_list_dict = aws_credential_list_instance.to_dict()
# create an instance of AwsCredentialList from a dict
aws_credential_list_from_dict = AwsCredentialList.from_dict(aws_credential_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



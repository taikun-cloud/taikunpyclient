# AwsEksNodeGroupDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**ami_type** | **str** |  | [optional] 
**ami_release_version** | **str** |  | [optional] 
**arn** | **str** |  | [optional] 
**capacity_type** | **str** |  | [optional] 
**health_issues** | **List[str]** |  | [optional] 
**status** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**created** | **str** |  | [optional] 
**disk_size** | **int** |  | [optional] 
**desired_size** | **int** |  | [optional] 
**max_size** | **int** |  | [optional] 
**min_size** | **int** |  | [optional] 
**instance_types** | **List[str]** |  | [optional] 

## Example

```python
from taikunpycore.models.aws_eks_node_group_dto import AwsEksNodeGroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of AwsEksNodeGroupDto from a JSON string
aws_eks_node_group_dto_instance = AwsEksNodeGroupDto.from_json(json)
# print the JSON string representation of the object
print(AwsEksNodeGroupDto.to_json())

# convert the object into a dict
aws_eks_node_group_dto_dict = aws_eks_node_group_dto_instance.to_dict()
# create an instance of AwsEksNodeGroupDto from a dict
aws_eks_node_group_dto_from_dict = AwsEksNodeGroupDto.from_dict(aws_eks_node_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



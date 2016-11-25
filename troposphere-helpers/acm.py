import os

from troposphere import Ref, Join, AWS_STACK_NAME, GetAtt
from troposphere.awslambda import Code, Function
from troposphere.cloudformation import CustomResource
from troposphere.iam import ManagedPolicy, Role

module_path = os.path.dirname(__file__)


def global_acm_resources(template, acm_properties):
    """
    Add a function to create a global ACM cert and invoke it for each object in acm_properties
    The obejcts in acp_properties should contain the same properties as when creating a normal
    ACM certificate

    :type acm_properties list
    :rtype tuple
    """
    with open(module_path + '/lambda_code/global_acm.py', 'r') as file:
        acm_code = file.read()

    write_logs_policy = template.add_resource(ManagedPolicy(
        "WriteLogsPolicy",
        Description='Allow Creating Log Group, Log Stream and putting logs in it',
        PolicyDocument={
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Action": [
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                ],
                "Resource": "arn:aws:logs:*:*:*"
            }],
        },
    ))

    global_acm_function_role = template.add_resource(Role(
        "GlobalAcmFunctionRole",
        AssumeRolePolicyDocument={
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Principal": {
                    "Service": "lambda.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }]
        },
        ManagedPolicyArns=[
            Ref(write_logs_policy),
            'arn:aws:iam::aws:policy/AWSCertificateManagerFullAccess'
        ],
    ))

    global_acm_function = template.add_resource(Function(
        "GlobalAcmFunction",
        Code=Code(
            ZipFile=acm_code,
        ),
        Description=Join('', [Ref(AWS_STACK_NAME), ' query service catalog']),
        Handler='index.lambda_handler',
        Role=GetAtt(global_acm_function_role, 'Arn'),
        Runtime='python2.7',
    ))

    output_resources = []
    for i, property in enumerate(acm_properties):
        resource = template.add_resource(CustomResource(
            "GlobalAcmNr{}".format(i),
            ServiceToken=GetAtt(global_acm_function, 'Arn'),
            DomainName=property['DomainName'],
            DomainValidationOptions=property['DomainValidationOptions'],
            SubjectAlternativeNames=property['SubjectAlternativeNames'],

        ))
        output_resources.append(resource)

    return tuple(output_resources)

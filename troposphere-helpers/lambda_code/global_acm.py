import boto3
import cfnresponse
import re


acm = boto3.client('acm', region_name='us-east-1')
not_allowed_in_token = re.compile('[\W]+')


def lambda_handler(event, context):
    resource_id = event.get('PhysicalResourceId', None)
    try:
        request_type = event['RequestType']

        if request_type == "Delete":
            try:
                acm.delete_certificate(CertificateArn=resource_id)
                cfnresponse.send(event, context, cfnresponse.SUCCESS, {}, resource_id)
            except Exception as e:
                cfnresponse.send(event, context, cfnresponse.FAILED, {}, resource_id)
            finally:
                return

        try:
            domain_name = event['ResourceProperties']['DomainName']
        except KeyError as e:
            print("Missing parameter")
            cfnresponse.send(event, context, cfnresponse.FAILED, {}, resource_id)
            raise e
        sans = event['ResourceProperties'].get('SubjectAlternativeNames', None)
        domain_validation_options = event['ResourceProperties'].get('DomainValidationOptions', None)
        idempotency_token = not_allowed_in_token.sub('', context.aws_request_id)[:32]

        response = acm.request_certificate(
            DomainName=domain_name,
            SubjectAlternativeNames=sans,
            IdempotencyToken=idempotency_token,
            DomainValidationOptions=domain_validation_options,
        )

        response_data = {'Arn': response['CertificateArn']}
        resource_id = response['CertificateArn']
        cfnresponse.send(event, context, cfnresponse.SUCCESS, response_data, resource_id)
    except Exception as e:
        cfnresponse.send(event, context, cfnresponse.FAILED, {}, resource_id)
        raise e

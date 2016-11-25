def hosted_zone_map():
    """Map of the AWS Hosted Zone Ids, per region"""

    regions = [
        'us-east-1', 'us-west-1', 'us-west-2', 'ap-south-1', 'ap-northeast-2', 'ap-southeast-1',
        'ap-southeast-2', 'ap-northeast-1', 'eu-central-1', 'eu-west-1', 'sa-east-1',
    ]

    # It's easier to copy paste per service, paste them here as input
    input = {
        'ElasticBeanstalk': {
            'us-east-1': 'Z117KPS5GTRQ2G',
            'us-west-1': 'Z1LQECGX5PH1X',
            'us-west-2': 'Z38NKT9BP95V3O',
            'ap-south-1': 'Z18NTBI3Y7N9TZ',
            'ap-northeast-2': 'Z3JE5OI70TWKCP',
            'ap-southeast-1': 'Z16FZ9L249IFLT',
            'ap-southeast-2': 'Z2PCDNR3VC2G1N',
            'ap-northeast-1': 'Z1R25G3KIG2GBW',
            'eu-central-1': 'Z1FRNW7UH4DEZJ',
            'eu-west-1': 'Z2NYPWQ7DFZAZH',
            'sa-east-1': 'Z10X7K2B4QSOFV',
        },
        'ElasticLoadBalancing': {
            'us-east-1': 'Z35SXDOTRQ7X7K',
            'us-west-1': 'Z368ELLRRE2KJ0',
            'us-west-2': '	Z1H1FL5HABSF5',
            'ap-south-1': '	ZP97RAFLXTNZK',
            'ap-northeast-2': '	ZWKZPGTI48KDX',
            'ap-southeast-1': 'Z1LMS91P8CMLE5',
            'ap-southeast-2': 'Z1GM3OXH4ZPM65',
            'ap-northeast-1': 'Z14GRHDCWA56QT',
            'eu-central-1': 'Z215JYRZR1TBD5',
            'eu-west-1': 'Z32O12XQLNTSW2',
            'sa-east-1': 'Z2P70J7HTTTPLU',
        },
        'CloudFront': {
            'all': 'Z2FDTNDATAQYW2',  # Cloudfront has only one hosted zone id (global service)
        }
    }

    # We transform this to the expected output per region
    output = {}

    for region in regions:
        for service in input:
            if output.get(region, None) is None:
                output[region] = {}
            try:
                output[region][service] = input[service][region]
            except KeyError:
                output[region][service] = input[service]['all']

    return output


def ami_map():
    """Map of the AWS AMIs per region"""
    return {
        'us-east-1': {  # N Virginia
            'AmazonLinux2016090HvmEbs': 'ami-b73b63a0',  # Amazon Linux 2016.09.0 - HVM EBS 64-bit
            'AmazonNat2016090HvmEbs': 'ami-863b6391',
        },
        'us-east-2': {  # Ohio
            'AmazonLinux2016090HvmEbs': 'ami-58277d3d',
            'AmazonNat2016090HvmEbs': 'ami-8d5a00e8',
        },
        'us-west-1': {  # N. California
            'AmazonLinux2016090HvmEbs': 'ami-23e8a343',
            'AmazonNat2016090HvmEbs': 'ami-f4e8a394',
        },
        'us-west-2': {  # Oregon
            'AmazonLinux2016090HvmEbs': 'ami-5ec1673e',
            'AmazonNat2016090HvmEbs': 'ami-d0c066b0',
        },
        'eu-west-1': {  # Ireland
            'AmazonLinux2016090HvmEbs': 'ami-9398d3e0',
            'AmazonNat2016090HvmEbs': 'ami-509dd623',
        },
        'eu-central-1': {  # Frankfurt
            'AmazonLinux2016090HvmEbs': 'ami-f9619996',
            'AmazonNat2016090HvmEbs': 'ami-fd619992',
        },
        'ap-south-1': {  # Mumbai
            'AmazonLinux2016090HvmEbs': 'ami-34b4c05b',
            'AmazonNat2016090HvmEbs': 'ami-93b5c1fc',
        },
        'ap-northeast-1': {  # Tokyo
            'AmazonLinux2016090HvmEbs': 'ami-0c11b26d',
            'AmazonNat2016090HvmEbs': 'ami-c50cafa4',
        },
        'ap-northeast-2': {  # Seoul
            'AmazonLinux2016090HvmEbs': 'ami-983ce8f6',
            'AmazonNat2016090HvmEbs': 'ami-b036e2de',
        },
        'ap-southeast-1': {  # Singapore
            'AmazonLinux2016090HvmEbs': 'ami-b953f2da',
            'AmazonNat2016090HvmEbs': 'ami-df50f1bc',
        },
        'ap-southeast-2': {  # Sydney
            'AmazonLinux2016090HvmEbs': 'ami-db704cb8',
            'AmazonNat2016090HvmEbs': 'ami-ae714dcd',
        },
        'sa-east-1': {  # Sao Paulo
            'AmazonLinux2016090HvmEbs': 'ami-97831ffb',
            'AmazonNat2016090HvmEbs': 'ami-98b824f4',
        },
        'us-gov-west-1': {  # GovCloud
            'AmazonLinux2016090HvmEbs': 'ami-7cb1091d',
            'AmazonNat2016090HvmEbs': 'ami-65a91104',
        },
        'cn-north-1': {  # Beijing
            'AmazonLinux2016090HvmEbs': 'ami-7c15c111',
            'AmazonNat2016090HvmEbs': 'ami-85eb3fe8',
        }
    }

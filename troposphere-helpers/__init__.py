from troposphere import Ref, BaseAWSObject, AWS_NO_VALUE

def no_value():
    """Shortcut to add no value in CloudFormation"""
    return Ref(AWS_NO_VALUE)


def get_resource_name(o):
    """Return the Resource name if o is an BaseAWSObject"""
    return o.title if isinstance(o, BaseAWSObject) else o


class MetadataHelper(object):
    """
    This class helps with template metadata
    """

    def __init__(self, template):
        self.template = template

    def add_parameter_group(self, name, parameters):
        """Add a parameter group to the AWS::CloudFormation::Interface"""
        meta_key = 'AWS::CloudFormation::Interface'
        groups_key = 'ParameterGroups'

        # Make sure the nested dic exists
        if self.template.metadata.get(meta_key) is None:
            self.template.metadata[meta_key] = {}
        if self.template.metadata[meta_key].get(groups_key) is None:
            self.template.metadata[meta_key][groups_key] = []

        parameters = map(lambda x: get_resource_name(x), parameters)

        self.template.metadata[meta_key][groups_key].append({
            'Label': {'default': name},
            'Parameters': parameters
        })

    def add_parameter_label(self, parameter, label):
        """Add a parameter label to the AWS::CloudFormation::Interface"""
        meta_key = 'AWS::CloudFormation::Interface'
        labels_key = 'ParameterLabels'

        # Make sure the nested dict exists
        if self.template.metadata.get(meta_key) is None:
            self.template.metadata[meta_key] = {}
        if self.template.metadata[meta_key].get(labels_key) is None:
            self.template.metadata[meta_key][labels_key] = {}

        parameter = get_resource_name(parameter)

        self.template.metadata[meta_key][labels_key][parameter] = {"default": label}

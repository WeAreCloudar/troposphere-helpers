from troposphere.elasticbeanstalk import OptionSettings


def add_option_settings(dictionary):
    """
    Convert a dictionary with option settings to the format that CloudFormation expects
    :param dictionary: dict
    :return: list
    """
    result = []
    for namespace, options in dictionary.items():
        for name, value in options.items():
            result.append(OptionSettings(
                Namespace=namespace,
                OptionName=name,
                Value=value
            ))
    return result

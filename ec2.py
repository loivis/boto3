import boto3

client = boto3.client('ec2')


def get_image_id(service):
    images = client.describe_images(
        Filters=[{
            'Name': 'tag:Service',
            'Values': [service]
        }],
        Owners=['self'])['Images']
    # print(response)
    images = sorted(images, key=lambda k: k['CreationDate'], reverse=True)
    # for image in images:
    #     print(image)
    image_id = images[-1]
    print image_id['ImageId'], image_id['CreationDate'], image_id['Name']
    return image_id


get_image_id('cassandra')

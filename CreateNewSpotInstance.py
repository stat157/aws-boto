import boto.ec2
conn = boto.ec2.connect_to_region("us-west-1")

# Creates a spot instances request for ten m1.small instances.
conn.request_spot_instances(
    0.005,
    'ami-d383af96',
    count='1',
    key_name='anyuser',
    instance_type='t1.micro',
    security_groups=['default', 'UbuntuServerBasic'])

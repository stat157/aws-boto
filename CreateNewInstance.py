import boto.ec2
conn = boto.ec2.connect_to_region("us-west-1")

conn.run_instances(
    'ami-d383af96',
    key_name='anyuser',
    instance_type='t1.micro',
    security_groups=['default', 'UbuntuServerBasic'])

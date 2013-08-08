import boto.ec2
conn = boto.ec2.connect_to_region("us-west-1",
    aws_access_key_id='YOUR_KEY_ID_HERE',
    aws_secret_access_key='YOUR_SECRET_ACCESS_KEY_HERE')

conn.run_instances(
    'ami-d383af96',
    key_name='anyuser',
    instance_type='t1.micro',
    security_groups=['default', 'UbuntuServerBasic'])

import boto.ec2
conn = boto.ec2.connect_to_region("us-west-2")

conn.run_instances(
    'ami-ace67f9c',
    key_name='throwaway',
    instance_type='t1.micro',
    security_groups=['default'])

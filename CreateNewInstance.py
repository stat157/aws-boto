import boto.ec2
import sys
conn = boto.ec2.connect_to_region("us-west-2")

if conn is None:
	print "ERROR: Could not connect. Perhaps try connecting to one of the following regions"
	print boto.ec2.regions()
	sys.exit(1)

conn.run_instances(
    'ami-ace67f9c',
    key_name='throwaway',
    instance_type='t1.micro',
    security_groups=['default'])

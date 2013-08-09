import boto.ec2.autoscale

conn = boto.ec2.autoscale.connect_to_region('us-west-1')

conn.get_all_groups()

from boto.ec2.autoscale import LaunchConfiguration

from boto.ec2.autoscale import AutoScalingGroup

lc = LaunchConfiguration(
    name='NewAutoScaleGroup',
    image_id='ami-d383af96',
    instance_type='t1.micro',
    key_name='anyuser',
    security_groups=['default', 'UbuntuServerBasic'])

conn.create_launch_configuration(lc)

ag = AutoScalingGroup(group_name='my_group', load_balancers=['my-lb'],
                          availability_zones=['us-west-1'],
                          launch_config=lc, min_size=4, max_size=8,
                          connection=conn)
>>> conn.create_auto_scaling_group(ag)

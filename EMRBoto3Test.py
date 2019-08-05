import os
from pprint import pprint

import boto3

aws_key = ''
aws_skey = ''


class EMR():
    def __init__(self):
        session = boto3.session.Session(region_name='ap-northeast-2')
        self.emr_client = session.client('emr', aws_access_key_id=aws_key, aws_secret_access_key=aws_skey)

    def describe_cluster(self):
        summary = self.emr_client.describe_cluster(ClusterId='j-TPRL610MB0PJ')
        pprint(summary)

    def run_job_flow(self):
        response = self.emr_client.run_job_flow(Name='obkwon-emr-airflow',
                                                LogUri='s3://ap-rnd-emr/log/',
                                                ReleaseLabel='emr-5.25.0',
                                                ServiceRole='EMR_DefaultRole',
                                                JobFlowRole='EMR_EC2_DefaultRole',
                                                VisibleToAllUsers=True,
                                                Applications=[{'Name': 'Spark'}],
                                                Steps=[{
                                                    'Name': 'etl',
                                                    'ActionOnFailure': 'TERMINATE_CLUSTER',
                                                    'HadoopJarStep': {
                                                        'Jar': 's3://ap-northeast-2.elasticmapreduce/libs/script-runner/script-runner.jar',
                                                        'Args': [
                                                            's3://ap-rnd-emr/src/recsys_etl.sh',
                                                        ]
                                                    }
                                                }],
                                                Instances={
                                                    'InstanceGroups': [
                                                        {
                                                            'Name': 'master',
                                                            'Market': 'SPOT',
                                                            'InstanceRole': 'MASTER',
                                                            'InstanceType': 'r3.xlarge',
                                                            'InstanceCount': 1
                                                        },
                                                        {
                                                            'Name': 'slave',
                                                            'Market': 'SPOT',
                                                            'InstanceRole': 'CORE',
                                                            'InstanceType': 'r3.xlarge',
                                                            'InstanceCount': 2
                                                        }],

                                                    'KeepJobFlowAliveWhenNoSteps': False,
                                                    'TerminationProtected': False,
                                                    'Ec2SubnetId': 'subnet-05259f839fce21f8c',
                                                    # 'Ec2KeyName': '<Key pair name>',
                                                    # 'AdditionalMasterSecurityGroups': [
                                                    #     '<additional security group ID>'
                                                    # ]
                                                })
        return response['JobFlowId']

    def describe_cluster(self, job_flow_id):
        return self.emr_client.describe_cluster(ClusterId=job_flow_id)


emr = EMR()
# JobFlowId = emr.run_job_flow()
JobFlowId = 'j-28K7411EE8EDY'
print(emr.describe_cluster(JobFlowId))

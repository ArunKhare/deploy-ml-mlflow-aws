import mlflow.sagemaker as mfs

experiment_id = '1'
run_id = 'e227eda631e0401b8019701fd97f4ec0'
region = 'us-east-1'
aws_id = '741481426945'
arn = 'arn:aws:iam::741481426945:role/aws-sagemaker-for-deploy-ml-model'
app_name = 'model-application'
model_uri = f'mlruns/{experiment_id}/{run_id}/artifacts/random-forest-model'
tag_id = '1.30.0'


image_url = aws_id + '.dkr.ecr.' + region + '.amazonaws.com/mlflow-pyfunc:' + tag_id


mfs.deploy(app_name,
	model_uri=model_uri,
	region_name=region,
	mode='create',
	execution_role_arn=arn,
	image_url=image_url)
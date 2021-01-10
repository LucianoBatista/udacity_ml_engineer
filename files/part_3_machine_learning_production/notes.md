# Topics

- Cloud Computing
- Machine Learning in the Workplace
- Deployment

We will use Amazon SageMaker to deploy our models.

Amazon's SageMaker: Prepare -> Build -> Train and Tune -> **Deploy and Manage**

Question that will be answered in this session:

1. What's the machine learning workflow?
Explore and Process -> Modeling -> Deployment

1. How does deployment fit into the machine learning workflow?
Deploying, monitoring and updating throughout the time.

1. What is cloud computing?
Transformantion of IT products into IT services.

1. Why would we use cloud computing for deploying machine learning models?
- Reduced investments and Proportional Costs
- Increased Scalability
- Increased Availability and Reliability

1. Why isn't deployment a part of many machine learning curriculums?
Because this part of the job is normally associated with Ops and not with Analysts or Data Scientists. But currently we have technologies that bring facilities to deployment and Analysts can done the deployment job too.

1. What does it mean for a model to be deployed?
The integration of the model with the production enviroment existent. And use the inputs of the existing enviroment to output predictions using real world data.

1. What are the essential characteristics associated with the code of deployed models?
- Coded into the programming languange of the production environment
- Coded in Predictive Model Markup Language (PMML) or Portable Format Analytics (PFA)
- Python model is converted into a format that can be used in the production environment

1. What are different cloud computing platforms we might use to deploy our machine learning models?
- AWS, GCP or Azure

# SageMaker

## What is AWS Sagemaker?

AWS (or Amazon) SageMaker is a fully managed service that provides the ability to build, train, tune, deploy, and manage large-scale machine learning (ML) models quickly.

### Tools from Sagemaker

- Ground Truth: To label the jobs, datasets and workforces
- Notebook: To create jupyter notebook instances, configure the lifecycle of the notebooks, and attache git repos
- Training: To choose an ML algo, define the trainig jobs, and tune the hyperparameter
- Inference: To compile and configure the trained models, and endpoints for deployments

### Sagemaker Instances

Sagemaker instances are the dedicated VMs that are optimized to fit different machine learning use cases. The supported instance types, names and pricing in SageMaker are different than that of EC2.

The type of sagemaker instances that are supported varies with aws regions and availability zones.

- **Instances Used here:** ml.t2.medium, ml.m4.xlarge, ml.p2.xlarge (cpu, gpu, for the project)

## Quotes

Service quotes or limits, are the maximum number of service resources or operations for your AWS account.

There are three ways to view your quotas, as mentioned here:
- Service Endpoints and Quotas,
- Service Quotas console,
- AWS CLI commands - list-service-quotas and list-aws-default-service-quotas

We can ask for a new quote limit, Udacity tutorial of how to do that! **[SAVA_AFTER]**

## Sagemaker workflow

Steps needed on SageMaker workflow

**1. set up the notebook**

```
import sagemaker
from sagemaker import get_execution_role # info about IAM role
from sagemaker.amazon.amazon_estimator import get_image_uri # to choose the docker container
from sagemaker.predictor import csv_serializer # serializer to csv files

session = sagemaker.Session() # information about the sassion

role = get_execution_role()

```

2. Preparação e divisão de dados em treino e teste é igual ao que já fazemos

**3. Uploading the data files to S3**

That will be needed by the training job later on.

```
data_dir = '../data/project_folder'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
```

that will upload our data
**session.upload_data**

```
# saving the files into the directory created
X_test.to_csv(os.path.join(data_dir, 'test.csv'), header=False, index=False)

pd.concat([Y_val, X_val], axis=1).to_csv(os.path.join(data_dir, 'validation.csv'), header=False, index=False)
pd.concat([Y_train, X_train], axis=1).to_csv(os.path.join(data_dir, 'train.csv'), header=False, index=False)



prefix = 'project-mlalgo-studos'

test_location = session.upload_data(os.path.join(data_dir, 'test.csv'), key_prefix=prefix)
train_location = session.upload_data(os.path.join(data_dir, 'train.csv'), key_prefix=prefix)
val_location = session.upload_data(os.path.join(data_dir, 'validation.csv'), key_prefix=prefix)
```


**4. Modeling: Train using xgboost built in algo from sagemaker**

```
container = get_image_uri(session.boto_region_name, 'xgboost')

xgb = sagemaker.estimator.Estimator(container,
                                    role,
                                    train_instance_count=1,
                                    train_instance_type='ml.m4.xlarge',
                                    output_path='s3://{}/{}/output'.format(session.default_bucket(), prefix),
                                    sagemaker_session=session)

xgb.set_hyperparameters(max_depth ...) # a lot of hyperparams


s3_input_train = sagemaker.s3_input(s3_data=train_location, content_type='csv')
s3_input_validation = sagemaker.s3_input(s3_data=val_location, content_type='csv')

xgb.fit({'train': s3_input_train, 'validation': s3_input_validation})

```

**Test**

```
xgb_transformer = xgb.transformer(instance_count = 1, instance_type = 'ml.m4.xlarge')

xgb_transformer.transform(test_location, content_type='text/csv', split_type='Line')
xgb_transformer.wait()

```

!aws s3 cp --recursive $xgb_transformer.output_path $data_dir

The last part is to analyse the predictions, ordinary python code.
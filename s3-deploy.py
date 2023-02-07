from flows import pipe
from prefect.deployments import Deployment
from prefect.filesystems import S3

s3 = S3.load("myawsblock")

deploy = Deployment.build_from_flow(
    flow=pipe, name="k8s-generic", storage=s3, infrastructure="kubernetes-job"
)


if __name__ == "__main__":
    deploy.apply()

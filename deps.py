from logflow import log_it
from prefect.deployments import Deployment
from prefect.filesystems import S3
from time import sleep


storage_block = S3(bucket_path="my-first-bucket34")
storage_block.save("myawsblock3", overwrite=True)

deployment = Deployment.build_from_flow(
    flow=log_it,
    name="log_it",
    parameters={"name": "Marvin"},
    infra_overrides={"env": {"PREFECT_LOGGING_LEVEL": "DEBUG"}},
    work_queue_name="staging",
    storage=S3.load("myawsblock3"),
)

if __name__ == "__main__":
    deployment.apply()

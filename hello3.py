from prefect import flow


@flow(retries=3)
def hello():
    print("Hi there!")


if __name__ == "__main__":
    hello()

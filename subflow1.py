import httpx
from prefect import flow


@flow
def fetch_cat_fact():
    return httpx.get("https://catfact.ninja/fact?max_length=140").json()["fact"]


@flow
def fetch_dog_fact():
    return httpx.get(
        "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all"
    ).json()[5]["fact"]


@flow
def animal_facts():
    cat_fact = fetch_cat_fact()
    dog_fact = fetch_dog_fact()
    print(f"š±: {cat_fact} \nš¶: {dog_fact}")


if __name__ == "__main__":
    animal_facts()

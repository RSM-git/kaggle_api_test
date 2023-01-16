import kaggle
import os

os.makedirs("data/raw", exist_ok=True)


def test_download():
    if os.environ.get("KAGGLE_USRENAME") is not None:
        print("Got Kaggle username")

    if os.environ.get("KAGGLE_KEY") is not None:
        print("Got Kaggle key")
    kaggle.api.dataset_download_file("clmentbisaillon/fake-and-real-news-dataset",
                                     "Fake.csv",
                                     path="data/raw/", )
    assert os.path.exists("data/raw/Fake.csv.zip")
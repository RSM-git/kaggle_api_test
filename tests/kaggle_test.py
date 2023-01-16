import kaggle
import os

os.makedirs("data/raw", exist_ok=True)


def test_download():
    kaggle.api.dataset_download_file("clmentbisaillon/fake-and-real-news-dataset",
                                     "Fake.csv",
                                     path="data/raw/", )
    assert os.path.exists("data/raw/Fake.csv.zip")
    assert os.environ.get("KAGGLE_USERNAME") is not None
    assert os.environ.get("KAGGLE_KEY") is not None
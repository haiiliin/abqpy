import os

import fire
import requests


class ReadTheDocsAPI:
    """ReadTheDocs API client"""

    def __init__(self, project: str = "abqpy", token: str = None):
        self.project = project
        self.TOKEN = token or os.environ.get("RTD_TOKEN")
        self.HEADERS = {"Authorization": f"token {self.TOKEN}"}


class ReadTheDocsVersion(ReadTheDocsAPI):
    """Manage versions of a project"""

    def update(self, version: str, *, active: bool = None, hidden: bool = None, privacy_level: str = None):
        """Update status of a version

        Parameters
        ----------
        version : str
            Version to update
        active : bool, optional
            Whether the version is active
        hidden : bool, optional
            Whether the version is hidden
        privacy_level : str, optional
            Privacy level of the version

        Returns
        -------
        Response from the API
        """
        URL = f"https://readthedocs.org/api/v3/projects/{self.project}/versions/{version}/"
        data = {}
        for option in ("active", "hidden", "privacy_level"):
            if locals()[option] is not None:
                data[option] = locals()[option]
        response = requests.patch(URL, json=data, headers=self.HEADERS)
        print(response)


class ReadTheDocs(ReadTheDocsAPI):
    """Manage a project on ReadTheDocs"""

    def __init__(self, project: str = "abqpy", token: str = None):
        super().__init__(project, token)
        self.version = ReadTheDocsVersion(project, token)


if __name__ == "__main__":
    # Print to stdout, a workaround from https://github.com/google/python-fire/issues/188#issuecomment-1528976874
    fire.core.Display = lambda lines, out: out.write("\n".join(lines) + "\n")
    fire.Fire(ReadTheDocs)

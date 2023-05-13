import os
import re

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

    def build(self, version: str):
        """Build a version

        Parameters
        ----------
        version : str
            Version to build
        """
        URL = f"https://readthedocs.org/api/v3/projects/{self.project}/versions/{version}/builds/"
        print(requests.post(URL, headers=self.HEADERS))

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
        """
        URL = f"https://readthedocs.org/api/v3/projects/{self.project}/versions/{version}/"
        data = {}
        for option in ("active", "hidden", "privacy_level"):
            if locals()[option] is not None:
                data[option] = locals()[option]
        print(requests.patch(URL, json=data, headers=self.HEADERS))


class ReadTheDocsRedirect(ReadTheDocsAPI):
    """Manage redirects of a project"""

    def _lists(self) -> requests.Response:
        """List redirects

        Returns
        -------
        Response from the API
        """
        URL = f"https://readthedocs.org/api/v3/projects/{self.project}/redirects/"
        return requests.get(URL, headers=self.HEADERS)

    def update(self, minor_patch: str):
        """Update a redirect from /{lang}/{major} to the latest /{lang}/{major}.{minor}.{patch} version

        Parameters
        ----------
        minor_patch : str
            {minor}.{patch} version to update
        """
        URL = f"https://readthedocs.org/api/v3/projects/{self.project}/redirects/{{pk}}/"
        for redirect in self._lists().json()["results"]:
            url = URL.format(pk=redirect["pk"])
            from_url, to_url = redirect["from_url"], redirect["to_url"]
            lang, pfx, major, minor, patch, sfx = re.match(r"/(\w+)?/([vV]?)(\d+)\.(\d+)\.(\d+)(.+?)", to_url).groups()
            data = dict(url=url, from_url=from_url, to_url=f"/{lang}/{pfx}{major}.{minor_patch}{sfx}", type="exact")
            print(requests.put(url, json=data, headers=self.HEADERS))


class ReadTheDocs(ReadTheDocsAPI):
    """Manage a project on ReadTheDocs"""

    def __init__(self, project: str = "abqpy", token: str = None):
        super().__init__(project, token)
        self.version = ReadTheDocsVersion(project, token)
        self.redirect = ReadTheDocsRedirect(project, token)


if __name__ == "__main__":
    # Print to stdout, a workaround from https://github.com/google/python-fire/issues/188#issuecomment-1528976874
    fire.core.Display = lambda lines, out: out.write("\n".join(lines) + "\n")
    fire.Fire(ReadTheDocs)

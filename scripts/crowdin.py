import os
from datetime import datetime
from pathlib import Path

import fire
import polib
from crowdin_api import CrowdinClient


class FirstCrowdinClient(CrowdinClient):
    TOKEN = os.environ.get("CROWDIN_PERSONAL_TOKEN", None)


class Crowdin:
    """Interact with the Crowdin API."""

    projectId = "586189"
    languageId = "zh-CN"
    root = "docs/source/locales/zh_CN"
    glob_pattern = "LC_MESSAGES/*.po"

    def __init__(self, projectId: int = None, languageId: str = None, root: str = None, glob_pattern: str = None):
        """Initialize the Crowdin API.

        Parameters
        ----------
        projectId : int, optional
            The Crowdin project ID, by default "586189".
        languageId : str, optional
            The Crowdin language ID, by default "zh-CN".
        root : str, optional
            The root directory of the Crowdin translations, by default "docs/source/locales/zh_CN".
        glob_pattern : str, optional
            The glob pattern to match the translation files, by default "LC_MESSAGES/*.po".
        """
        self.projectId = projectId or self.projectId
        self.languageId = languageId or self.languageId
        self.root = root or self.root
        self.glob_pattern = glob_pattern or self.glob_pattern
        self.client = FirstCrowdinClient()

    def _translations(self, limit: int = 500) -> dict[str, str]:
        """List all translations.

        Parameters
        ----------
        limit : int, optional
            The maximum number of translations to return, by default 500. Maximum 500.
        """
        translations = {}
        list_translations = self.client.string_translations.list_language_translations(
            projectId=self.projectId, languageId=self.languageId, limit=limit
        )
        for translation in list_translations["data"]:
            stringId = translation["data"]["stringId"]
            string = self.client.source_strings.get_string(projectId=self.projectId, stringId=stringId)["data"]["text"]
            translation_text = translation["data"]["text"]
            translations[string] = translation_text
        return translations

    def _pofile_entries(self, pofile: polib.POFile) -> dict[str, tuple[int, polib.POEntry]]:  # noqa
        """Return a dictionary of POFile entries.

        Parameters
        ----------
        pofile : polib.POFile
            The POFile to parse.

        Returns
        -------
        dict[str, tuple[int, polib.POEntry]]
            A dictionary of (msgid, (index, entry)) pairs.
        """
        entries = {}
        for index, entry in enumerate(pofile):
            entries[entry.msgid] = (index, entry)
        return entries

    def sync(self):
        """Sync the translations from Crowdin to the local repository."""
        print("Pulling translations from Crowdin...\n")
        translations = self._translations()
        print("Updating local translations...\n")
        for file in Path(self.root).glob(self.glob_pattern):
            print(f"\tUpdating {file}...")
            pofile = polib.pofile(str(file))
            entries = self._pofile_entries(pofile)
            updated = False
            for string, translation in translations.items():
                if string in entries:
                    updated = True
                    index, entry = entries[string]
                    pofile[index].msgstr = translation
            if updated:
                pofile.metadata["PO-Revision-Date"] = datetime.now().strftime("%Y-%m-%d %H:%M%z")
                pofile.metadata["Last-Translator"] = "Crowdin"
                pofile.save()


crowdin = Crowdin()


def main():
    """Interact with the Crowdin API."""
    fire.core.Display = lambda lines, out: out.write("\n".join(lines) + "\n")
    fire.Fire(Crowdin)


if __name__ == "__main__":
    main()

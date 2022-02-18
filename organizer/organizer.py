import os
import pathlib
from typing import List
import json

with open(
    pathlib.Path(os.path.dirname(__file__)) / "extensions.json", "r"
) as extensions:
    EXTENSIONS = json.load(extensions)


class Organizer:

    EXTENSIONS = EXTENSIONS

    def __init__(self, root_dir: pathlib.Path) -> None:
        self._root_dir = root_dir
        self._create_type_directories()

    def _files_in_root_dir(self) -> List[pathlib.Path]:
        return [x for x in self._root_dir.iterdir() if x.is_file()]

    def _create_type_directories(self) -> None:
        for folder_name in Organizer.EXTENSIONS.keys():
            folder_name_path = self._root_dir / folder_name
            folder_name_path.mkdir(exist_ok=True)

    def organize(self) -> None:
        files = self._files_in_root_dir()
        for file in files:
            file_extension = file.suffix
            for folder_name, extension_list in Organizer.EXTENSIONS.items():
                if file_extension in extension_list:
                    file.rename(self._root_dir.resolve() / folder_name / file.name)

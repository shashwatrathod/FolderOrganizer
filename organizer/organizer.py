import os
import pathlib
from typing import List
import json

from organizer.ConflictStrategy import ConflictStrategy

with open(
    pathlib.Path(os.path.dirname(__file__)) / "extensions.json", "r"
) as extensions:
    EXTENSIONS = json.load(extensions)


class Organizer:

    EXTENSIONS = EXTENSIONS

    def __init__(self, root_dir: pathlib.Path, conflict_strategy: ConflictStrategy) -> None:
        self._root_dir = root_dir
        self._create_type_directories()
        self._conflict_strategy = conflict_strategy

    def _files_in_root_dir(self) -> List[pathlib.Path]:
        return [x for x in self._root_dir.iterdir() if x.is_file()]

    def _create_type_directories(self) -> None:
        for folder_name in Organizer.EXTENSIONS.keys():
            folder_name_path = self._root_dir / folder_name
            folder_name_path.mkdir(exist_ok=True)

    def handle_rename_source_strategy(self, filename: str, destination_base_dir: pathlib.Path) -> pathlib.Path:
        """Asks user to input a new name for the conflicting source file.

        Args:
            filename (str): original file name
            destination_base_dir (pathlib.Path): path to the folder where `filename` is supposed to be moved.

        Returns:
            pathlib.Path: new destination path
        """
        file_name_without_extension, extension = os.path.splitext(filename)

        new_name_without_extension = input(f"Please enter a new name for {file_name_without_extension}: ")
        new_name = new_name_without_extension + extension

        return destination_base_dir.joinpath(new_name)
        

    def handle_delete_destination_strategy(self, destination_path: pathlib.Path) -> None:
        """
        Removes the file present at the given destination path if it exists.
        Args:
            destination_path (pathlib.Path): path to the conflicting file that is to be deleted.
        """
        if os.path.exists(str(destination_path)):
            os.remove(str(destination_path))

    def _handle_interactive_conflict_strategy(self) -> ConflictStrategy:
        """
        Displays a menu to the user asking for their choice to resolve the given conflict. Returns the user's choice
        in the form of ConflictStrategy. Defaults to ConflictStrategy.IGNORE in case of BAD user input.
        """
        print(f"""Please choose one of the following options:
    1. Rename the source file.
    2. Delete the file in the destination folder with the same name.
    3. Do not copy this file (default)
    Please enter your choice below:""")
        conflict_choice = input()

        strategy = ConflictStrategy.IGNORE

        if (conflict_choice == "1"):
            strategy = ConflictStrategy.RENAME_SOURCE
        elif (conflict_choice == "2"):
            strategy = ConflictStrategy.DELETE_DESTINATION
        
        return strategy

    
    def organize(self) -> None:
        """
            Copies all the files in self.root_dir to folders in self.root_dir that match their respective types.
        """

        files = self._files_in_root_dir()
        for file in files:
            file_extension = file.suffix
            for folder_name, extension_list in Organizer.EXTENSIONS.items():
                if file_extension in extension_list:
                    destination_base_dir = self._root_dir.resolve().joinpath(folder_name)
                    destination_path = destination_base_dir.joinpath(file.name)

                    if (os.path.exists(destination_path)):

                        print(f"Found a conflict while moving files - file {file.name} already exists in {destination_base_dir}.")

                        strategy = self._conflict_strategy

                        if (strategy == ConflictStrategy.INTERACTIVE):
                            strategy = self._handle_interactive_conflict_strategy()

                        if (strategy == ConflictStrategy.RENAME_SOURCE):
                            destination_path = self.handle_rename_source_strategy(file.name, destination_base_dir)
                            print(f"Moving {file.name} to {destination_path}")
                        elif (strategy == ConflictStrategy.DELETE_DESTINATION):
                            self.handle_delete_destination_strategy(destination_path)
                            print(f"Deleted original file at destination: {destination_path}")
                        else:
                            print(f"Ignoring {file.name}")
                            continue  

                        print("\n")
                
                    file.rename(destination_path)

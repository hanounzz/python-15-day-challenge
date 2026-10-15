from pathlib import Path

from openai import files

downloads = Path("C:\\Users\\Hana Salah\\Downloads")

def check_files (object):
   for file in object.iterdir():
       print(file)

def group_files():
    for file in downloads.iterdir():
        if file.is_file():
            extension=file.suffix
            if extension in [".pdf",".docx",".txt"]:
                new_folder = downloads / "Documents"
                new_folder.mkdir(exist_ok=True)
                file.rename(new_folder / file.name)
            elif extension in [".jpg",".jpeg",".png",".gif"]:
                new_folder = downloads / "Images"
                new_folder.mkdir(exist_ok=True)
                file.rename(new_folder / file.name)
            elif extension in [".mp3",".wav",".flac"]:
                new_folder = downloads / "Audio"
                new_folder.mkdir(exist_ok=True)
                file.rename(new_folder / file.name)
            else:
                new_folder = downloads / "Others"
                new_folder.mkdir(exist_ok=True)
                file.rename(new_folder / file.name)



def group_files_names():
    for file in files.iterdir():
        if file.is_file():
            name=file.stem
            if name in ["german","deutsch","A1","A2","B1","B2","C1","C2","MENSCHEN","NETZWERK","SCHRITT","SICHER","DEUTSCH","SPRACHEN"]:
                new_folder = downloads / "German"
                new_folder.mkdir(exist_ok=True)
                file.rename(new_folder / file.name)
            elif name in["english","english","A1","A2","B1","B2","C1","C2","ENGLISH","LANGUAGE"]:
                new_folder = downloads / "English"
                new_folder.mkdir(exist_ok=True)
                file.rename(new_folder / file.name)
            elif name in ["programming","python","java","c++","javascript"]:
                new_folder = downloads / "Programming"
                new_folder.mkdir(exist_ok=True)
                file.rename(new_folder / file.name)

def main():
    print("Files in Downloads directory:")
    check_files(downloads)
    group_files()

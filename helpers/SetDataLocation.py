import os 

class PathDir:

    def __init__(self):
        self.cwd = os.getcwd()

    def check_file(self) -> bool:
        for file in os.listdir():
            if file.endswith(".artistdata"):
                self.data_path = file
                return True
        return False

    def create_file(self, file_path:str): 
        if self.check_file():
            print(".artistdata already created. If need to change path, do so manually.")
            return None
        
        # Create .artistdata file and put file_path in there.
        with open('.artistdata', 'w') as f:
            f.write(file_path)
    
    def get_path_and_chdir(self):
        if not self.check_file():
            print("Please create .artistdata file. helpers folder for details.")

        os.chdir(self.cwd)
        with open('.artistdata', 'r') as f:
            self.file_path = f.read()
        
        os.chdir(self.file_path)
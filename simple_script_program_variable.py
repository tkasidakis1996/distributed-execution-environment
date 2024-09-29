
class SimpleScriptProgramVariable

    def __init__(self, var_type: str, var_name : str, var_value : str):

        self.my_type : str = var_type

        self.my_name : str = var_name

        self.my_value : str = var_value
    
    def set_value(self, new_value : str) -> None:

        self.my_value = new_value
    
    def get_name(self) -> str:

        return self.my_name
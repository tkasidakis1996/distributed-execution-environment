from simple_script_program_variable import SimpleScriptProgramVariable

class SimpleScriptProgram:

    def __init__(self, program_name : str, program_arguments : list[str]):

        self.my_name : str = program_name

        self.number_of_arguments : int = 1

        self.my_variables : list[SimpleScriptProgramVariable] = []

        for argument in program_arguments:

            argument_variable_name : str = "$arg"+str(self.number_of_arguments)

            program_variable : SimpleScriptProgramVariable = SimpleScriptProgramVariable("string", argument_variable_name, argument)

            self.my_variables.append(program_variable)

            self.number_of_arguments = self.number_of_arguments + 1

        self.my_fd_to_my_code : int = open(self.my_name, "r")

        self.program_counter : int = 0

        self.current_command : str = ""
    
    def next_command(self) -> list[str]:

        while True:
            
            self.current_command = self.my_fd_to_my_code.readline()

            self.program_counter = self.program_counter + 1

            if(self.current_command is not ""):
                break

        parts_of_the_current_command : list[str] = self.current_command.split(" ")

        return parts_of_the_current_command
    
    def update_variable(self, var_name : str, var_value : str) -> None:

        for variable in self.my_variables:

            if(variable.get_name() is var_name):

                variable.set_value(var_value)

                break


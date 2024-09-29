from simple_script_program import SimpleScriptProgram

class SimpleScriptInterpreter:

    def __init__(self):

        self.my_programs : list[SimpleScriptProgram] = []
    
    def receive_a_new_program(self, program_name : str, program_arguments : list[str]) -> None:

        simple_script_program : SimpleScriptProgram = SimpleScriptProgram(program_name, program_arguments)

        self.my_programs.append(simple_script_program)
    
    def run(self):

        for program in self.my_programs

            parts_of_program_command = program.next_command()
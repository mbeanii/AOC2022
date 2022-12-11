class File():
    def __init__(self, size, parent_dir):
        self.size = size
        self.dir  = parent_dir


class Directory():
    def __init__(self, name, parent_dir):
        self.total_size = 0
        self.name = name
        self.parent_dir = parent_dir
        self.child_dirs = {}
        self.files = {}


class Filesystem():
    def __init__(self, input):
        self.master_file_list = []
        self.master_dir_list = []
        self.root_dir = Directory("/", None)
        self.dir_pointer = self.root_dir
        for command in self.read_commands(input):
            self.execute_one(command)
    
    def read_commands(self, input) -> list:
        """ Returns a list of dict commands as:
        [
            {
                command : [output]
            },...
        ]
        """
        commands_list = input.split("$ ")
        commands_list = list(filter(None, commands_list))
        return [{command.splitlines()[0] : command.splitlines()[1:]} for command in commands_list]

    def execute_one(self, command) -> None:
        responses = list(command.values())[0]
        if responses:                           # ls
            for response in responses:
                self.process_ls_response(*response.split(" "))
        else:
            for it in command.keys():           #  cd
                self.execute_cd(it.split(" ")[1])
        return

    def process_ls_response(self, first_word, second_word):
        if first_word == "dir":
            self.add_directory(second_word)
        else:                                   # It's a file
            self.add_file(int(first_word), second_word)
        return

    def execute_cd(self, dir_name):
        if dir_name == "/":
            self.dir_pointer = self.root_dir
            return
        if dir_name == "..":
            self.dir_pointer = self.dir_pointer.parent_dir
            return
        self.dir_pointer = self.dir_pointer.child_dirs[dir_name]
        return

    def add_file(self, size, name):
        if name not in self.dir_pointer.files:
            new_file = File(size, self.dir_pointer)
            self.dir_pointer.files[name] = new_file
            self.master_file_list.append(new_file)
            recursively_update_parent_dir_sizes(self.dir_pointer, size)
        return

    def add_directory(self, name):
        if name not in self.dir_pointer.child_dirs:
            new_dir = Directory(name, self.dir_pointer)
            self.dir_pointer.child_dirs[name] = new_dir
            self.master_dir_list.append(new_dir)
        return
            

def recursively_update_parent_dir_sizes(dir: Directory, size: int):
    if not dir:
        return
    dir.total_size += size
    recursively_update_parent_dir_sizes(dir.parent_dir, size)
    return

with open("Day 7\input.txt", "r") as f:
    input = f.read()
filesystem = Filesystem(input)
sum = sum([x.total_size for x in filesystem.master_dir_list if x.total_size <= 100000])
print(sum)

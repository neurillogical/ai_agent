from functions.get_files_info import get_files_info

def print_format(working_directory: str, directory: str) -> str:
    file_info = get_files_info(working_directory, directory)
    lines = file_info.split("\n")
    
    indented: list[str] = []
    for line in lines:
        indented.append("  " + line)

    if directory == ".":
        current_header = "Result for current directory:"
        return f"{current_header}\n" + "\n".join(indented)
    header = f"Result for '{directory}' directory:"
    return f"{header}\n" + "\n".join(indented)

print(print_format("calculator", "pkg"))
print(print_format("calculator", "/bin"))
print(print_format("calculator", "../"))
print(print_format("calculator", "."))
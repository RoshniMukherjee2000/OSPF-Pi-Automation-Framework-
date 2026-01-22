# from src.connection import execute_command

# out, err = execute_command("hostname")

# print("STDOUT:")
# print(out)

# print("STDERR:")
# print(err)

from src.connection import execute_command

def show_message_on_linux(message):
    """
    Broadcast a message to Linux terminal using wall.
    """
    cmd = f'wall "{message}"'
    out, err = execute_command(cmd)

    if err:
        print("Error:", err)
    else:
        print("Message sent successfully from Windows.")

if __name__ == "__main__":
    show_message_on_linux("HELLO FROM WINDOWS AUTOMATION")

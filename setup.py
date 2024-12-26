from cx_Freeze import setup, Executable

# Replace 'your_script.py' with your main Python script
setup(
    name="LuaNova Estoque",
    version="1.0",
    description="Sistema de controle de estoque",
    executables=[Executable("app.py")]
)

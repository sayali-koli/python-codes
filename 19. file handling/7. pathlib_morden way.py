from pathlib import Path

file = Path("hello.txt")

print(file.exists())
print(file.stat().st_size)
print(file.is_file())
print(file.is_dir())


path = Path("data") / "log" / "app.log"
print(path)

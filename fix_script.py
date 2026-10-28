import io

path = "app/services/ai_assistant_service.py"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Check lines around 693-708
print("Line 694:", repr(lines[693]))
print("Line 695:", repr(lines[694]))
print("Line 707:", repr(lines[706]))

# lines[695:708] are the duplicate lines
# Let's verify and remove them
if 'DATA DATABASE PRIBADI PENGGUNA' in lines[695] and '"""' in lines[706]:
    del lines[695:708]
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.writelines(lines)
    print("Successfully deleted duplicate lines!")
else:
    print("Lines did not match!")

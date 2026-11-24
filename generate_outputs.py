import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
PYTHON = r"C:\Users\HP\AppData\Local\Programs\Python\Python312\python.exe"

samples = [
    ("case_01_employee_payroll.py", "Rajesh Kumar\n75000\n10\n5000\n"),
    ("case_02_retail_billing.py", "3\nRice\n2\n250\ngrocery\nHeadphones\n1\n3500\nelectronics\nPerfume\n2\n1800\nluxury\n"),
    ("case_03_attendance_recovery.py", "60\n38\n"),
    ("case_04_warehouse_inventory.py", "5\nRice Bags\n100\n106\nSugar\n80\n82\nOil Cans\n50\n43\nWheat\n60\n60\nSalt\n25\n18\n"),
    ("case_05_student_performance.py", "3\n4\nAnanya\n85\n82\n78\n88\nBharath\n65\n58\n62\n50\nChitra\n45\n48\n43\n39\n"),
    ("case_06_timetable_conflicts.py", "5\nMathematics\n9\n10\nChemistry\n9\n11\nPhysics\n10\n11\nPython Lab\n14\n16\nEnglish\n15\n16\n"),
    ("case_07_transaction_detection.py", "7\nT001\n500\nAmazon\nT002\n1200\nFlipkart\nT003\n500\nAmazon\nT004\n800\nSwiggy\nT005\n1200\nFlipkart\nT006\n300\nZomato\nT007\n500\nAmazon\n"),
    ("case_08_calendar_generator.py", "7\n2025\n"),
    ("case_09_marks_matrix.py", "4\n4\nAnanya\n85\n90\n78\n88\nBharath\n70\n72\n68\n75\nChitra\n62\n65\n69\n64\nDivya\n92\n95\n89\n83\n"),
    ("case_10_smart_canteen.py", "3\n1\n4\n2\n3\n4\n2\n")
]

os.makedirs(os.path.join(ROOT, "outputs"), exist_ok=True)
os.makedirs(os.path.join(ROOT, "screenshots"), exist_ok=True)

for index, (filename, stdin) in enumerate(samples, 1):
    program = os.path.join(ROOT, "programs", filename)
    result = subprocess.run(
        [PYTHON, program],
        input=stdin,
        text=True,
        capture_output=True,
        cwd=ROOT
    )
    text = result.stdout
    if result.stderr:
        text += "\nERROR:\n" + result.stderr

    output_name = f"case_{index:02d}_output.txt"
    output_path = os.path.join(ROOT, "outputs", output_name)
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)

    lines = text.splitlines() or ["No output"]
    line_height = 24
    width = 1000
    height = max(600, (len(lines) + 4) * line_height)
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("consola.ttf", 17)
        title_font = ImageFont.truetype("consolab.ttf", 18)
    except Exception:
        font = ImageFont.load_default()
        title_font = font

    draw.rectangle((0, 0, width, 42), fill=(20, 24, 31))
    draw.text((18, 10), f"Terminal - {filename}", fill=(255, 255, 255), font=title_font)
    y = 58
    for line in lines:
        draw.text((18, y), line[:150], fill=(20, 20, 20), font=font)
        y += line_height

    screenshot_name = f"case_{index:02d}_{filename.replace('case_', '').replace('.py', '')}.png"
    image.save(os.path.join(ROOT, "screenshots", screenshot_name), optimize=True)

    print(f"Generated {output_name}")

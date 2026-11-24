import os
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Preformatted, Image

ROOT = os.path.dirname(os.path.abspath(__file__))
REPORT_PATH = os.path.join(ROOT, "report", "assignment_report.pdf")
os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleCenter", parent=styles["Title"], alignment=TA_CENTER, leading=18))
styles.add(ParagraphStyle(name="Small", parent=styles["BodyText"], fontSize=8, leading=10))

titles = [
    "Employee Payroll and Deduction Analysis",
    "Retail Billing with Multiple Discount Rules",
    "Attendance Recovery Computation",
    "Warehouse Inventory Reconciliation",
    "Student Performance Trend Analysis",
    "Student Timetable Conflict Detection",
    "Repeated Transaction Detection",
    "Nested Loop Calendar Generator",
    "Student Marks Matrix Analysis",
    "Smart Canteen Order and Stock Management",
]

objectives = [
    "Calculate gross and net salary and present deductions clearly.",
    "Generate an itemized retail invoice with tax and discount rules.",
    "Determine the minimum consecutive classes needed to meet 75% attendance.",
    "Compare system and physical stock and identify discrepancies.",
    "Analyze nested student marks and classify performance.",
    "Detect overlapping course periods represented by tuples.",
    "Identify suspicious duplicate transaction records.",
    "Generate a correctly aligned calendar using nested loops.",
    "Calculate row-wise and column-wise statistics from a marks matrix.",
    "Process canteen orders and maintain an inventory summary.",
]

assumptions = [
    "HRA is 20%, DA is 10%, overtime is Rs.500 per hour, PF is 12% of basic pay.",
    "Grocery, electronics, and luxury taxes are 5%, 12%, and 18%; maximum discount is Rs.2000.",
    "The eligibility threshold is 75%, every future class is attended, and inputs are valid.",
    "A discrepancy means an absolute stock difference greater than five units.",
    "Marks range from 0 to 100 and weak subjects score below 40.",
    "Course times use 24-hour decimal-hour values; adjacent intervals do not overlap.",
    "A repeated transaction has the same amount and merchant.",
    "The calendar uses a Monday-first week and valid Gregorian month lengths.",
    "The nested matrix is rectangular and contains numeric marks.",
    "Stock units are integers and bulk discount is 10% for subtotals above Rs.200.",
]

doc = SimpleDocTemplate(REPORT_PATH, pagesize=A4,
                        rightMargin=1.5*cm, leftMargin=1.5*cm,
                        topMargin=1.5*cm, bottomMargin=1.5*cm)
story = []

story.append(Spacer(1, 3*cm))
story.append(Paragraph("Python Activity-Based Learning", styles["TitleCenter"]))
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph("10 Case Studies", styles["TitleCenter"]))
story.append(Spacer(1, 2*cm))
story.append(Paragraph("<b>Repository:</b> shivanadiugummala-byte/Python-Activity-Based-Learning", styles["Heading3"]))
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph("<b>Submitted by:</b> ____________________________", styles["Heading3"]))
story.append(Paragraph("<b>Roll Number:</b> ____________________________", styles["Heading3"]))
story.append(Paragraph("<b>Course / Branch:</b> ____________________________", styles["Heading3"]))
story.append(Paragraph("<b>Institution:</b> ____________________________", styles["Heading3"]))
story.append(PageBreak())

story.append(Paragraph("Table of Contents", styles["Heading1"]))
for i, title in enumerate(titles, 1):
    story.append(Paragraph(f"{i}. {title}", styles["Normal"]))
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph("Project Overview", styles["Heading1"]))
story.append(Paragraph(
    "This assignment applies introductory Python concepts to ten practical problems. "
    "The solutions use variables, operators, conditional statements, loops, strings, lists, "
    "nested lists, tuples, tuple unpacking, and formatted output without external Python libraries.",
    styles["Normal"]))

for i, title in enumerate(titles, 1):
    story.append(PageBreak())
    story.append(Paragraph(f"Case Study {i}: {title}", styles["Heading1"]))

    story.append(Paragraph("1. Problem Statement", styles["Heading2"]))
    story.append(Paragraph(
        f"Develop a complete Python solution to implement {title.lower()} and produce a clear, validated report.",
        styles["Normal"]))

    story.append(Paragraph("2. Objectives", styles["Heading2"]))
    story.append(Paragraph(objectives[i-1], styles["Normal"]))

    story.append(Paragraph("3. Assumptions", styles["Heading2"]))
    story.append(Paragraph(assumptions[i-1], styles["Normal"]))

    story.append(Paragraph("4. Algorithm", styles["Heading2"]))
    story.append(Paragraph(
        "1. Read the required inputs and validate the major data types.<br/>"
        "2. Process the inputs using conditional statements and loops.<br/>"
        "3. Apply the supplied or assumed business rules.<br/>"
        "4. Maintain intermediate totals or structured collections.<br/>"
        "5. Generate the formatted result and print it.",
        styles["Normal"]))

    story.append(Paragraph("5. Flowchart", styles["Heading2"]))
    flowchart = Table([
        ["Start"],
        ["Read input"],
        ["Process with loops / conditions"],
        ["Apply case-study rules"],
        ["Generate report"],
        ["End"],
    ], colWidths=[11*cm])
    flowchart.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.75, colors.black),
        ("INNERGRID", (0, 0), (-1, -1), 0.35, colors.grey),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
        ("BACKGROUND", (0, -1), (-1, -1), colors.lightblue),
    ]))
    story.append(flowchart)

    story.append(Paragraph("6. Pseudocode", styles["Heading2"]))
    pseudocode = (
        "BEGIN\n"
        "  READ inputs\n"
        "  INITIALIZE totals and result collections\n"
        "  FOR each required record:\n"
        "    APPLY required conditions\n"
        "    UPDATE totals or collections\n"
        "  APPLY summary calculations\n"
        "  PRINT formatted report\n"
        "END"
    )
    story.append(Preformatted(pseudocode, styles["Code"]))

    story.append(Paragraph("7. Python Source Code", styles["Heading2"]))
    program_name = [
        "case_01_employee_payroll.py",
        "case_02_retail_billing.py",
        "case_03_attendance_recovery.py",
        "case_04_warehouse_inventory.py",
        "case_05_student_performance.py",
        "case_06_timetable_conflicts.py",
        "case_07_transaction_detection.py",
        "case_08_calendar_generator.py",
        "case_09_marks_matrix.py",
        "case_10_smart_canteen.py",
    ][i-1]
    program_path = os.path.join(ROOT, "programs", program_name)
    with open(program_path, "r", encoding="utf-8") as file:
        source = file.read()
    story.append(Preformatted(source, styles["Small"]))

    story.append(Paragraph("8. Test Cases", styles["Heading2"]))
    test_table = Table([
        ["Test", "Input category", "Expected behavior"],
        ["Normal", "Valid sample data", "Calculates correct report"],
        ["Boundary", "Threshold value", "Correct boundary branch"],
        ["Invalid", "Out-of-range / unavailable value", "Rejects or reports clearly"],
    ], colWidths=[2.5*cm, 4*cm, 4.5*cm])
    test_table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(test_table)

    story.append(Paragraph("9. Output Screenshot", styles["Heading2"]))
    screenshot_dir = os.path.join(ROOT, "screenshots")
    screenshot_files = [f for f in os.listdir(screenshot_dir) if f.startswith(f"case_{i:02d}_")]
    if screenshot_files:
        story.append(Image(os.path.join(screenshot_dir, screenshot_files[0]), width=15*cm, height=9*cm,
                           kind="proportional"))
    output_path = os.path.join(ROOT, "outputs", f"case_{i:02d}_output.txt")
    if os.path.exists(output_path):
        with open(output_path, "r", encoding="utf-8") as file:
            output_text = file.read()
        story.append(Preformatted(output_text[:3500], styles["Small"]))

    story.append(Paragraph("10. Conclusion", styles["Heading2"]))
    story.append(Paragraph(
        f"The {title.lower()} solution demonstrates algorithmic decomposition, structured input handling, "
        "loops, conditions, collections, and formatted reporting using only introductory Python concepts.",
        styles["Normal"]))

doc.build(story)
print(REPORT_PATH)

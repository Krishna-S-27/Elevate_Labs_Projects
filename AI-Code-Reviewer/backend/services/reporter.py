import os
import time
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf_report(language: str, code: str, report_path: str = None):
    """
    Generate a PDF report for the given code.
    Saves it at `report_path` (if provided), otherwise generates a default path.
    """

    reports_dir = os.path.join("backend", "reports")
    os.makedirs(reports_dir, exist_ok=True)

    if report_path is None:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        report_path = os.path.join(reports_dir, f"code_review_report_{language}_{timestamp}.pdf")

    doc = SimpleDocTemplate(report_path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph(f"<b>AI Code Review Report</b>", styles["Title"]))
    story.append(Spacer(1, 20))

    story.append(Paragraph(f"<b>Language:</b> {language}", styles["Normal"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph(f"<b>Generated:</b> {time.ctime()}", styles["Normal"]))
    story.append(Spacer(1, 20))

    story.append(Paragraph("<b>Submitted Code:</b>", styles["Heading2"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(f"<pre>{code}</pre>", styles["Code"]))
    story.append(Spacer(1, 20))

    story.append(Paragraph("<b>AI Review:</b>", styles["Heading2"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph("This is a placeholder AI review. Integrate your real analysis output here.", styles["Normal"]))

    doc.build(story)

    return report_path

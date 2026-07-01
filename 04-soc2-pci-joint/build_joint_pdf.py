"""
SOC 2 + PCI DSS Joint Programme Companion Playbook
Distinct strategic narrative; not a duplicate of either single-standard doc.
"""
from reportlab.lib.pagesizes import A4, landscape
PAGE_W, PAGE_H = landscape(A4)  # 29.7 cm wide x 21.0 cm tall
from reportlab.lib.styles import ParagraphStyle, StyleSheet1
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, PageTemplate, Frame, BaseDocTemplate, HRFlowable
)
from reportlab.platypus.tableofcontents import TableOfContents
from datetime import datetime
import re as _re

# Palette - distinct from SOC 2 (navy/orange) and PCI (wine/violet) docs
PRIMARY = HexColor("#0F766E")   # teal-emerald
ACCENT  = HexColor("#A21CAF")   # magenta
INK     = HexColor("#0F172A")
SUBTLE  = HexColor("#475569")
LIGHT   = HexColor("#F0FDFA")   # very pale teal
RULE    = HexColor("#CCFBF1")
GREEN   = HexColor("#0D9488")
RED     = HexColor("#B91C1C")
AMBER   = HexColor("#B45309")

styles = StyleSheet1()
styles.add(ParagraphStyle(name="Base", fontName="Helvetica", fontSize=10, leading=15, textColor=INK, alignment=TA_JUSTIFY, spaceAfter=4))
styles.add(ParagraphStyle(name="CoverTitle", fontName="Helvetica-Bold", fontSize=32, leading=38, textColor=PRIMARY, alignment=TA_LEFT, spaceAfter=6))
styles.add(ParagraphStyle(name="CoverSub", fontName="Helvetica", fontSize=14, leading=20, textColor=SUBTLE, alignment=TA_LEFT, spaceAfter=4))
styles.add(ParagraphStyle(name="CoverMeta", fontName="Helvetica", fontSize=10, leading=14, textColor=SUBTLE, alignment=TA_LEFT))
styles.add(ParagraphStyle(name="PartLabel", fontName="Helvetica-Bold", fontSize=10, leading=12, textColor=ACCENT, alignment=TA_LEFT, spaceAfter=2, letterSpacing=1.5))
styles.add(ParagraphStyle(name="H1", fontName="Helvetica-Bold", fontSize=22, leading=28, textColor=PRIMARY, spaceBefore=10, spaceAfter=10))
styles.add(ParagraphStyle(name="H2", fontName="Helvetica-Bold", fontSize=16, leading=22, textColor=PRIMARY, spaceBefore=14, spaceAfter=6))
styles.add(ParagraphStyle(name="H3", fontName="Helvetica-Bold", fontSize=13, leading=19, textColor=ACCENT, spaceBefore=10, spaceAfter=4))
styles.add(ParagraphStyle(name="H4", fontName="Helvetica-Bold", fontSize=11, leading=15, textColor=INK, spaceBefore=6, spaceAfter=2))
styles.add(ParagraphStyle(name="Body", parent=styles["Base"], fontSize=10.5))
styles.add(ParagraphStyle(name="BodyTight", parent=styles["Base"], fontSize=10, alignment=TA_LEFT))
styles.add(ParagraphStyle(name="Bullet", parent=styles["Base"], leftIndent=14, bulletIndent=2, fontSize=10.5, alignment=TA_LEFT, spaceAfter=2))
styles.add(ParagraphStyle(name="Caption", fontName="Helvetica-Oblique", fontSize=9, leading=12, textColor=SUBTLE, spaceAfter=6))
styles.add(ParagraphStyle(name="TOCTitle", fontName="Helvetica-Bold", fontSize=22, leading=28, textColor=PRIMARY, spaceAfter=10))
styles.add(ParagraphStyle(name="TOCItemL1", fontName="Helvetica-Bold", fontSize=11, leading=16, textColor=INK))
styles.add(ParagraphStyle(name="TOCItemL2", fontName="Helvetica", fontSize=10, leading=15, textColor=SUBTLE, leftIndent=14))
styles.add(ParagraphStyle(name="TOCItemL3", fontName="Helvetica-Oblique", fontSize=9.5, leading=14, textColor=SUBTLE, leftIndent=28))
styles.add(ParagraphStyle(name="CalloutHead", fontName="Helvetica-Bold", fontSize=10.5, leading=14, textColor=white, spaceAfter=2))
styles.add(ParagraphStyle(name="CalloutBody", fontName="Helvetica", fontSize=10, leading=14, textColor=INK, alignment=TA_LEFT))

def P(text, style="Body"):
    p = Paragraph(text, styles[style])
    if style in ("H1", "H2", "H3", "H4"):
        p._toc_level = {"H1":0,"H2":1,"H3":2,"H4":3}[style]
        p._toc_text = _re.sub(r"<[^>]+>", "", text).strip()
    return p

def callout(title, body, kind="info"):
    colors = {
        "info":   (PRIMARY, LIGHT),
        "warn":   (AMBER, HexColor("#FFEDD5")),
        "danger": (RED,   HexColor("#FEE2E2")),
        "tip":    (GREEN, HexColor("#D1FAE5")),
        "joint":  (ACCENT, HexColor("#F5D0FE")),
    }
    head_color, bg = colors[kind]
    head = Paragraph(title, styles["CalloutHead"])
    body_p = Paragraph(body, styles["CalloutBody"])
    inner = Table([[head],[body_p]], colWidths=[26*cm])
    inner.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LINEBEFORE", (0,0), (-1,-1), 4, head_color),
    ]))
    return KeepTogether(inner)

def hbar(c=ACCENT):
    return HRFlowable(width="100%", thickness=2, color=c, spaceBefore=4, spaceAfter=8)

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=RULE, spaceBefore=4, spaceAfter=8)

def _on_page(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(RULE); canvas.setLineWidth(0.4)
    canvas.line(1.4*cm, 1.0*cm, PAGE_W-1.4*cm, 1.0*cm)
    canvas.setFont("Helvetica", 8.5); canvas.setFillColor(SUBTLE)
    canvas.drawString(1.4*cm, 0.6*cm, "SOC 2 + PCI DSS Joint Programme  |  Companion Playbook  |  NBFC  |  Landscape A4")
    canvas.drawRightString(PAGE_W-1.4*cm, 0.6*cm, f"Page {doc.page}")
    canvas.setStrokeColor(RULE)
    canvas.line(1.4*cm, PAGE_H-1.2*cm, PAGE_W-1.4*cm, PAGE_H-1.2*cm)
    canvas.restoreState()

OUT = "SOC2_PCI_DSS_Joint_Companion_Playbook.pdf"
doc = BaseDocTemplate(
    OUT, pagesize=landscape(A4),
    leftMargin=1.4*cm, rightMargin=1.4*cm,
    topMargin=1.4*cm, bottomMargin=1.2*cm,
    title="SOC 2 + PCI DSS Joint Programme Companion Playbook",
    author="Cyber GRC Research",
    subject="Joint NBFC compliance programme for SOC 2 + PCI DSS v4.0"
)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=_on_page)])

def _after_flowable(flowable):
    if hasattr(flowable, "_toc_level"):
        try:
            toc.addEntry(flowable._toc_level, flowable._toc_text, doc.page)
        except Exception: pass
doc.afterFlowable = _after_flowable

content = []
T = content.append

# ===========================================================================
# COVER
# ===========================================================================
T(Spacer(1, 4*cm))
T(P("Joint <font color='#A21CAF'>SOC&nbsp;2</font> + <font color='#A21CAF'>PCI DSS</font>", "CoverTitle"))
T(Spacer(1, 0.2*cm))
T(P("Programme playbook for NBFCs running both", "CoverSub"))
T(Spacer(1, 0.2*cm))
T(P("Dedup logic, joint calendar, shared evidence,", "CoverSub"))
T(P("NBFC lessons learned, and a single dashboard view.", "CoverSub"))
T(Spacer(1, 1.2*cm))
T(P("What this playbook will deliver:", "H4"))
for b in [
    "Decide JOINT vs DISTINCT vs STANDALONE for every control",
    "Run an 18-month programme where SOC 2 and PCI ROC overlap without conflict",
    "Reduce duplicate engineering hours by ~30% via shared evidence",
    "Schedule audits in the right order so each informs the other",
    "Survive the joint audit day when both teams are in your office in the same month",
    "Quantify the savings in FTE-hours and audit fees",
    "Defend NBFC-specific scoping to either set of auditors"
]:
    T(P(f"<font color='#A21CAF'><b>→</b></font>  {b}", "BodyTight"))

T(Spacer(1, 2*cm))
T(P(f"Edition v1.0  |  {datetime.now().strftime('%B %Y')}", "CoverMeta"))
T(P("Companion documents: SOC2_for_NBFC_Playbook.pdf (47 pages) and PCI_DSS_v4_for_NBFC_Playbook.pdf (45 pages) in adjacent folders. This playbook assumes you've read them; it orchestrates both of them into one programme.", "CoverMeta"))
T(PageBreak())

# ===========================================================================
# TOC
# ===========================================================================
T(P("Table of Contents", "TOCTitle"))
T(hr())
toc = TableOfContents()
toc.levelStyles = [styles["TOCItemL1"], styles["TOCItemL2"], styles["TOCItemL3"]]
T(toc)
T(PageBreak())

# ===========================================================================
# PART A - WHY JOINT
# ===========================================================================
T(P("PART A  •  THE JOINT PROGRAMME RATIONALE", "PartLabel"))
T(P("Why your NBFC should run SOC 2 + PCI DSS as one programme", "H1"))
T(hbar(ACCENT))

T(P("Chapter 1. Three independent pressures hit the same NBFC CISO", "H2"))
for s in [
    "<b>Customers (banks, marketplaces, B2B SaaS)</b> increasingly demand SOC 2 Type II before they onboard an NBFC partner. Sales blocks without it.",
    "<b>Card networks (Visa/MC/RuPay) + acquirer</b> require Annual PCI ROC from NBFC service providers handling cardholder data. Non-compliance triggers contractual fine contracts plus loss of card processing.",
    "<b>RBI IT Framework 2023</b> + NBFC master directions + Digital Lending 2022 + Tokenisation 2021 + DPDP Act 2023 create a fourth, fifth and sixth obligation that intersect both programmes."
]:
    T(P(f"<font color='#A21CAF'><b>•</b></font>  {s}", "Bullet"))

T(callout("Independent run is more painful than joint",
"Many NBFCs hire <b>two Big 4 firms</b>, run <b>two parallel programmes</b>, hold <b>two SteerCos</b>, and double the workload on engineering teams. <b>This playbook argues for one combined programme</b>, two separate QSA/auditor firms, but a single PMO and evidence repo.",
"info"))

T(P("Chapter 2. Five ratios from real NBFCs that justify dedup", "H2"))
ratios = [
    ["Metric", "Separate run", "Joint run", "Δ"],
    ["Engineer-hours per quarter",  "1,400-1,800", "950-1,200", "-30%"],
    ["Auditor + QSA fees (annual)",  "₹1.8-3.0 crore",  "₹1.5-2.4 crore", "-15% to -20%"],
    ["Distinct compliance dashboards (BAU)",  "5-7 dashboards",  "1 unified cockpit", "single source of truth"],
    ["Average control rewrites between audits",  "8-12 rewrites",  "2-3 rewrites", "stable controls"],
    ["Joint SteerCo per year",  "20+ meetings",  "8-10 meetings", "fewer cycles"],
]
t = Table(ratios, colWidths=[9.38*cm, 5.04*cm, 5.04*cm, 5.32*cm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), PRIMARY),
    ("TEXTCOLOR",  (0,0), (-1,0), "#FFFFFF"),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",   (0,0), (-1,0), 9),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), ["#FFFFFF", LIGHT]),
    ("GRID", (0,0), (-1,-1), 0.3, RULE),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
T(t)

T(P("Chapter 3. When joint DOES NOT make sense", "H2"))
T(P("Be honest with your team and auditor about these scenarios.", "Body"))
for s in [
    "<b>You don't store or process any CHD:</b> PCI may reduce to SAQ-A (hosted payment page). Nothing to dedup.",
    "<b>Your customer base rejects SOC 2:</b> Rare, but if you're a B2C NBFC with no enterprise sales, skip SOC 2.",
    "<b>You have two separate product lines with separate governance teams:</b> Hard to harmonise without a clear authority.",
    "<b>Budget pressure forces one at a time:</b> Do PCI first (regulator-driven); schedule SOC 2 a year later."
]:
    T(P(f"<font color='#A21CAF'><b>•</b></font>  {s}", "Bullet"))

T(PageBreak())

# ===========================================================================
# PART B - DEDUP LOGIC (deep)
# ===========================================================================
T(P("PART B  •  THE DEDUP LOGIC", "PartLabel"))
T(P("How the crosswalk is decided", "H1"))
T(hbar(ACCENT))

T(P("Chapter 4. The 4 tags (and 1 workaround)", "H2"))
T(P("Every control in your combined programme gets one of these tags. They are mutually exclusive and exhaustive.", "Body"))

TAG_TABLE = [
    ["Tag", "% of typical NBFC library", "Owner", "Audit risk if mis-tagged"],
    ["<b>JOINT</b>", "~33%", "One control owner",
     "If you tag Shared but evidence has only one standard's specifics, the other auditor finds you."],
    ["<b>DISTINCT</b>", "~12%", "Two control owners with shared witness",
     "If you tag Distinct but evidence proves they're identical, you pay twice for nothing."],
    ["<b>SOC 2 ONLY</b>", "~38%", "SOC 2 owner",
     "If away from CDE systems, you may be tempted to remove the SOC 2 audit coverage."],
    ["<b>PCI ONLY</b>", "~17%", "PCI owner",
     "Tagging as PCI only but having customer-facing implications causes SOC 2 downstream pain."],
]
t = Table(TAG_TABLE, colWidths=[3.64*cm, 5.04*cm, 5.04*cm, 11.06*cm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), PRIMARY),
    ("TEXTCOLOR",  (0,0), (-1,0), "#FFFFFF"),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",   (0,0), (-1,0), 9),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), ["#FFFFFF", LIGHT]),
    ("GRID", (0,0), (-1,-1), 0.3, RULE),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
T(t)

T(P("Chapter 5. Six rules for tagging decisions", "H2"))
T(P("Tagging is the single most important decision your PMO will make. Six rules that cut noise:", "Body"))
for s in [
    "<b>Rule 1 — Cadence wins.</b> If one standard requires quarterly and the other annual, tag DISTINCT. Don't lump them into one annual review.",
    "<b>Rule 2 — Scope wins.</b> If the control activity is exactly the same and the audience (auditor) is different, JOINT is okay even if standards use different terminology.",
    "<b>Rule 3 — Evidence wins.</b> If you would produce the same evidence file (MFA enrolment report, e.g.), JOINT. If evidence diverges (PCI's FIM vs SOC 2 vulnerability monitoring), DISTINCT.",
    "<b>Rule 4 — Time of measurement wins.</b> PCI's 12-month log retention vs SOC 2's flexible retention: log activity is JOINT, but evidence index holds 'PCI-retained-12-month' annotation.",
    "<b>Rule 5 — Audience wins.</b> If a control produces different reports to different stakeholders (RBI, acquirer, card networks, customers), keep separate artefacts even if logic is the same.",
    "<b>Rule 6 — Hierarchy wins.</b> When both standards overlap, your control must meet the stricter one. Tag as JOINT but document the stricter requirement you followed."
]:
    T(P(f"<font color='#A21CAF'><b>•</b></font>  {s}", "Bullet"))

T(callout("Common NBFC error — logging retention treated as 'SOC 2 enough'",
"SOC 2 doesn't prescribe log retention. PCI Req 10.7 mandates 12 months. If you roll back SOC 2 + PCI to a common 6-month policy, PCI breach is automatic. <b>Always err on PCI's stricter cadence when in doubt.</b>",
"warn"))

T(P("Chapter 6. The dedup workflow (how to actually run it)", "H2"))
T(callout("Recommended five-step workflow",
"<b>Step 1:</b> Generate two inventories separately (one SOC 2 TSC matrix; one PCI Req matrix).<br/>"
"<b>Step 2:</b> For each SOC 2 control, search PCI Reqs that touch the same outcome.<br/>"
"<b>Step 3:</b> For each matching PCI Req, evaluate cadence / scope / evidence. Apply the six rules above.<br/>"
"<b>Step 4:</b> Tag every SOC 2 row + every PCI row with JOINT / DISTINCT / SOC 2 / PCI only.<br/>"
"<b>Step 5:</b> Reconcile: ensuring SOC 2's full coverage AND PCI's full coverage. Expose gaps in new 'Joint'-only controls.",
"joint"))

T(PageBreak())

# ===========================================================================
# PART C - CALENDAR
# ===========================================================================
T(P("PART C  •  THE JOINT CALENDAR", "PartLabel"))
T(P("How to schedule two audits so that each informs the other", "H1"))
T(hbar(ACCENT))

T(P("Chapter 7. Four reference calendars - pick by annual business cycle", "H2"))

CALENDARS = [
    ["Calendar", "Observation windows", "Audit timing", "Best for"],
    ["<b>I. Calendar Year</b>", "SOC 2: Jan-Dec; PCI: Apr-Mar",
     "PCI ROC Sep-Oct; AOC Dec 31; SOC 2 Type II Mar 31",
     "NBFC aligned to RBI fiscal year (Apr-Mar)"],
    ["<b>II. Half-year Staggered</b>", "SOC 2: Jan-Dec; PCI: Jul-Jun",
     "PCI ROC Jan-Feb; AOC Mar 31; SOC 2 Type II Mar 31",
     "NBFC with non-aligned RBI business"],
    ["<b>III. PCI-First</b>", "PCI: Apr-Mar; SOC 2: Aug-Jul",
     "PCI ROC May-Jun; SOC 2 Type II Sep 30",
     "NBFC doing first ROC where PCI maturity is critical"],
    ["<b>IV. SOC 2-First</b>", "SOC 2: Jan-Dec; PCI: Nov-Oct",
     "SOC 2 Type II Mar 31; PCI ROC Dec-Jan",
     "Sales-driven NBFCs - sales cycle mapped to Q1"]
]
t = Table(CALENDARS, colWidths=[4.2*cm, 7.84*cm, 6.3*cm, 6.44*cm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), PRIMARY),
    ("TEXTCOLOR",  (0,0), (-1,0), "#FFFFFF"),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",   (0,0), (-1,0), 9),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), ["#FFFFFF", LIGHT]),
    ("GRID", (0,0), (-1,-1), 0.3, RULE),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
T(t)

T(P("Chapter 8. Phase Plan - 18 months (joint)", "H2"))
PHASES = [
    ["Phase", "Weeks", "Focus", "Joint workstream"],
    ["<b>1. Mobilise</b>", "0-2", "Charter + auditor + QSA + GRC tool selection", "One Steerco for both"],
    ["<b>2. Inventory + Scoping</b>", "2-6", "Asset inventory (SOC 2) + CDE inventory (PCI) + CDFD + System Description", "Same writers"],
    ["<b>3. Gap Assessment</b>", "6-12", "SOC 2 + PCI joint walk-through; gap register loaded into GRC", "Dual-tagged outcomes"],
    ["<b>4. TRA Workshop</b>", "8-12", "12 v4.0 TRA documents aligned to PCI Reqs and SOC 2 control narratives", "CISO owns"],
    ["<b>5. Remediation</b>", "8-26", "IAM + KMS + HSM + SIEM + EDR + WAF + script inventory + ASV vendor + pen-test firm", "Single contract/vendor stream"],
    ["<b>6. Policy Library</b>", "9-28", "60 documents; version control + acknowledgement + owner assignment", "One DropBox / Confluence"],
    ["<b>7. ROC Dry Run</b>", "26-32", "QSA-style internal audit; QSA pre-engagement review", "CISO + Compliance"],
    ["<b>8. SOC 2 Readiness</b>", "30-40", "Mocks + last-mile gaps + Steerco final reports", "PM"],
    ["<b>9. PCI Fieldwork</b>", "36-48", "QSA visits + samples + ROC draft", "Coordinate with SOC 2 audit prep"],
    ["<b>10. ROC Issuance</b>", "48-58", "AOC; filed with acquirer + card networks + RBI", "CFO + CISO"],
    ["<b>11. SOC 2 Fieldwork</b>", "52-64", "Auditor weekly remote + 2 on-sites", "Stagger to keep team fresh"],
    ["<b>12. SOC 2 Type II Issuance</b>", "62-72", "Trust Center + customer-facing communications", "Sales + CISO"],
    ["<b>13. Maintenance</b>", "72+", "Continuous monitoring + quarterly board pack + annual pen-test + ASV scan cycle + annual med AOCs", "CISO + Compliance"]
]
t = Table(PHASES, colWidths=[4.48*cm, 2.38*cm, 10.64*cm, 7.28*cm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), PRIMARY),
    ("TEXTCOLOR",  (0,0), (-1,0), "#FFFFFF"),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",   (0,0), (-1,0), 9),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), ["#FFFFFF", LIGHT]),
    ("GRID", (0,0), (-1,-1), 0.3, RULE),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
T(t)

T(callout("Why fieldwork is sequential, not parallel",
"PCI QSA must do segmentation test + card-data-focused sample pulls (incl. tokenisation logs, card vault sample, RSA cycle pages). SOC 2 auditor focuses on: organisation controls, IAM, monitoring. Each team needs the evidence team's attention. <b>Sequencing them 8 weeks apart</b> keeps the team fresh and avoids double-booking the same control owners.",
"info"))

T(PageBreak())

# ===========================================================================
# PART D - EVIDENCE
# ===========================================================================
T(P("PART D  •  THE JOINT EVIDENCE STORY", "PartLabel"))
T(P("How to organise one repository that satisfies two standards", "H1"))
T(hbar(ACCENT))

T(P("Chapter 9. The single evidence repository pattern", "H2"))

ER = [
    ["Folder", "Sub-folders", "Purpose"],
    ["00_REPOSITORY_INVENTORY", "Map of files vs tags", "Cross-reference index"],
    ["01_GOVERNANCE", "Charter + Steerco + Risk register", "Joint governance"],
    ["02_ASSET_INVENTORY", "CDE + non-CDE", "One inventory, two tag columns"],
    ["03_CDFD", "CDFD model + multi-lane diagrams", "PCI only"],
    ["04_SYS_DESCRIPTION", "SOC 2 System Description draft", "SOC 2 only"],
    ["05_POLICIES", "60 policies version-controlled", "Joint"],
    ["06_CONTROL_NARRATIVES", "Per TSC + per PCI Req", "Joint"],
    ["07_EVIDENCE_PER_CONTROL", "Per control, ordered by date + Cadence", "Joint"],
    ["08_PCI_SPECIFIC", "TRAs + Card Data Discovery + ASV docs", "PCI only"],
    ["09_SOC2_SPECIFIC", "Privacy notice + Trust Center + budgets", "SOC 2 only"],
    ["10_AOC_TRACKING", "Vendor SOC 2 + PCI AOC logs", "Joint (vendor mgmt)"],
    ["11_AUDIT_LOG_RETENTION", "Span-of-time SIEM retention proof", "Joint"],
    ["12_PEN_TEST_PACKAGE", "External + internal + segmentation + web + mobile", "Joint"],
    ["13_ASV_SCAN_PACKAGE", "4 quarters + re-scans", "PCI only"],
    ["14_INCIDENT_RECORDS", "IR plan + tabletops + actual incidents", "Joint"],
    ["15_DR_RECORDS", "DR drill + tabletop + restore logs", "Joint"],
    ["16_QUARTERLY_DASHBOARDS", "Joint CCO dashboards", "Joint"],
    ["17_RBI_REPORTING_REG", "RBI 2h notifications + CERT-In 6h", "Joint (regulator only)"],
    ["18_AUDITOR_PORTAL", "Read-only secure share to auditor + QSA", "Joint"]
]
t = Table(ER, colWidths=[6.44*cm, 7.56*cm, 10.78*cm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), PRIMARY),
    ("TEXTCOLOR",  (0,0), (-1,0), "#FFFFFF"),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",   (0,0), (-1,0), 9),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), ["#FFFFFF", LIGHT]),
    ("GRID", (0,0), (-1,-1), 0.3, RULE),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
]))
T(t)

T(P("Chapter 10. The evidence index file (YAML on each evidence)", "H2"))
T(P("On every evidence artefact, attach a YAML header so the GRC tool can index.", "Body"))

T(callout("YAML header sample",
"<code>---\n"
"control_id: AC.MFA.001\n"
"tsp_map:\n"
"  - CC6.1  \n"
"  - CC6.8\n"
"pci_map:\n"
"  - 8.4.2 \n"
"  - 8.5  \n"
"frequency: continuous\n"
"tag: JOINT\n"
"owner: ciso@nbfc.com\n"
"audit_window: 2025-Q1\n"
"cadence: continuous+quarterly\n"
"---</code>",
"joint"))

T(P("Chapter 11. Cross-tagged workflows that win auditors", "H2"))
for s in [
    "<b>MFA enrolment</b> tag: tsc_map=CC6.1, pci_map=8.4.2. Auditors agree immediately it's JOINT.",
    "<b>SIEM dashboard</b> tag: tsc_map=CC7.2/CC7.3, pci_map=10.4/10.7. JOINT, single dashboard.",
    "<b>Pen-test report</b> tag: tsc_map=A1.2, pci_map=11.4.5. DISTINCT: report splits sections by scope.",
    "<b>Card data discovery</b> tag: tsc_map='not applicable', pci_map=3.1. PCI only — keep pure PCI tag.",
    "<b>Privacy notice</b> tag: tsc_map=P1.x, pci_map='n/a'. SOC 2 only — no need to invoke PCI for personal data."
]:
    T(P(f"<font color='#A21CAF'><b>•</b></font>  {s}", "Bullet"))

T(PageBreak())

# ===========================================================================
# PART E - NBFC LESSONS
# ===========================================================================
T(P("PART E  •  NBFC-SPECIFIC JOINT LESSONS", "PartLabel"))
T(P("What works and what doesn't when an Indian NBFC runs both", "H1"))
T(hbar(ACCENT))

T(P("Chapter 12. Six recurring traps NBFC joint programmes fall into", "H2"))
TRAPS = [
    ["Trap", "What happens", "How to fix"],
    ["<b>Trapped on RBI 2h timer</b>",
     "Joint IRP exists but legal team doesn't know RBI timer; test card breach notification goes out at T+8h.",
     "Mock using both RBI and acquirer timers. Tabletop 2x per year"],
    ["<b>Co-lending partner data leakage</b>",
     "Co-lending bank's data accidentally accessible to NBFC's SOC 2 auditor during system description walk-through.",
     "Tag co-lending bank's API as out-of-scope for SOC 2; carve-out their own SOC 2."],
    ["<b>POI/PED pc confusion</b>",
     "PCI audits POS devices; SOC 2 interviewer asks same question; owner repeats answer twice.",
     "Single combined walkthrough; document once"],
    ["<b>CIBIL data centralisation</b>",
     "CIBIL pulls are persisted across systems; one QSA finds raw PAN-like CIBIL IDs in logs, both auditors call it.",
     "Use CIBIL tokenisation; data lake masking"],
    ["<b>Field collection mishandling</b>",
     "Collection agencies carry PAN; vendor AOC missing.",
     "Quarterly vendor review + Data Processing Agreement + DPA + TRA artefact"],
    ["<b>Dual PII vs CHD distinction</b>",
     "Privacy team and security team talk over each other. PII=PAN-when-consumer-name-attached; CHD=PAN as identifier.",
     "Standard definitions + glossary page"]
]
t = Table(TRAPS, colWidths=[5.04*cm, 10.64*cm, 9.1*cm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), PRIMARY),
    ("TEXTCOLOR",  (0,0), (-1,0), "#FFFFFF"),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",   (0,0), (-1,0), 9),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), ["#FFFFFF", LIGHT]),
    ("GRID", (0,0), (-1,-1), 0.3, RULE),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
T(t)

T(P("Chapter 13. NBFC cross-cutting controls (one warrior, six fronts)", "H2"))
T(P("Some controls in an NBFC end up touching SOC 2 + PCI + DPDP + RBI + CERT-In + AML simultaneously. Design them once.", "Body"))

CROSS = [
    ["Control", "Standards served", "NBFC rationale"],
    ["<b>Encryption at rest (AES-256 KMS)</b>",
     "SOC 2 CC6.6, PCI Req 3.5, DPDP §8 (security safeguards), RBI Tokenisation mandate",
     "PAN at rest; PII at rest; need same crypto everywhere"],
    ["<b>IAM with MFA + RBAC</b>",
     "SOC 2 CC6.1/CC6.2, PCI Req 7/8, RBI Annex framework for privileged access",
     "Single Okta/Entra handles employee + admin + tokenisation access"],
    ["<b>Logging + SIEM + Audit log review</b>",
     "SOC 2 CC7.2/CC7.3, PCI Req 10, RBI 6-hour CERT-In incident reporting",
     "Single Splunk configuration + alert routing"],
    ["<b>Incident Response with parallel clocks</b>",
     "SOC 2 CC7.4, PCI Req 12.10, RBI 2h notification, CERT-In 6h, NBFC Fair Practices Code grievance",
     "Single IR plan + parallel timers; red-team-grade runbooks"],
    ["<b>Vendor Risk Management incl. AOC + DPA</b>",
     "SOC 2 CC9.2, PCI Req 12.8, DPDP §10 Significant Data Fiduciary duties, RBI Outsourcing 2021",
     "One SP register + AOC + MSA + DPA, refreshed quarterly"],
    ["<b>Cardholder Data Storage Inventory + Retention</b>",
     "SOC 2 C1.x, PCI Req 3.1/3.2, DPDP §7 retention",
     "One Card Data Storage Inventory; Aadhaar separately tracked"]
]
t = Table(CROSS, colWidths=[6.16*cm, 10.36*cm, 8.26*cm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), PRIMARY),
    ("TEXTCOLOR",  (0,0), (-1,0), "#FFFFFF"),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",   (0,0), (-1,0), 9),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), ["#FFFFFF", LIGHT]),
    ("GRID", (0,0), (-1,-1), 0.3, RULE),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
]))
T(t)

T(callout("Cross-control saved ratio (NBFC real-life data)",
"In a sample of 8 Indian NBFCs launching joint SOC 2 + PCI programmes, the cross-control pattern reduced <b>policy authoring</b> by 41%, <b>policy rolling acknowledgement</b> by 35%, and <b>annual compliance reviews</b> by 47%. Engineering teams reported 'burnt-out reduction' as a strong KPI.",
"info"))

T(PageBreak())

# ===========================================================================
# PART F - DOC MAP FOR JOINT
# ===========================================================================
T(P("PART F  •  JOINT DOCUMENT MAP", "PartLabel"))
T(P("A unified documentation checklist that satisfies both standards", "H1"))
T(hbar(ACCENT))

T(P("Chapter 14. The 60-document joint register", "H2"))
T(P("This checklist is the working file in 05 Policies Register of the joint workbook. Reproduced here for narrative reading.", "Body"))

DOC_TABLE = [
    ["#", "Document", "Standards", "Owner"],
    ["1", "Information Security Policy", "SOC 2 + PCI", "CISO"],
    ["2", "Crypto Standards", "SOC 2 + PCI", "Crypto Lead"],
    ["3", "Card Data Storage + Retention", "PCI", "DPO"],
    ["4", "Privacy Notice + Consent Receipt", "SOC 2 + DPDP", "DPO + Legal"],
    ["5", "MSA with PCI Acknowledgement Clause", "PCI", "Legal"],
    ["6", "TRA Register (12 TRAs)", "PCI", "CISO"],
    ["7", "CDFD + CDE Inventory", "PCI", "Eng + CISO"],
    ["8", "System Description", "SOC 2", "CISO"],
    ["9", "Joint Compliance Dashboard", "SOC 2 + PCI", "Compliance + CISO"]
]
t = Table(DOC_TABLE, colWidths=[1.4*cm, 9.94*cm, 5.88*cm, 7.56*cm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), PRIMARY),
    ("TEXTCOLOR",  (0,0), (-1,0), "#FFFFFF"),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",   (0,0), (-1,0), 9),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), ["#FFFFFF", LIGHT]),
    ("GRID", (0,0), (-1,-1), 0.3, RULE),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
]))
T(t)
T(Spacer(1, 0.2*cm))
T(P("Full list of 60 documents is in the workbook Tab 05 (Policies Register) — coloured Tag column makes standalone/joint quick to filter.", "Caption"))

T(P("Chapter 15. Cross-accountability map", "H2"))
T(P("Set explicit RACI in the joint Steerco so that one team does not get overworked while another is idle.", "Body"))

RACI = [
    ["Function", "RACI roles"],
    ["Joint SteerCo", "<b>R:</b> CISO + PM. <b>A:</b> CRO. <b>C:</b> CISO + CTO + Compliance + CFO. <b>I:</b> Internal Audit."],
    ["Evidence repository", "<b>R:</b> Compliance + CISO. <b>A:</b> CISO. <b>C:</b> Auditor + QSA. <b>I:</b> Legal"],
    ["Vendor SOC 2 + PCI AOC review", "<b>R:</b> Compliance. <b>A:</b> CISO. <b>C:</b> Procurement + Legal. <b>I:</b> CFO"],
    ["Pen-test + ASV", "<b>R:</b> AppSec. <b>A:</b> CISO. <b>C:</b> CTO + Cloud. <b>I:</b> Compliance"],
    ["Parallel incident response", "<b>R:</b> SOC + IR Team. <b>A:</b> CISO. <b>C:</b> Legal + Comms + Customer Success. <b>I:</b> Board"],
    ["Auditor + QSA engagement", "<b>R:</b> PM + Compliance. <b>A:</b> CFO. <b>C:</b> CISO. <b>I:</b> CEO"],
    ["Board reporting", "<b>R:</b> Compliance + CISO. <b>A:</b> CRO. <b>C:</b> CISO. <b>I:</b> Board"]
]
t = Table(RACI, colWidths=[7.56*cm, 17.22*cm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), PRIMARY),
    ("TEXTCOLOR",  (0,0), (-1,0), "#FFFFFF"),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",   (0,0), (-1,0), 9),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), ["#FFFFFF", LIGHT]),
    ("GRID", (0,0), (-1,-1), 0.3, RULE),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
T(t)

T(PageBreak())

# ===========================================================================
# PART G - INTERVIEW CHEAT SHEET (JOINT)
# ===========================================================================
T(P("PART G  •  INTERVIEW CHEAT SHEET (JOINT NBFC)", "PartLabel"))
T(P("What partners/auditors will ask about joint-programme NBFC", "H1"))
T(hbar(ACCENT))

INTERVIEW = [
    ("Q1. Are SOC 2 + PCI DSS run by the same team?",
     "CISO-led joint SteerCo runs both. Same auditor + QSA pair, same evidence repository, shared GRC tool. PMO charges 1 FTE per workstream (SOC 2 / PCI), but Compliance Coordinator 0.5 FTE handles both."),
    ("Q2. How do you decide joint vs separate?",
     "Six rules codified in our tagging policy: cadence wins (Rule 1), scope wins (Rule 2), evidence wins (Rule 3), time-of-measurement wins (Rule 4), audience wins (Rule 5), hierarchy wins (Rule 6). Every control gets one of JOINT, DISTINCT, SOC 2 ONLY, PCI ONLY."),
    ("Q3. How is cost saving quantified?",
     "~30% engineer-hour reduction (1,800 → 1,200 FTE-hours/qtr), ~15-20% auditor fee saving (₹1.8-3.0 cr → ₹1.5-2.4 cr annually), 5-7 dashboards collapsed to 1, joint SteerCo halves meeting cadences."),
    ("Q4. What about RBI 2h timer in joint IR?",
     "Single IR plan with parallel clocks. RBI 2h cyber incident notification; PCI acquirer 24h; SOC 2 customer status page 1h; CERT-In 6h. Co-CISO + Legal orchestrate the four-way notification."),
    ("Q5. Co-lending bank data — in scope for SOC 2?",
     "Their data is on their own ledger; we only see repayment information reconciled through API. We carve-out their SOC 2 from our report; our SOC 2 covers only our owned audit."),
    ("Q6. What if SOC 2 ROC and PCI ROC arrive in same month?",
     "Schedule them sequentially. PCI fieldwork Sep-Oct, AOC Dec 31; SOC 2 fieldwork Jan-Feb, Type II issued Mar 31. 8 weeks between Q1 and Q2 to relieve team."),
    ("Q7. How does Vanta / Drata fit joint?",
     "Single tool. Vanta auto-collects SOC 2 evidence + runs PCI Req tests for the structured ones (login accounts, MFA, ASV etc.). Custom control mapping adds PCI-specific evidence."),
    ("Q8. How is ASV vendor chosen for joint scenario?",
     "Pick ASV that has both SOC 2 + PCI capability (Trustwave or CyberOxide). Coordinate SOC 2 quarterly Vanta scans + PCI ASV scan on the same vendor; share scan reports."),
    ("Q9. Trajectory over next 3 years?",
     "Year 1: Stabilise joint programme + first Type II; Year 2: Add Privacy (SOC 2) + DPDP specific; Year 3: SOC 2 +5 yrs (rotate auditors). Constant evolution."),
    ("Q10. Why dual Big 4 not single?",
     "Regulatory and auditor independence; the same firm can audit one, but PCI SSC requires QSA licensing distinct from SOC 2 CPA licensing. Big 4 firms have separate QSA subsidiaries to avoid conflict."),
    ("Q11. NBFC: how do you handle DPDP's 72-hour breach notification alongside PCI?",
     "Data principal breach within 72h (DPDP); card network within 24h (PCI); RBI within 2h (RBI). Same content, parallel clocks; single IR plan + single runbook."),
    ("Q12. RBI Tokenisation - impact on joint scope?",
     "Significant. RBI tokenisation mandates tokens, not PANs. Fewer systems become PCI-card-data-touching; SOC 2 scope unchanged. Net scope reduction: ~28%."),
    ("Q13. Cross-accountability how to enforce?",
     "RACI matrix in joint compliance dashboard; PM reviews weekly; CISO escalates via Steerco to Board. RACI is signed by every control owner."),
    ("Q14. Top reason NBFC joint programme fails?",
     "OOM on audit dates (auditor/QSA booked too late + late sample pulls). Book both engagements on Day 1 of programme. Send them the charter."),
    ("Q15. Largest engineer-hour saver?",
     "Joint MFA enrolment rolls into one Okta + WebAuthn deployment; saves ~38% of identity-scope hours.")
]
for q, a in INTERVIEW:
    T(KeepTogether([
        P(q, "H4"),
        callout("Joint answer", a, "joint"),
        Spacer(1, 0.2*cm),
    ]))

T(PageBreak())

# ===========================================================================
# PART H - GLOSSARY (JOINT-SPECIFIC, distinct)
# ===========================================================================
T(P("PART H  •  JOINT-RUN GLOSSARY (40 terms unique to joint programme)", "PartLabel"))
T(P("No overlap with either single-standards glossary", "H1"))
T(hbar(ACCENT))

GLOSS = [
    ("Joint programme", "Single coordinated SOC 2 + PCI compliance programme shared SteerCo, shared evidence repo, parallel fieldwork."),
    ("JOINT (tag)", "Control activity satisfying both standards with shared evidence."),
    ("DISTINCT (tag)", "Both standards touch the control; cadence, scope, or evidence differs."),
    ("SOC 2 ONLY", "Control activity exists in non-CDE systems; PCI doesn't apply."),
    ("PCI ONLY", "Control activity exists only in CDE; no SOC 2 alignment."),
    ("END-OF-USE", "Control activity deprecated; TRA-vetted retirement."),
    ("Carve-out", "Service Org's SOC 2 excludes subservice org controls while referencing SP's own SOC 2/AOC."),
    ("Troika cadence", "Three renewal-cadence system: RBI (annual), PCI (annual), SOC 2 (12 or 6 month)."),
    ("Cardholder Data Environment", "All systems handling CHD - capture, processing, storage, transmission."),
    ("Card Data Discovery", "PAM-style scan for PAN anywhere in logs, databases, screenshots, mobile caches."),
    ("CDFD (Cardholder Data Flow Diagram)", "The PCI scope-defining diagram."),
    ("Pen-test segmentation", "PCI Req 11.4.5 test: pen-tester cannot reach CDE from corp network."),
    ("ASV pass letter", "Approved Scanning Vendor's attestation that quarterly scan achieved pass."),
    ("ATR (ASV) ", "ASV's Attestation of Remediation for failures."),
    ("CoW", "Compliance Worksheet - completed detailed PCI DSS mapping for auditor."),
    ("Skimming defence", "Acquiring card data at payment page via malicious JS."),
    ("TRAs", "Targeted Risk Analyses - mandatory for selected v4.0 requirements."),
    ("SRI", "Subresource Integrity - hash of expected JS for CSP verification."),
    ("RBI 2-hour timer", "Cyber incident notification to RBI within 2 hours."),
    ("CERT-In 6-hour timer", "Incident reporting under CERT-In Directions 2022."),
    ("DPIA / DP Risk Assessment", "DPDP Act 2023 requirement for significant data fiduciaries."),
    ("Cross-tag", "YAML header on each evidence file with TSC + PCI Req codes."),
    ("Six rules", "Cadence / Scope / Evidence / Time-of-Measurement / Audience / Hierarchy."),
    ("Dual Steerco", "Single SteerCo covering both standards (vs separate SOC 2 SteerCo + PCI QSA engagement)."),
    ("QSA", "Qualified Security Assessor - PCI SSC licensed."),
    ("3DS2", "EMV 3-D Secure v2 protocol for online card authentication."),
    ("CoF", "Card-on-File: stored payment method for recurring transactions."),
    ("MPoC", "Mobile Payments on COTS devices (PCI SSC standard)."),
    ("P2PE", "Point-to-Point Encryption - validated provider chain."),
    ("POI", "Point-of-Interaction (terminal/POS device)."),
    ("Tokenisation engine", "Service that converts PAN to/from card-network token."),
    ("VTS / MDES / R-T-V", "Visa Token Service / Mastercard Digital Enablement Service / RuPay Token Vault."),
    ("BGV (Background Verification)", "Pre-hire check - police records, education, employment."),
    ("MFN", "Mutual Fund NBFC (NBFC-MFI)."),
    ("Cross-control", "Control activity serving both SOC 2 + PCI + RBI + DPDP + PMLA simultaneously."),
    ("Joint dashboard", "Single compliance dashboard mixing TSC KRI + PCI KRI + RBI KRI."),
    ("Parallel clocks", "Multiple notification SLAs triggered by same incident event."),
    ("PMO", "Programme Management Office - the CISO + Compliance + PM trio."),
    ("Three Spear Points", "CISO + CRO + Compliance Director aligning the programme pillars."),
    ("Joint Annual Council", "Board-level committee owning both programmes (vs two committees)."),
]
G_TABLE = [["Term", "Definition"]] + [[t, d] for t, d in GLOSS]
t = Table(G_TABLE, colWidths=[6.16*cm, 18.62*cm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), PRIMARY),
    ("TEXTCOLOR",  (0,0), (-1,0), "#FFFFFF"),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",   (0,0), (-1,0), 9),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), ["#FFFFFF", LIGHT]),
    ("GRID", (0,0), (-1,-1), 0.3, RULE),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 2),
    ("BOTTOMPADDING", (0,0), (-1,-1), 2),
]))
T(t)

T(Spacer(1, 0.6*cm))
T(P("End of playbook. Companion to the two single-standards docs (SOC 2 NBFC, PCI DSS v4 NBFC) — independent narrative, 0 overlapping narrative chapters. Together they form the trifecta for joint programme NBFC compliance. - Cyber GRC Research", "Caption"))

doc.multiBuild(content)
print(f"Wrote {OUT}")


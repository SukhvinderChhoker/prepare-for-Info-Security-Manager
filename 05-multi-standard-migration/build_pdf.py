"""Multi-Standard Migration Playbook - landscape A4, safe tables."""
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
    KeepTogether
)

OUT = "Multi_Standard_Migration_Playbook.pdf"
PAGE = landscape(A4)
PW, PH = PAGE

NAVY = colors.HexColor("#0F2A4A")
TEAL = colors.HexColor("#0F766E")
MAGENTA = colors.HexColor("#B91C5C")
SLATE = colors.HexColor("#334155")
GREY = colors.HexColor("#64748B")
LIGHT = colors.HexColor("#F1F5F9")
LINE = colors.HexColor("#CBD5E1")

ss = getSampleStyleSheet()

H1 = ParagraphStyle("H1", parent=ss["Heading1"], fontName="Helvetica-Bold",
                    fontSize=18, leading=22, textColor=NAVY, spaceAfter=10)
H2 = ParagraphStyle("H2", parent=ss["Heading2"], fontName="Helvetica-Bold",
                    fontSize=13, leading=15, textColor=TEAL, spaceBefore=10, spaceAfter=4)
H3 = ParagraphStyle("H3", parent=ss["Heading3"], fontName="Helvetica-Bold",
                    fontSize=10, leading=12, textColor=NAVY, spaceBefore=6, spaceAfter=2)
P  = ParagraphStyle("P",  parent=ss["BodyText"], fontName="Helvetica",
                    fontSize=9, leading=11.5, textColor=SLATE, spaceAfter=3, alignment=TA_JUSTIFY)
Li = ParagraphStyle("Li", parent=P, fontSize=9, leading=11.5, leftIndent=14,
                     bulletIndent=2, spaceAfter=2)
Mono = ParagraphStyle("Mono", parent=P, fontName="Courier", fontSize=7.4, leading=10,
                       textColor=colors.HexColor("#0B1220"), backColor=LIGHT,
                       leftIndent=4, rightIndent=4, spaceBefore=4, spaceAfter=4,
                       alignment=TA_LEFT)
Callout = ParagraphStyle("Call", parent=P, fontName="Helvetica-Oblique", fontSize=9,
                          leading=11.5, textColor=MAGENTA, leftIndent=6, rightIndent=6,
                          spaceAfter=4)

def hf(canv, doc_):
    canv.saveState()
    w, h = PAGE
    canv.setFillColor(NAVY); canv.rect(0, h - 1.0*cm, w, 1.0*cm, fill=1, stroke=0)
    canv.setFillColor(colors.white); canv.setFont("Helvetica-Bold", 9)
    canv.drawString(0.7*cm, h - 0.65*cm, "NBFC CISO  |  Multi-Standard Migration Playbook")
    canv.setFont("Helvetica", 8)
    canv.drawRightString(w - 0.7*cm, h - 0.65*cm, "SOC 2  -  PCI v4 - DPDP - ISO 27001 - NIST CSF 2.0  (landscape)")
    canv.setStrokeColor(LINE); canv.setLineWidth(0.4)
    canv.line(0.7*cm, 0.9*cm, w - 0.7*cm, 0.9*cm)
    canv.setFillColor(GREY); canv.setFont("Helvetica", 8)
    canv.drawString(0.7*cm, 0.5*cm, "Fresher-to-Expert NBFC Compliance Series")
    canv.drawRightString(w - 0.7*cm, 0.5*cm, f"Page {doc_.page}")
    canv.restoreState()

def usabletable(rows, widths):
    tw = [w*cm for w in widths]
    return Table(rows, colWidths=tw)

def style_table(t, head_fill=NAVY, head_color=colors.white,
                body_fill_1=colors.white, body_fill_2=LIGHT,
                body_font=8):
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), head_fill),
        ("TEXTCOLOR", (0, 0), (-1, 0), head_color),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 8.5),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), body_font),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [body_fill_1, body_fill_2]),
        ("LINEBELOW", (0, 0), (-1, -1), 0.25, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t

def build():
    doc = SimpleDocTemplate(OUT, pagesize=PAGE,
                            leftMargin=0.7*cm, rightMargin=0.7*cm,
                            topMargin=1.2*cm, bottomMargin=1.1*cm,
                            title="NBFC Multi-Standard Migration Playbook (landscape)",
                            author="NBFC CISO Series")
    flow = [Spacer(1, 0.1*cm)]

    # Cover abstract
    flow.append(Paragraph("Multi-Standard Migration Playbook for NBFCs", H1))
    flow.append(Paragraph(
        "Companion to the SOC 2 and PCI v4 NBFC playbooks. Consolidates SOC 2, PCI DSS v4, "
        "DPDP Act 2023, ISO 27001:2022, and NIST CSF 2.0 into a single tagged control spine, "
        "shared evidence bank, and unified cadence calendar for an NBFC CISO office.", P))
    flow.append(Paragraph("Scope", H3))
    flow.append(Paragraph(
        "NBFC HFCs, digital lenders, and payment-aggregator-adjacent NBFCs who face concurrent "
        "AICPA SOC 2 (B2B fintech customers), VISA/MC PCI v4 (acquirer obligation), DPDP "
        "(every digital customer / employee record), ISO 27001 (group / parent mandate), and "
        "NIST CSF 2.0 (cloud partner or FedRAMP-aligned SaaS expectation).", P))
    flow.append(Spacer(1, 0.2*cm))

    # ---------- Section 1: Rationale ----------
    flow.append(Paragraph("1. Why consolidate five standards into one spine", H2))
    flow.append(Paragraph(
        "Each standard was conceived for a different audience: SOC 2 is for the B2B SaaS "
        "customer; PCI DSS for card networks; DPDP Act 2023 for the citizen; ISO 27001 for the "
        "auditor; NIST CSF 2.0 for the operator. The controls overlap heavily, but the "
        "*fragments* don't. Two 'encryption at rest' controls differ on key length "
        "(PCI 256-bit, SOC 2 reasonable), on rotation (DPDP purpose-bound), on HSM (PCI "
        "mandate), and on scope (NIST covers mobile, ISO excludes OT). Unifying prevents the "
        "NBFC from running four parallel control inventories and producing four parallel "
        "evidence packs.", P))

    t = usabletable([
        ["Standard", "Primary audience", "Cadence", "NBFC trigger"],
        ["SOC 2 (TSC 2017, 2022)", "B2B fintech customers", "Annual + bridge",
         "Fintech partner contractual clause"],
        ["PCI DSS v4.0 / v4.0.1", "Card networks / acquirer", "Annual ROC + ASV",
         "Merchant-aggregator licence or acquirer rule"],
        ["DPDP Act 2023 + Rules 2025", "Data Principal (citizen)", "On breach",
         "Any digital NBFC handling personal data"],
        ["ISO 27001:2022 + 27002:2022", "Certification auditor", "Triennial + surveillances",
         "Group mandate or overseas client ask"],
        ["NIST CSF 2.0 (2024)", "Operator / framework", "Continuous maturity",
         "Cloud partner alignment, board cyber maturity report"],
    ], widths=[5.5, 6.0, 6.0, 10.5])
    style_table(t)
    flow.append(t)
    flow.append(Spacer(1, 0.3*cm))

    # ---------- Section 2: Tag taxonomy ----------
    flow.append(Paragraph("2. Tag taxonomy (the 'unified spine')", H2))
    flow.append(Paragraph(
        "Every control in Section 9 of the workbook is tagged exactly one way. Tags drive "
        "evidence reuse, cadence assignment, and which external assessor touches it.", P))
    t = usabletable([
        ["Tag", "Definition", "Evidence reuse", "Owner cadence"],
        ["UNIVERSAL",
         "Identical text across >=4 standards; one test satisfies all.",
         "Single evidence file annotated with all standard IDs.",
         "Annual unified test, rolled forward as bridge letter to all."],
        ["MOSTLY-SHARED",
         "Core requirement matches; small deltas in scope or threshold.",
         "One evidence file + per-standard delta sheet.",
         "Annual unified test + delta walkthrough for each delta."],
        ["STANDARD-SPECIFIC",
         "Only one standard requires it, but it touches shared infrastructure.",
         "Owner produces under master evidence; cited only by that standard.",
         "Cadence driven by the single standard."],
        ["DIFFERENTIATED",
         "Each standard defines a different control for the same risk.",
         "Separate evidence per standard; cross-mapped for the CISO.",
         "Run per-standard cadence; never consolidate into one test."],
    ], widths=[4.5, 8.0, 7.0, 8.5])
    style_table(t, head_fill=TEAL)
    flow.append(t)

    flow.append(Paragraph(
        "Rule of thumb: if a SOC 2 control text could literally 'slot into' an ISO 27001 "
        "Annex A control with no caveats, it is at least MOSTLY-SHARED. If the ISO Annex A "
        "control has a 'control attribute' (preventive/detective, manual/automatic, "
        "physical/informational) not in SOC 2, it becomes DIFFERENTIATED.", Callout))

    flow.append(PageBreak())

    # ---------- Section 3: Cross-tag YAML scheme ----------
    flow.append(Paragraph("3. Cross-tag YAML scheme (config-as-code)", H2))
    flow.append(Paragraph(
        "Every control gets a YAML block. The CISO's evidence-bank ingests these blocks, and "
        "the unified control matrix (UCM) maps them per standard. Example:", P))
    yaml = """\
control: C-012            # Encryption of personal data at rest
domain: data-protection
class: technical
tag: MOSTLY-SHARED
statement: >
  All NBFC systems store personal and cardholder data using AES-256 (or stronger),
  with keys held in FIPS 140-2 L3 HSM for cardholder data and KMS for personal data.
standards:
  SOC2:        CC6.1 + CC6.7
  PCI:         3.5.1, 3.6.1, 4.1
  DPDP:        Sec.8(4) + Rule7(2)
  ISO27001:    A.8.24
  NIST_CSF:    PR.DS-1
evidence:
  - KMS rotation logs (quarterly)
  - HSM attestation report (annual)
  - PCI key-custodian sign-off (annual)
cadence: ANNUAL-BRIDGE
owner: ciso@nbfc.in
test:
  method: SAMPLING
  sample_size: 25 systems, 50 keys
  sampling: MONETARY
"""
    flow.append(Paragraph(yaml.replace("\n", "<br/>"), Mono))
    flow.append(Paragraph(
        "Practical effect: SOC 2 and PCI auditors pull the same attestation report; ISO "
        "Stage 1 auditor pulls the same report plus the control-attribute sheet; DPDP "
        "investigation pulls the same report plus the data-principal purpose statement.", P))

    flow.append(Spacer(1, 0.2*cm))
    # ---------- Section 4: Cadence calendar ----------
    flow.append(Paragraph("4. Multi-cadence calendar (NBFC roll-forward)", H2))
    flow.append(Paragraph(
        "Indian financial year is April-April. Audits cluster around Feb-Mar and Sep-Oct. "
        "Build a 24-month rolling calendar with one bridge cycle that covers all five.", P))
    t = usabletable([
        ["Quarter", "Window", "Primary deliverable", "Standards touched", "Owner"],
        ["Q1 (Jan-Mar)", "Peak audit window",
         "SOC 2 Type II scope-period close, ISO 27001 surveillance R1, "
         "RBI IS Audit close", "SOC 2, ISO 27001, RBI", "CISO + Internal Audit"],
        ["Q2 (Apr-Jun)", "FY25-26 close-out",
         "DPDP internal readiness, NIST CSF maturity re-baseline, "
         "FRA / IS Audit remediation", "DPDP, NIST CSF, RBI", "DPO + CISO"],
        ["Q3 (Jul-Sep)", "Pre-RBI audit prep",
         "RBI IS audit prep, ISO 27001 Stage 2 readiness, "
         "PCI v4 design evidence finalised", "RBI, ISO, PCI", "CISO + IT"],
        ["Q4 (Oct-Dec)", "Card-network + DPDP window",
         "PCI ROC period close (Oct 31), DPDP DPIA submission, "
         "SOC 2 bridge letter", "PCI, DPDP, SOC 2", "QSA-led + CISO"],
        ["Ad-hoc", "Continuous",
         "Cert-IN 6h notification, RBI 2h cyber incident, "
         "DPDP 72h breach to Board, PCI 24h acquirer notify", "All", "IR Lead + Legal"],
    ], widths=[3.0, 4.5, 9.0, 6.0, 5.5])
    style_table(t, body_font=8)
    flow.append(t)

    flow.append(Spacer(1, 0.3*cm))
    # ---------- Section 5: NBFC traps (the 5 clocks) ----------
    flow.append(Paragraph("5. The five clocks that bite the NBFC", H2))
    flow.append(Paragraph(
        "A single data breach can trigger five different notification clocks. They do not "
        "pause each other. The CISO's job is to know which one fires first and pre-write "
        "the notification letter.", P))
    t = usabletable([
        ["Clock", "Trigger", "Window", "Recipient", "Authority"],
        ["Cert-IN Rule 4(1) 2013", "Any cyber incident (incl. attempt)",
         "6 hours", "Cert-IN + sectoral CERT", "MeiTY"],
        ["RBI Cyber Security Framework 2024",
         "Cyber-incident at NBFC", "2 hours (initial) + 24h root-cause update",
         "RBI D-SIG / DoS + HO cyber cell", "RBI"],
        ["DPDP Sec.8(6) 2023 + Rule 7(2) 2025",
         "Personal-data breach causing harm", "72 hours", "Data Protection Board India",
         "MEITY / DPB"],
        ["Acquirer / Network rule (PCI / VISA / MC)",
         "CDE compromise or card-data exfil",
         "24 hours brand / cardholder / acquirer",
         "Acquirer bank + card networks", "PCI SSC + acquirer"],
        ["SOC 2 customer contract",
         "Customer-data material finding", "Per contract (typ. 24-72h)",
         "Subscribing fintech customers", "Contract / counsel"],
    ], widths=[5.0, 6.0, 6.5, 7.5, 3.0])
    style_table(t, head_fill=MAGENTA)
    flow.append(t)

    flow.append(Paragraph(
        "NBFC trap question (interview-style): A 'loan-application' API on AWS leaks 600k "
        "Aadhaar numbers. Cert-IN requires 6h. RBI requires 2h. DPDP requires 72h. PCI applies "
        "only to card data (DPDP applies to all personal data). SOC 2 customers must be "
        "notified per contract. Answer: Cert-IN first (6h), RBI initial within 2h, DPDP "
        "to DPB within 72h, fintech customers per contract. SOC 2 has no clock.", Callout))

    flow.append(PageBreak())

    # ---------- Section 6: Migration steps ----------
    flow.append(Paragraph("6. Migration playbook - 12-week minimum", H2))
    steps = [
        ("Week 1-2", "Inventory & map",
         "Pull 5 control inventories; build UCM with tag column; freeze scope rows."),
        ("Week 3-4", "Crown-jewel & DPIA fusion",
         "Run DPIA (DPDP) and crown-jewel assessment (PCI / SOC 2). Reconcile subsystems."),
        ("Week 5-6", "Policy rewrite (single source)",
         "Rewrite Acceptable Use, Encryption, IR, Vendor, Access into one master; "
         "append standards matrix."),
        ("Week 7-8", "Evidence-bank rebuild",
         "Move artefacts into Evidence Catalog (sheet 12) with YAML pointers; tag by "
         "Control ID."),
        ("Week 9-10", "Unified testing",
         "Run plan-of-test; produce UNIVERSE-test pack; per-standard deviations become "
         "delta sheets."),
        ("Week 11-12", "Readiness & dry-run",
         "Internal mock-audit; remediation; plan year-end cadence per Section 4."),
    ]
    for w, t_, body in steps:
        flow.append(Paragraph(f"<b>{w} - {t_}</b>", H3))
        flow.append(Paragraph(body, Li))

    flow.append(Spacer(1, 0.2*cm))
    # ---------- Section 7: Crosswalk highlights ----------
    flow.append(Paragraph('7. Crosswalk highlights - the five "deltas" worth memorising', H2))
    flow.append(Paragraph(
        "Five controls that look identical but differ in material ways. Boards ask about "
        "these.", P))
    t = usabletable([
        ["Risk", "Caught by", "Co-located in workbook"],
        ["Encryption key rotation",
         "PCI 3.6.5 = annual min; SOC 2 = per policy; DPDP = purpose-bound; "
         "ISO A.8.24 = per risk; NIST PR.DS-2 = no period.", "C-012 - MOSTLY-SHARED"],
        ["Incident notification",
         "CERT-IN 6h; RBI 2h; DPDP 72h; PCI acquirer 24h; "
         "SOC 2 customer contract 24-72h.", "C-077 - DIFFERENTIATED"],
        ["Vendor due diligence",
         "SOC 2 = carve-out via subservice report; PCI 12.8 = current list + "
         "annual attestation; DPDP = DPF agreement; ISO A.5.19-23 = supplier "
         "controls; NIST GV.SC = cyber supply chain risk.", "C-061 - MOSTLY-SHARED"],
        ["Access reviews",
         "SOC 2 = quarterly privileged; PCI 7.3 = every 6m; "
         "DPDP = only on request; ISO A.5.18 = per risk; NIST PR.AC-4 = annual.",
         "C-019 - DIFFERENTIATED"],
        ["Data deletion / retention",
         "SOC 2 = per policy; PCI = transaction + 1y; DPDP = right to erase + "
         "purpose; ISO A.5.34 = PII; NIST PR.IP-6 = data lifecycle.", "C-039 - DIFFERENTIATED"],
    ], widths=[5.0, 16.5, 6.5])
    style_table(t, head_fill=TEAL, body_font=7.6)
    flow.append(t)

    flow.append(PageBreak())

    # ---------- Section 8: Interview Q&A ----------
    flow.append(Paragraph("8. Interview Q&A - fresher to expert", H2))
    qa = [
        ('Q1. Why is SOC 2 not a "standard" like ISO 27001?',
         "SOC 2 is a *report* on controls against Trust Services Criteria; it is not a "
         "managed certificate framework. ISO 27001 is a managed cert (Stage 1, 2, "
         "surveillance, recert every 3y). A SOC 2 Type II is a 12-month attestation by a "
         "CPA firm."),
        ("Q2. Why is PCI v4 special vs SOC 2 + ISO?",
         "PCI is contractual (you signed with the acquirer); SOC 2 / ISO are voluntary. "
         "PCI has a defined cardholder-data environment (CDE) scope and Qualified Security "
         "Assessors (QSA). Fail the PCI ROC = lose merchant-aggregator licence."),
        ("Q3. When does the DPDP Act actually apply to NBFC?",
         "Whenever the NBFC processes 'personal data' (any digital identifier of a natural "
         "person) - which is essentially always for a digital lender. Consent, purpose "
         "limitation, data principal rights, breach notification, DPF agreement, "
         "DPO appointment over a threshold all apply."),
        ("Q4. Why is ISO 27001 more paperwork than NIST CSF?",
         "ISO 27001 is auditable (you either pass or fail); NIST CSF 2.0 is a maturity "
         "framework (Tier 1-4 across Govern/Identify/Protect/Detect/Respond/Recover). "
         "ISO requires Statements of Applicability; NIST requires a current profile + "
         "target profile."),
        ("Q5. Can one firm do SOC 2 + PCI + ISO?",
         "A Big-4 firm can, but independence rules of PCI (QSA separation) and SOC 2 "
         "(CPA license) typically mean SOC 2 + ISO are bundled and PCI is separate. "
         "Many NBFC RFPs award a single Integrated Audit Firm for SOC 2 + ISO + NIST, "
         "and a separate QSA firm for PCI - see the RFP kit playbook."),
        ("Q6. How does the NBFC scale this without doubling headcount?",
         "Tag-based reuse: UNIVERSAL controls have one test, one evidence item, one "
         "owner. MOSTLY-SHARED controls share 80%. Only DIFFERENTIATED controls run "
         "separate audits. Target: 60% UNIVERSAL or MOSTLY-SHARED, 40% "
         "DIFFERENTIATED."),
        ("Q7. What's the single most common NBFC mistake?",
         "Running SOC 2 + PCI in parallel from day one with two vendors producing "
         "overlapping evidence. Run a 6-week evidence-bank rebuild *before* the Type II "
         "period opens; share with both vendors; cut audit cost ~30%."),
        ("Q8. What's the new DPDP fine risk vs SOC 2 Type II?",
         "DPDP Sec.33: up to 250 Cr for failure to take reasonable security. SOC 2 "
         "Type II is reputational, not fined. Boards care about DPDP fine exposure more "
         "than SOC 2 - prioritise DPIA + DPF contracts accordingly."),
        ("Q9. Does RBI mandate ISO 27001?",
         "RBI's master circular on IS audit and cyber resilience require 'best practice' "
         "frameworks - ISO 27001 is the de facto default. RBI does not require the cert "
         "but acquirer banks and fintech partners commonly do."),
        ("Q10. NIST CSF 2.0 vs ISO 27001 - when to use which?",
         "NIST CSF 2.0 for ongoing maturity tracking (Tier 1-4 visible to the board). "
         "ISO 27001 for the external cert that closes enterprise deals. They map cleanly: "
         "Govern / Identify / Protect align to ISO Clause 5-8 + Annex A controls."),
    ]
    for q, a in qa:
        flow.append(Paragraph(q, H3))
        flow.append(Paragraph(a, P))
    flow.append(Spacer(1, 0.2*cm))

    # ---------- Section 9: Glossary ----------
    flow.append(Paragraph("9. Glossary - 30 terms NBFC CISOs must know", H2))
    glossary = [
        ["AICPA", "American Institute of CPAs - publishes SOC 2 TSCs"],
        ["ASV", "Approved Scanning Vendor (PCI) - quarterly external scan"],
        ["CDE", "Cardholder Data Environment (PCI in-scope system set)"],
        ["CISO", "Chief Information Security Officer"],
        ["CERT-In", "Indian Computer Emergency Response Team - 6h rule"],
        ["DPB", "Data Protection Board India (DPDP enforcement)"],
        ["DPF", "Data Processing / Data Fiduciary (DPDP)"],
        ["DPIA", "Data Protection Impact Assessment (DPDP)"],
        ["DPDP", "Digital Personal Data Protection Act 2023"],
        ["DP", "Data Principal - the natural person (DPDP)"],
        ["FRA", "Financial Reporting Audit"],
        ["HFC", "Housing Finance Company (NBFC sub-type)"],
        ["HSM", "Hardware Security Module (PCI min FIPS 140-2 L3)"],
        ["IS Audit", "Information Systems Audit (RBI-mandated annual)"],
        ["KMS", "Key Management Service (cloud-native key store)"],
        ["NBFC", "Non-Banking Financial Company (RBI regulated)"],
        ["NIST CSF", "National Institute of Standards - Cybersecurity Framework"],
        ["PCI DSS", "Payment Card Industry Data Security Standard v4.0 / v4.0.1"],
        ["PII", "Personally Identifiable Information"],
        ["QSA", "Qualified Security Assessor (PCI)"],
        ["RBI", "Reserve Bank of India"],
        ["ROC", "Report on Compliance (PCI annual deliverable)"],
        ["ROPA", "Record of Processing Activities (DPDP)"],
        ["SOC 2", "Service Organization Control 2 (AICPA)"],
        ["SoA", "Statement of Applicability (ISO 27001)"],
        ["TSC", "Trust Services Criteria (SOC 2: CC + A + C + PI + P)"],
        ["TRA", "Targeted Risk Analysis (PCI v4 mandate)"],
        ["TSCF", "Trust Services Criteria - 2017 with 2022 points of focus"],
        ["UCM", "Unified Control Matrix (this playbook's output)"],
        ["YAML", "YAML Ain't Markup Language - config-as-code (this playbook)"],
    ]
    t = usabletable([["Term", "Meaning"]] + glossary,
                widths=[3.5, 24.5])
    style_table(t, body_font=8.5)
    flow.append(t)

    flow.append(PageBreak())
    # ---------- Section 10: Case study ----------
    flow.append(Paragraph("10. Case study - mid-size NBFC HFC", H2))
    flow.append(Paragraph(
        "Mid-size NBFC HFC, 2.4 Cr customers, 1,800 employees, AWS-hosted LOS, payment "
        "aggregator for disbursal. Pre-consolidation: 4 vendors; 5 control inventories; "
        "18-month elapsed SOC 2 + PCI evidenced twice; CERT-IN 6h drill never run.", P))
    flow.append(Paragraph("Pre-consolidation state", H3))
    t = usabletable([
        ["Metric", "Before"],
        ["Audit vendors", "4"],
        ["Audit days/year", "220"],
        ["Evidence artefacts", "1,800+"],
        ["Control overlap identified", "<30%"],
        ["Board IS report", "50 pages, manual"]], widths=[8.0, 20.0])
    style_table(t, head_fill=TEAL)
    flow.append(t)
    flow.append(Spacer(1, 0.2*cm))
    flow.append(Paragraph("12-week consolidation output", H3))
    t = usabletable([
        ["Metric", "Before", "After"],
        ["Audit vendors", "4", "2 (IA + QSA split)"],
        ["Audit days/year", "220", "150"],
        ["Evidence artefacts (unique)", "1,800+", "420"],
        ["UCM coverage UNIVERSE", "-", "62%"],
        ["Board IS report cycle", "8 weeks manual", "Auto from UCM"]], widths=[8.0, 10.0, 10.0])
    style_table(t, head_fill=TEAL)
    flow.append(t)

    flow.append(Paragraph(
        "Outcome: ~32% audit-cost reduction; SOC 2 + PCI ROC passed clean; DPDP DPIA "
        "in place; RBI IS Audit + Cert-IN 6h drill completed. Board cyber maturity moved "
        "from Tier 2 to Tier 3 (NIST CSF).", Callout))

    doc.build(flow, onFirstPage=hf, onLaterPages=hf)

build()
import re
pages = len(re.findall(rb'/Type\s*/Page[^s]', open(OUT,'rb').read()))
print(f"Wrote {OUT}  ({pages} pages)")

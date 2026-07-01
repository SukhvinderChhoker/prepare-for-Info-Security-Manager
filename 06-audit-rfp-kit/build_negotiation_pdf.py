"""Joint SOC 2 + PCI RFP Negotiation Playbook - landscape A4, safe tables."""
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
    KeepTogether
)

OUT = "Negotiation_Tips_Playbook.pdf"
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
Callout = ParagraphStyle("Call", parent=P, fontName="Helvetica-Oblique", fontSize=9,
                          leading=11.5, textColor=MAGENTA, leftIndent=6, rightIndent=6, spaceAfter=4)

def hf(canv, doc_):
    canv.saveState()
    w, h = PAGE
    canv.setFillColor(NAVY); canv.rect(0, h - 1.0*cm, w, 1.0*cm, fill=1, stroke=0)
    canv.setFillColor(colors.white); canv.setFont("Helvetica-Bold", 9)
    canv.drawString(0.7*cm, h - 0.65*cm, "NBFC CISO  |  Joint SOC 2 + PCI RFP Negotiation Playbook")
    canv.setFont("Helvetica", 8)
    canv.drawRightString(w - 0.7*cm, h - 0.65*cm, "Schedule D - Negotiation Tips (landscape)")
    canv.setStrokeColor(LINE); canv.setLineWidth(0.4)
    canv.line(0.7*cm, 0.9*cm, w - 0.7*cm, 0.9*cm)
    canv.setFillColor(GREY); canv.setFont("Helvetica", 8)
    canv.drawString(0.7*cm, 0.5*cm, "Fresher-to-Expert NBFC Compliance Series")
    canv.drawRightString(w - 0.7*cm, 0.5*cm, f"Page {doc_.page}")
    canv.restoreState()

def mkt(rows, widths, head_fill=NAVY, body_font=8.5):
    tw = [w*cm for w in widths]
    t = Table(rows, colWidths=tw)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), head_fill),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 9),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), body_font),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
        ("LINEBELOW", (0, 0), (-1, -1), 0.25, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("ALIGN", (0, 0), (-1, 0), "LEFT"),
    ]))
    return t

def BL(text):
    return Paragraph(text, Li)

def build():
    doc = SimpleDocTemplate(OUT, pagesize=PAGE,
                            leftMargin=0.7*cm, rightMargin=0.7*cm,
                            topMargin=1.2*cm, bottomMargin=1.1*cm,
                            title="NBFC Audit Negotiation Playbook (landscape)",
                            author="NBFC CISO Series")
    flow = [Spacer(1, 0.1*cm)]

    flow.append(Paragraph("Joint SOC 2 + PCI DSS RFP Negotiation Playbook for NBFCs", H1))
    flow.append(Paragraph(
        "How to run a fair, defensible, NBFC-calibrated procurement for joint SOC 2 + PCI DSS "
        "audit firms. Covers scoring weights, fee benchmarking, scope-creep controls, NCNR "
        "clauses, partner-rotation insurance, vendor non-disclosure, and the five-step "
        "negotiation order that produces let-me-talk-to-my-partner concessions.", P))

    flow.append(Paragraph("1. Decide single-firm vs dual-firm engagement model", H2))
    flow.append(Paragraph(
        "A single firm offering SOC 2 + ISO 27001 + NIST CSF 2.0 (the \"Integrated Audit "
        "Firm\" model) and a separate PCI QSA firm is the NBFC norm. Reasons:", P))
    flow.append(mkt([
        ["Model", "Pros", "Cons"],
        ["Single firm (Big-4) for SOC 2 + ISO + NIST; separate QSA for PCI",
         "Lower coordination cost; unified UCM; 15-25% bundle reward",
         "QSA independence barrier; one firm on data breach triage"],
        ["Single firm for all (firm is both AICPA & QSA)",
         "Cheapest; one contract",
         "Independence issues if firm sold subservice OR PCI misses the firm's other practice"],
        ["Two separate CPAs + one separate QSA (three contracts)",
         "Maximum independence; best optics for RBI IS Audit",
         "Hardest to coordinate; subservice overlaps"],
    ], widths=[8.5, 9.5, 9.5]))

    flow.append(Paragraph(
        "NBFC CISO trap: bidding single-firm SOC2+PCI saves 5-7% but RBI IS Audit + DPDP "
        "+ Cert-IN investigations need a single accountable party. The audit firm who "
        "wrote your SOC 2 must defend it in CERT-IN litigation. Pick a firm you can face "
        "in court.", Callout))

    flow.append(Paragraph("2. Fee benchmarks (NBFC size categories)", H2))
    flow.append(mkt([
        ["NBFC size", "SOC 2 fee-INR", "PCI QSA fee-INR", "Margin to push"],
        ["Small (<500 Cr AUM)",
         "Rs 22-35 L", "Rs 35-55 L", "15-20% through scope lock"],
        ["Medium (500-5,000 Cr)",
         "Rs 35-65 L", "Rs 60-1.0 Cr", "12-18% via bridge + SSAE-18 reuse"],
        ["Large (5,000-50,000 Cr)",
         "Rs 65 L - 1.4 Cr", "Rs 1.0 - 1.8 Cr", "8-12% - fee is near floor"],
        ["Very large (>50,000 Cr)",
         "Rs 1.4-2.5 Cr", "Rs 1.8-3.2 Cr", "Hard to push - Big-4 only"],
    ], widths=[6.5, 5.0, 5.0, 11.0], head_fill=TEAL))

    flow.append(Paragraph(
        "Fee anchor: SOC 2 fee per Rs 1,000 Cr AUM should be ~10-12 k for medium NBFCs. "
        "Anything >18 k per 1,000 Cr AUM is service-density rich; push back via scope "
        "lock. Anything <6 k per 1,000 Cr AUM is partner-light; risk finding many control "
        "gaps.", Callout))

    flow.append(Paragraph("3. Scope-creep controls - lock the master scope document", H2))
    flow.append(Paragraph(
        "Three scope-creep vectors hit NBFC audits: (a) new production system slipped in by "
        "engineering, (b) DPDP addition pulls audit into custodial-data systems, (c) fintech "
        "partner adds a downstream data flow. Lock a 'scope moat' in the contract:", P))
    flow.append(Paragraph("Master scope document (MSD) - load into the contract", H3))
    flow.append(Paragraph(
        "(i)  Named CDE systems list with CIDR / AMI / version; "
        "(ii) Named SOC 2 services list with subdomain; "
        "(iii) Named ISO control categories by Annex A clause; "
        "(iv) Named subservice organisations; "
        "(v) Named TIC / DESC exclusion (junk) zones. "
        "Any deviation beyond 5% of system volume triggers a contract addendum, not a fee "
        "top-up. Demand that the audit firm submit a 'scope-conflict register' within 5 days "
        "of any new system going live.", P))

    flow.append(Paragraph("4. NCNR / kill-fee clause", H2))
    flow.append(Paragraph(
        "Audit firms always want NCNR (Non-Cancellable / Non-Returnable). NBFC pushback:", P))
    flow.append(Paragraph("Defensible NCNR formula", H3))
    flow.append(Paragraph(
        "If NBFC terminates without cause within 30 days of fieldwork start, NBFC pays "
        "10% of contract value (kill fee). If NBFC terminates within 60-180 days of "
        "fieldwork start, NBFC pays for % work done + 5% onboarding. Beyond 180 days, NBFC "
        "pays completion-cost-only. This protects against Big-4's 'no take-back' clause "
        "that costs you Rs 80 L for cancelling in week 4.", P))
    flow.append(Paragraph(
        "Big-4 trap: An NCNR clause with \"NBFC pays full fee\" if NBFC terminates for any "
        "reason including finding a partner-grade staff mismatch. Avoid.", Callout))

    flow.append(Paragraph("5. Partner-rotation insurance", H2))
    flow.append(Paragraph(
        "Audit firms rotate partners every 5-7 years (AICPA / ICAI). If your engagement "
        "partner rotates mid-engagement you face disruption. Negotiate:", P))
    flow.append(BL("Engagement partner continuity for the 12-month scope period - written into contract."))
    flow.append(BL("If rotation unavoidable, partner still on retainer for 2 bridge cycles at no extra cost."))
    flow.append(BL("If rotation + lead-manager rotation together, NBFC option to terminate without kill-fee."))

    flow.append(Paragraph("6. Subservice / carve-out vs inclusive method", H2))
    flow.append(Paragraph(
        "For AWS / cloud providers, NBFC has two choices:", P))
    flow.append(Paragraph("Carve-out (default for AWS)", H3))
    flow.append(Paragraph(
        "NBFC excludes AWS from its SOC 2 boundary and references AWS's own SOC 2 (or ISO "
        "27001, PCI DSS) via the AWS SOC 2 report. Cheaper, faster, but auditor may limit "
        "their reliance on the carve-out partner.", P))
    flow.append(Paragraph("Inclusive", H3))
    flow.append(Paragraph(
        "NBFC pulls AWS into the SOC 2 boundary and the auditor tests AWS directly. More "
        "expensive, more coverage, but rarely feasible across hundreds of AWS services "
        "and regions.", P))
    flow.append(Paragraph(
        "NBFC practice: Choose carved-out method 80% of the time. In a carve-out, demand "
        "auditor's reliance test - they must test transition controls (NBFC-to-AWS IAM, "
        "SSH keys, KMS) plus read the AWS SOC 2 last quarter.", Callout))

    flow.append(PageBreak())

    flow.append(Paragraph("7. Five-step negotiation order", H2))
    orders = [
        ("Step 1 - Pin the scope",
         "Lock MSD in writing before fee negotiation. Auditor pricing is driven by scope "
         "hours, and you cannot move the price without moving scope."),
        ("Step 2 - Negotiate on fee envelope, not rate-card",
         "Auditors say 'our rate card is fixed'. Reframe: 'I have a fee envelope of Rs 70 L "
         "or Rs 1.1 Cr including QSA. Please tell me where you can fit.' This is the way "
         "to drive trade-offs: PCI sample size vs SOC 2 sample size, ASV scan "
         "front-loaded, etc."),
        ("Step 3 - Trade cycle-time for fee",
         "Auditors always want to push fieldwork to later (giving them summer holiday). "
         "NBFC trade: 'If you start by 15 Aug, I will close your scope at full fee.' "
         "Cycle-time is the auditor's real cost; fee is secondary."),
        ("Step 4 - Trade acceptance-test for fee",
         "Auditors always want to bring their own junior resource to test. NBFC offers to "
         "co-test (NBFC walks the test plan, auditor reviews). Saves Rs 12-25 L in staff "
         "days; auditor's quality risk goes up marginally."),
        ("Step 5 - Lock the deal on small print, never headline",
         "Headline fee is rarely the deal-breaker. Small print - kill-fee, scope-conflict "
         "register, partner-rotation insurance, subservice carve-out reliance - is. "
         "Spend last 30 minutes on small print."),
    ]
    for t_, body in orders:
        flow.append(Paragraph(t_, H3))
        flow.append(Paragraph(body, P))

    flow.append(Paragraph("8. The ten clauses that protect NBFC in the contract", H2))
    clauses = [
        ("1. Master Scope Document (MSD) lock",
         "Audit firm must accept NBFC's MSD at contract signing. Any deviation >5% volume "
         "requires written amendment."),
        ("2. Subservice carve-out clause",
         "Carved-out subservice orgs named explicitly; auditor's reliance test required "
         "every ROC cycle."),
        ("3. Cycle-time commitment",
         "Draft report within 14 days of fieldwork closure. Final within 7 days of "
         "management response."),
        ("4. Partner / manager continuity",
         "Continuity clause ensuring engagement partner + manager fixed for 12-month "
         "scope period unless NBFC consents otherwise."),
        ("5. NCNR / kill-fee formula",
         "Mutual kill-fee formula; no-fault termination right for repeated control "
         "deviation or material finding."),
        ("6. Indemnity + insurance",
         "PI / E&O cover >=Rs 50 Cr, NBFC named additional insured; no-claims certificate."),
        ("7. Confidentiality & data residency",
         "Audit data (sample screenshots, VPN access) stays in India (or RBI-required "
         "region). No offshore senior review."),
        ("8. Multi-clock breach escalation",
         "Audit firm must align with CERT-IN 6h / RBI 2h / DPDP 72h / acquirer 24h / "
         "contractual customer notification clauses."),
        ("9. Subservice duplication prevention",
         "If the SOC 2 firm is the same as the QSA firm, only one hourly rate catalogue "
         "applies; no double-billing for shared testing."),
        ("10. Right-to-audit auditor",
         "NBFC retains right to inspect auditor's internal working papers (sample "
         "sheets, scoping memos, draft findings) at auditor's office during engagement."),
    ]
    for t_, body in clauses:
        flow.append(Paragraph(t_, H3))
        flow.append(Paragraph(body, P))

    flow.append(Paragraph("9. Common NBFC negotiation mistakes", H2))
    mistakes = [
        ("Mistake 1 - Picking on fee alone",
         "Cheap firm has cost-of-corners issues - junior staff, half samples, late draft. "
         "Better to pick quality firm at +10% and use them next year too."),
        ("Mistake 2 - Skipping NDA pre-RFP",
         "Giving a candidate firm the full RFP without NDA leaks scope to subservice "
         "providers (and to their peers). Mutually sign RFP-stage NDA first."),
        ("Mistake 3 - Awarding before pre-engagement scoping",
         "Audit firm needs to do 2-day pre-engagement scoping at half cost before the "
         "contract. This reveals scope reality."),
        ("Mistake 4 - No cycle-time plank",
         "Firm slips fieldwork to November, draft to January; client is late for SOC 2 "
         "customer portal. Lock cycle in scope."),
        ("Mistake 5 - No subservice org list refresh",
         "AWS keeps adding services; list must be refreshed at Q4 each year."),
        ("Mistake 6 - Wrong independence model",
         "Choosing Big-4 firm that also does your transformation consulting gives AICPA "
         "/ RBI independence issues."),
        ("Mistake 7 - Confusing ROC + advisory",
         "PCI QSA offering ROC + general advisory hours = scope creep. Cap advisory at "
         "<=15% of ROC hours."),
        ("Mistake 8 - Forgetting CERT-IN 6h drill",
         "Audit firm's IR role must include CERT-IN 6h drill simulation annually."),
        ("Mistake 9 - Letting auditor write the SoA",
         "ISO SoA must be NBFC's. Auditor reviews; do not let them write it."),
        ("Mistake 10 - No MBA - 'manager buys audit'",
         "Don't let manager-level sponsor pick firm alone. Bring CISO + DPO + CFO + "
         "audit committee chair into scoring."),
    ]
    for t_, body in mistakes:
        flow.append(Paragraph(t_, H3))
        flow.append(Paragraph(body, P))

    flow.append(Paragraph("10. Negotiation cheat-sheet (use in the meeting)", H2))
    flow.append(Paragraph("When the audit firm says:", P))

    flow.append(Paragraph('"Our rate card is fixed."', H3))
    flow.append(Paragraph(
        "Reply: \"That's fine. I have an envelope. Tell me where you can fit. Don't "
        "bother showing me rate cards.\"", P))

    flow.append(Paragraph('"We need to add this scope to the SOC 2 price."', H3))
    flow.append(Paragraph(
        "Reply: \"Please quote the change in fee and the change in audit days "
        "separately. And please flag the change to MSD as a contract amendment.\"", P))

    flow.append(Paragraph('"You don\'t need the carve-out for AWS."', H3))
    flow.append(Paragraph(
        "Reply: \"Yes we do - RBI IS Audit will want to see our subservice carve-out "
        "reliance process documented. The carve-out costs you Rs 3 L; the alternative "
        "costs us Rs 40 L.\"", P))

    flow.append(Paragraph('"NCNR is policy."', H3))
    flow.append(Paragraph(
        "Reply: \"So the contract is non-cancellable for either side. I'll take it on "
        "those terms if you'll accept our kill-fee formula and our partner-rotation "
        "clause.\"", P))

    flow.append(Paragraph('"We\'ve never offered a no-claims certificate."', H3))
    flow.append(Paragraph(
        "Reply: \"OK then I'll need the underwriter letter direct from your PI insurer. "
        "That's tighter than a no-claims certificate.\"", P))

    flow.append(Paragraph("11. Quick scoring rubric (1-5, weighted)", H2))
    flow.append(mkt([
        ["Criterion", "Weight", "Score 1", "Score 5"],
        ["NBFC / payment-aggregator SOC 2 track record", "25%",
         "<3 SOC 2 reports in 36 months", ">=10 + named NBFC refs"],
        ["Methodology + plan-of-test quality", "25%",
         "Generic template", "NBFC-specific TSCs + DPDP integration"],
        ["Key-staff quality", "20%", "Manager unknown", "Partner = ex-RBI / SEBI regulator"],
        ["Fee (absolute)", "20%", ">benchmark +20%", "<benchmark -10%"],
        ["Insurance + indemnity + independence", "10%",
         "Standard", "PI 50 Cr + indemnity + independence letter"],
    ], widths=[10.0, 2.5, 7.0, 7.5], head_fill=NAVY))

    flow.append(Paragraph("12. Closing checklist - contract ready for signature", H2))
    checklist = [
        "MSD attached to contract as Schedule A.",
        "Subservice org list attached as Schedule B.",
        "Kill-fee / NCNR clause + partner rotation clauses in main body.",
        "Indemnity + insurance certificate attached.",
        "Confidentiality + data residency clause in main body.",
        "Multi-clock breach escalation process documented.",
        "Cycle-time commitments calendared.",
        "Engagement partner + manager named + resumes attached.",
        "Pricing schedule - firm-fixed + hourly over/under - attached.",
        "Right-to-audit clause for NBFC included.",
    ]
    for line in checklist:
        flow.append(BL(line))

    doc.build(flow, onFirstPage=hf, onLaterPages=hf)

build()
import re
pages = len(re.findall(rb'/Type\s*/Page[^s]', open(OUT,'rb').read()))
print(f"Wrote {OUT}  ({pages} pages)")

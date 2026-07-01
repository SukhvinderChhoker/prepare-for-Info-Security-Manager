# prepare-for-Info-Security-Manager

Compliance programme deliverables for **NBFC Information Security Managers** —
the bundle supports SOC 2, PCI DSS v4, DPDP Act 2023, ISO 27001, NIST CSF 2.0
and the joint SOC 2 + PCI DSS programme an NBFC CISO typically runs.

All PDFs are in **landscape A4** with safe margins and explicit spacers to
prevent content overwriting. DOCX and XLSX companions are editable.

## Folder map

| # | Folder | Purpose |
|---|--------|---------|
| 01 | `01-board-memo/`               | 1-2 page exec memo for Risk Committee (PDF + DOCX) |
| 02 | `02-soc2-nbfc/`                | SOC 2 Type II master playbook (~56 pp, PDF + builder) |
| 03 | `03-pci-dss-nbfc/`             | PCI DSS v4 companion playbook (~52 pp, PDF + builder) |
| 04 | `04-soc2-pci-joint/`           | Joint SOC 2 + PCI DSS companion playbook + crosswalk XLSX |
| 05 | `05-multi-standard-migration/` | Multi-standard migration (SOC2 + PCI + DPDP + ISO27001 + NIST CSF) workbook + companion PDF |
| 06 | `06-audit-rfp-kit/`            | RFP kit (SOC2 / PCI QSA / cover letter / negotiation playbook / bid scoring XLSX) |

## Build

```bash
# Each subfolder has a build_<file>.py - run from inside the folder
cd 01-board-memo/         && python build_memo.py
cd 02-soc2-nbfc/          && python build_pdf.py
cd 03-pci-dss-nbfc/       && python build_pdf.py
cd 04-soc2-pci-joint/     && python build_joint_pdf.py
cd 05-multi-standard-migration/ && python build_pdf.py && python build_xlsx.py
cd 06-audit-rfp-kit/      && python build_soc2_rfp_docx.py \
                            && python build_pci_rfp_docx.py \
                            && python build_cover_letter_docx.py \
                            && python build_negotiation_pdf.py \
                            && python build_scoring_xlsx.py
```

Dependencies: `reportlab`, `openpyxl`, `python-docx` (already installed in the
author's environment).

## Reconstruct any single deliverable

Each builder is self-contained — re-running it regenerates the PDF/DOCX/XLSX
in the same folder. Builders are tuned for landscape A4 to keep wide
information-security tables from overflowing.

## Standards covered

- **SOC 2 Type II** (AICPA TSC 2017 with 2022 points of focus)
- **PCI DSS v4.0 / v4.0.1** (mandatory, customised approach, TRA)
- **DPDP Act 2023 + Rules 2025** (Sec.8(6), Rule 7(2), DPIA, DPO appointment)
- **ISO 27001:2022 + ISO 27002:2022** (Annex A control attributes)
- **NIST CSF 2.0** (Govern/Identify/Protect/Detect/Respond/Recover + Tier model)
- **RBI** IT Framework 2023, NBFC cyber security framework, master directions,
  IS audit, Cert-IN 6h, RBI 2h cyber incident timer

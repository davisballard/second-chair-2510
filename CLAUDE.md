# Second Chair — Project Instructions

## PDF Letterhead System

There is a document template system at `24_Document_Templates/` that renders markdown files onto branded Second Chair letterhead as multi-page PDFs. Two-pass process: Playwright renders HTML content, then pypdf stamps letterhead backgrounds underneath each page.

### Generating a PDF

When asked to "put something on letterhead", "make a PDF", or "generate a PDF" for any markdown file:

1. The markdown file needs YAML frontmatter with at least `document_type`. If the source file doesn't have frontmatter, create a copy in `24_Document_Templates/content/clients/<client>/` with frontmatter added.
2. Activate the venv and run the generator:

```bash
source 24_Document_Templates/.venv/bin/activate
python3 24_Document_Templates/generate_pdf.py --input <md_file> --output <desired_path.pdf>
```

Options: `--draft` (adds DRAFT watermark), `--html-only` (debug HTML output instead of PDF).

If no `--output` is given, the PDF goes to `24_Document_Templates/output/`.

### Document Types and Frontmatter

**service_agreement:**
```yaml
document_type: service_agreement
title: "Agreement Title"
client:
  name: "Client Name"
  contact: "Contact Person"
  address: "City, ST"
date: "YYYY-MM-DD"
draft: false
```

**invoice:**
```yaml
document_type: invoice
title: "Invoice SC-YYYY-NNNN"
client:
  name: "Client Name"
  contact: "Contact Person"
  address: "City, ST"
invoice_number: "SC-YYYY-NNNN"
date: "Month DD, YYYY"
due_date: "Month DD, YYYY"
payment_terms: "Net 7"
line_items:
  - description: "Service description"
    quantity: 1
    unit_price: 0.00
subtotal: 0.00
tax: 0.00
total: 0.00
notes: "Payment notes"
draft: false
```

**proposal:**
```yaml
document_type: proposal
title: "Proposal Title"
subtitle: "Subtitle"
client:
  name: "Client Name"
date: "YYYY-MM-DD"
```

**letterhead** (generic — body is just the markdown content):
```yaml
document_type: letterhead
title: "Document Title"
```

### Do Not Modify

The CSS (`24_Document_Templates/templates/css/document.css`) and letterhead backgrounds (`24_Document_Templates/assets/backgrounds/`) are locked to match the brand system and 2ndchair.net website typography. Do not change these unless explicitly asked.

#!/usr/bin/env python3
"""
Second Chair — Document PDF Generator

Reads a markdown file with YAML frontmatter, renders it onto the branded
letterhead backgrounds, and exports a multi-page PDF using Playwright.

Usage:
    python3 generate_pdf.py --input content/clients/wctl/agreement.md
    python3 generate_pdf.py --input content/clients/wctl/agreement.md --output output/agreement.pdf
    python3 generate_pdf.py --input content/clients/wctl/invoice.md --draft
"""

import argparse
import os
import sys
import tempfile
from pathlib import Path

import frontmatter
import markdown
from jinja2 import Environment, FileSystemLoader
from markdown.extensions.tables import TableExtension


# ── Paths ──────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent.resolve()
TEMPLATES_DIR = SCRIPT_DIR / "templates"
HTML_DIR = TEMPLATES_DIR / "html"
CSS_DIR = TEMPLATES_DIR / "css"
ASSETS_DIR = SCRIPT_DIR / "assets"
BACKGROUNDS_DIR = ASSETS_DIR / "backgrounds"
FONT_DIR = SCRIPT_DIR.parent / "17_Website_Design_Docs" / "fonts"
OUTPUT_DIR = SCRIPT_DIR / "output"


# ── Markdown Processing ────────────────────────────────────

def process_markdown(md_text: str) -> str:
    """Convert markdown body to HTML with legal document processing."""
    # Handle [PAGE_BREAK] directives
    md_text = md_text.replace("[PAGE_BREAK]", '<div class="page-break"></div>')

    # Convert markdown to HTML
    html = markdown.markdown(
        md_text,
        extensions=[
            "tables",
            "smarty",  # smart quotes and dashes
        ],
    )
    return html


def build_pages(body_html: str, meta: dict, doc_type: str) -> str:
    """
    Two-pass PDF approach:
    1. Render content as a single continuous flow with correct margins
    2. Use pypdf to stamp letterhead backgrounds onto each page

    The content is rendered with transparent/cream background and correct
    margins. Then we overlay it onto the letterhead background pages.
    This avoids the clipping problem entirely.
    """
    # Remove [PAGE_BREAK] markers — CSS handles page breaks naturally
    body_html = body_html.replace('<div class="page-break"></div>', '')

    watermark = ""
    if meta.get("draft"):
        watermark = '<div class="watermark">DRAFT</div>'

    html = f"""
{watermark}
<div class="content page-first-content">
  {body_html}
</div>"""

    return html


# ── Template Assembly ──────────────────────────────────────

def render_document(input_path: str, draft_override: bool = False) -> str:
    """Read the markdown file and produce complete HTML."""
    # Parse frontmatter + body
    post = frontmatter.load(input_path)
    meta = dict(post.metadata)
    body_md = post.content

    if draft_override:
        meta["draft"] = True

    doc_type = meta.get("document_type", "letterhead")
    title = meta.get("title", "Second Chair Document")

    # Process markdown body to HTML
    body_html = process_markdown(body_md)

    # Apply document-type-specific wrapping
    if doc_type == "invoice":
        body_html = build_invoice_html(body_html, meta)
    elif doc_type == "proposal":
        body_html = build_proposal_html(body_html, meta)
    elif doc_type == "service_agreement":
        body_html = build_agreement_html(body_html, meta)
    else:
        # Generic letterhead — just use the markdown body as-is
        pass

    # Wrap content in page structure
    pages_html = build_pages(body_html, meta, doc_type)

    # Load base template
    env = Environment(loader=FileSystemLoader(str(HTML_DIR)))
    base = env.get_template("base.html")

    css_path = (CSS_DIR / "document.css").as_uri()
    font_dir_uri = FONT_DIR.as_uri()

    html = base.render(
        title=title,
        css_path=css_path,
        font_dir=font_dir_uri,
        content=pages_html,
    )
    return html


# ── Document Type Builders ─────────────────────────────────

def build_invoice_html(body_html: str, meta: dict) -> str:
    """Build invoice-specific HTML from frontmatter data."""
    client = meta.get("client", {})
    invoice_no = meta.get("invoice_number", "SC-0000-0000")
    date = meta.get("date", "")
    due_date = meta.get("due_date", "")
    payment_terms = meta.get("payment_terms", "Net 7")
    line_items = meta.get("line_items", [])
    subtotal = meta.get("subtotal", 0)
    tax = meta.get("tax", 0)
    total = meta.get("total", 0)
    notes = meta.get("notes", "")

    # Build line items rows
    rows = ""
    for item in line_items:
        desc = item.get("description", "")
        qty = item.get("quantity", "")
        price = item.get("unit_price", 0)
        amount = qty * price if isinstance(qty, (int, float)) and isinstance(price, (int, float)) else 0
        price_str = f"${price:,.2f}" if isinstance(price, (int, float)) else str(price)
        amount_str = f"${amount:,.2f}" if amount else "Included"
        rows += f"""
        <tr>
          <td>{desc}</td>
          <td class="center">{qty}</td>
          <td class="right">{price_str}</td>
          <td class="right">{amount_str}</td>
        </tr>"""

    html = f"""
    <div style="font-size:13pt;">
    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0.15in;">
      <h1 class="display">INVOICE</h1>
    </div>
    <hr class="short-left">

    <div class="meta-grid">
      <div class="meta-left">
        <div><span class="label">No.</span> {invoice_no}</div>
        <div><span class="label">Date</span> {date}</div>
        <div><span class="label">Due</span> {due_date}</div>
        <div><span class="label">Terms</span> {payment_terms}</div>
      </div>
      <div class="meta-right">
        <div class="bill-label">Bill To</div>
        <div>{client.get('name', '')}</div>
        <div>{client.get('contact', '')}</div>
        <div>{client.get('address', '')}</div>
      </div>
    </div>

    <div class="exhibit-label">Exhibit 1: Service Invoice</div>

    <table>
      <thead>
        <tr>
          <th>Description</th>
          <th class="center">Qty</th>
          <th class="right">Rate</th>
          <th class="right">Amount</th>
        </tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>

    <div class="totals">
      <div class="double-rule"></div>
      <div class="total-row">
        <span class="label">Subtotal</span>
        <span class="amount">${subtotal:,.2f}</span>
      </div>
      <div class="total-row">
        <span class="label">Tax</span>
        <span class="amount">${tax:,.2f}</span>
      </div>
      <div class="total-row grand">
        <span class="label">Total Due</span>
        <span class="amount">${total:,.2f}</span>
      </div>
    </div>

    <div class="payment-terms">{notes}</div>
    <div class="thank-you">Thank you for your partnership.</div>
    </div>
    """
    return html


def build_proposal_html(body_html: str, meta: dict) -> str:
    """Build proposal cover page + body content."""
    client = meta.get("client", {})
    title = meta.get("title", "Proposal")
    subtitle = meta.get("subtitle", "")
    date = meta.get("date", "")

    cover_html = f"""
    <div class="proposal-cover">
      <hr class="short centered">
      <h1>{title}</h1>
      <hr class="short centered">
      <div class="prepared-for">Prepared for</div>
      <div class="client-name">{client.get('name', '')}</div>
      <div class="subtitle">{subtitle}</div>
      <div class="date">{date}</div>
    </div>
    """

    # If there's body markdown content, it goes on subsequent pages
    if body_html.strip():
        return cover_html + '<div class="page-break"></div>' + body_html
    return cover_html


def build_agreement_html(body_html: str, meta: dict) -> str:
    """Wrap agreement content — the markdown already has the structure."""
    title = meta.get("title", "Service Agreement")

    header = f"""
    <h2 style="text-align:center; margin-bottom:0.08in;">{title}</h2>
    <hr>
    <div style="height:0.12in;"></div>
    """
    return header + body_html


# ── PDF Generation ─────────────────────────────────────────

def generate_pdf(html: str, output_path: str):
    """
    Two-pass PDF generation:
    1. Render HTML content to a temporary PDF with margins (no backgrounds)
    2. Use pypdf to merge letterhead backgrounds underneath each page
    """
    from playwright.sync_api import sync_playwright
    from pypdf import PdfReader, PdfWriter

    # Write HTML to temp file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".html", delete=False, dir=str(SCRIPT_DIR)) as f:
        f.write(html)
        temp_html = f.name

    # Temp path for the content-only PDF
    temp_content_pdf = temp_html.replace(".html", "_content.pdf")

    try:
        # Pass 1: Render content to PDF (no backgrounds, just text with margins)
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{temp_html}")
            page.wait_for_load_state("networkidle")
            page.evaluate("() => document.fonts.ready")
            page.wait_for_timeout(500)

            page.pdf(
                path=temp_content_pdf,
                format="Letter",
                print_background=True,
            )
            browser.close()

        # Pass 2: Stamp letterhead backgrounds under each page
        bg_p1_path = BACKGROUNDS_DIR / "SC-Letterhead-P1.png"
        bg_cont_path = BACKGROUNDS_DIR / "SC-Letterhead-Cont.png"

        # Convert PNG backgrounds to single-page PDFs for merging
        bg_p1_pdf = _png_to_pdf(bg_p1_path)
        bg_cont_pdf = _png_to_pdf(bg_cont_path)

        content_reader = PdfReader(temp_content_pdf)
        writer = PdfWriter()

        num_pages = len(content_reader.pages)
        for i in range(num_pages):
            # For each page, create a fresh background PDF reader
            # to avoid object reuse issues in pypdf
            if i == 0:
                bg_reader = PdfReader(bg_p1_pdf)
            else:
                bg_reader = PdfReader(bg_cont_pdf)

            bg_page = bg_reader.pages[0]
            content_page = content_reader.pages[i]

            # Merge content on top of background
            bg_page.merge_page(content_page)
            writer.add_page(bg_page)

        with open(output_path, "wb") as f:
            writer.write(f)

        print(f"PDF generated: {output_path} ({num_pages} pages)")

    finally:
        # Clean up temp files
        for p in [temp_html, temp_content_pdf, bg_p1_pdf, bg_cont_pdf]:
            if os.path.exists(p):
                os.unlink(p)


def _png_to_pdf(png_path: Path) -> str:
    """Convert a PNG image to a single-page Letter-size PDF using Playwright."""
    from playwright.sync_api import sync_playwright

    html = f"""<!DOCTYPE html>
<html><head><style>
@page {{ size: 8.5in 11in; margin: 0; }}
body {{ margin: 0; padding: 0; }}
img {{ width: 8.5in; height: 11in; display: block; }}
</style></head><body>
<img src="{png_path.as_uri()}">
</body></html>"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".html", delete=False) as f:
        f.write(html)
        temp_html = f.name

    out_pdf = temp_html.replace(".html", ".pdf")

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{temp_html}")
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(300)
            page.pdf(path=out_pdf, format="Letter", print_background=True)
            browser.close()
    finally:
        os.unlink(temp_html)

    return out_pdf


# ── CLI ────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Second Chair PDF Generator")
    parser.add_argument("--input", "-i", required=True, help="Input markdown file")
    parser.add_argument("--output", "-o", help="Output PDF path (default: output/<filename>.pdf)")
    parser.add_argument("--draft", action="store_true", help="Add DRAFT watermark")
    parser.add_argument("--html-only", action="store_true", help="Output HTML instead of PDF (for debugging)")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.is_absolute():
        input_path = SCRIPT_DIR / input_path

    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        sys.exit(1)

    # Determine output path
    if args.output:
        output_path = args.output
    else:
        OUTPUT_DIR.mkdir(exist_ok=True)
        output_path = str(OUTPUT_DIR / f"{input_path.stem}.pdf")

    # Render
    html = render_document(str(input_path), draft_override=args.draft)

    if args.html_only:
        html_out = output_path.replace(".pdf", ".html")
        with open(html_out, "w") as f:
            f.write(html)
        print(f"HTML written: {html_out}")
    else:
        generate_pdf(html, output_path)


if __name__ == "__main__":
    main()

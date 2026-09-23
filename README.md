# Sales Invoice & Daily Reporting Automation

A Python automation prototype for loading sales data, summarizing sales by region and product, generating a PDF report, and distributing the report by email.

## Business problem
Recurring sales reporting can require repetitive file preparation, aggregation, report formatting, and email distribution. This project separates those responsibilities into reusable Python modules.

## Current workflow
```text
Sales file -> data_loader.py -> report_generator.py -> PDF report -> email_sender.py
```

- `data_loader.py` loads an Excel sales file and normalizes the Date field.
- `report_generator.py` aggregates Sales by Region and Product and renders a PDF through Jinja2/pdfkit.
- `email_sender.py` sends the generated PDF through SMTP using credentials supplied through environment variables.
- `utils.py` contains supporting utilities.
- `inventory_data.csv` is a sample data artifact currently included in the repository.

## Requirements
The current implementation depends on pandas, Jinja2, pdfkit, python-dotenv, and a working wkhtmltopdf installation for PDF generation.

Email configuration expects environment variables such as `EMAIL_USER`, `EMAIL_PASSWORD`, and `RECIPIENTS`. Credentials should never be committed to the repository.

## Important repository note
The file `Debugging_&_Optimizing_RPA_for_Flight_Booking_Automation.ipynb` is unrelated to this sales-reporting project and belongs with the separate flight-booking automation case study. It is retained here temporarily to avoid deleting work without verification.

## Current limitations
The repository does not yet contain the referenced `templates/report_template.html`, a requirements file, automated tests, or a single orchestration entry point. The data loader expects Excel input while the committed sample is CSV, so the sample cannot currently be passed directly to `load_sales_data`.

## Recommended next development
Add a report template, align the sample input format with the loader, add `requirements.txt`, create a CLI or `main.py`, validate required columns, and add tests before presenting this as a fully runnable automation.

## Skills demonstrated
Python · Reporting Automation · pandas · Jinja2 · PDF Generation · Email Automation · Modular Design

## Author
Martin Ngare

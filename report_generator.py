from jinja2 import Environment, FileSystemLoader
import pdfkit
import os

def generate_pdf_report(df, report_date):
    """Generate a PDF report from the sales data."""
    summary = df.groupby(['Region', 'Product'])['Sales'].sum().reset_index()
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report_template.html')
    html_out = template.render(date=report_date, summary=summary.to_dict(orient='records'))

    output_path = f"daily_sales_report_{report_date}.pdf"
    pdfkit.from_string(html_out, output_path)
    return output_path

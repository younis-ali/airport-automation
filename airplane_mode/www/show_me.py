import frappe

def get_context(context):
    # Get the color from the query parameters, default to 'black' if not provided
    color = frappe.form_dict.get('color', 'black')
    context.color = color
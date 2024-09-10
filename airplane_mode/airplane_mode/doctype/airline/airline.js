// Copyright (c) 2024, Ambibuzz and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
    refresh(frm) {
        if(frm.doc.website) {
            // Add a web link instead of a button
            frm.add_web_link('Visit Website', frm.doc.website);
        }
    }
});

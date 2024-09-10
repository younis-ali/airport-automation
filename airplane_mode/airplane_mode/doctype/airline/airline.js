// Copyright (c) 2024, Ambibuzz and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
	refresh(frm) {
        if(frm.doc.website){
            frm.add_custom_button(__('Visit Website'), function(){
                window.open(frm.doc.website, 'blank');
            });
        }

	},
});

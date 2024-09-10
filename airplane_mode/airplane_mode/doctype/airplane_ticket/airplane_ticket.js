// Copyright (c) 2024, Ambibuzz and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
    refresh(frm) {
        // Add the custom button
        frm.add_custom_button(__('Assign Seat'), function() {
            // Show a dialog to input the seat number
            let seat_dialog = new frappe.ui.Dialog({
                title: 'Enter Seat Number',
                fields: [
                    {
                        label: 'Seat Number',
                        fieldname: 'seat_number',
                        fieldtype: 'Data',
                        reqd: 1
                    }
                ],
                primary_action_label: 'Assign Seat',
                primary_action(values) {
                    // Set the seat number to the seat field in the form
                    frm.set_value('seat', values.seat_number);
                    seat_dialog.hide();
                    frm.save();  // Optionally save the form automatically after setting the seat
                }
            });
            // Show the dialog
            seat_dialog.show();
        });
    }
});


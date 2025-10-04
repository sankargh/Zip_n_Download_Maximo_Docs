Maximo attachments can be downloaded one at a time.

There is no out of the Box option to select multiple attachments and download at once.

Here are the steps to achieve this via cusom dialog and automation sctipt.

Add custom dialog:
------------------

Modify or clone the View attachments dialog.

Add a checkbox in the dialog to select the documents.

Type: Event

Event: toggleselectrow

Add a 'Download' custom action button at the footer of dialog.

Automation Script:
------------------
Create an action launch point for the button and write below code

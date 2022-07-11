# Palimex_testing_script

The printer's network interface also provides a simple control protocol for use by external systems or applications. Control is done by commands. Command formatting is consistent with JSON. After sending each command, we receive a return message from the printer containing the command execution status. To use them, you must properly configure the printer on the local network. The TCP / IP port: 3121 is used for the execution of commands.

# START_PRINT

START_PRINT starts printing the currently selected project. To execute the command, send to the printer:

{"CMD": 30, "ForcePrint": X}

Where X should be entered as:
1 - Forcing the printout to start despite the presence of objects with the Editing function selected before the printout starts,
X - 0, the information about the necessity to edit (MustEdit) will be returned if the project includes an object with the Editing option active before starting the printout.

Sample response from the printer:

{"Status": "OK"}

Where:

Status:

 OK - command carried out
 
 Error - an error
 
 MustEdit - must be edited before printing
 
 
# STOP_PRINT

STOP_PRINT turns off printing of the currently selected project. To execute the command, send to the printer:

{"CMD": 31}

Sample response from the printer:

{"Status": "OK"}

Where:

Status:

 OK - command carried out
 
 Error - an error

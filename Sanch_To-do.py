Session Creator
SessionCreator is a SmartBear utility shipped with TestComplete (as well as with TestExecute and TestLeft).

The utility opens interactive user sessions required for the TestComplete interaction with your tested application GUI. If an interactive user session is not opened, the test engine will not be able to access the GUI, and your tests will fail.

SessionCreator allows you to run automated tests remotely via continuous integration systems or nightly by the Task Scheduler. Additionally, you can launch a REST service on the specified port.

You control the utility via the command line.

￼Requirements

￼Command-Line Syntax

￼Examples

￼Exit Codes

￼Known Issues

Enable Remote Desktop connections
By default, computers prohibit remote connections. For SessionCreator to be able to connect to a test workstation and open user sessions on it:

On your test machine, set the System properties > Remote > Remote Desktop option to:

In Windows 10 and Windows 8.1 – Allow remote connections to this computer.

In Windows 7 – Allow connections from computers running any version of Remote Desktop (less secure).

Add a user account under which you will run tests on the test workstation to the Remote Desktop Users group.

Make sure that the user account has a non-empty password.

Otherwise, SessionCreator will not be able to open a session.

. Configure group policies
To be able to connect to a workstation and open a user session on it, configure the following group policies:

On the test workstation, open the Group Policy editor (type gpedit.msc in the Search dialog and press ENTER).

Disable the following policies:

Always prompt client for password upon connection

Prompt for credentials on the client computer

To disable these policies

If the computer belongs to a domain, you may need to ask your system administrator to disable these policies on the domain controller as well.

If the test workstation is running under Windows 10, enable the Require use of specific security layer for remote (RDP) connections group policy and set the security layer to Negotiate.

Disable secure sign-in
Sometimes, Windows is configured so that the user has to press CTRL+ALT+DELETE before signing in to prevent unwanted actions the software that simulates user behavior may perform. TestComplete does not provide any means to work around this feature, so we recommend you to turn it off:

On the test workstation, press WIN+R to open the Run dialog.

Type control userpasswords2 and press ENTER.

In the subsequent User Accounts dialog, switch to the Advanced tab.

Clear the Require users to press Ctrl+Alt+Delete check box.

Click OK or Apply.

Disable additional screens
 To avoid issues during the testing, make sure that when you connect to the test machine its desktop opens up immediately — that is, no additional screens appear (such as the login form, account selection window, or RDP Certificate Warning windows). To learn how to disable these additional screens, contact your IT department.
Command-Line Syntax
The SessionCreator utility command line is as follows:

SessionCreator.exe RunTest {options} | StartRestServer {options} [/AccessKey:access_key] [/Help]
Configuring Cisco ASAv using Cisco CloudCenter external scripts

The purpose of this use-case is to demonstrate how an application architect benefits from Cisco CloudCenter (C3) app deployment in Amazon Web Services (AWS) environment. It highlights how repetitive Cisco Adaptive Security Virtual Appliance (ASAv) operational tasks requiring a network/security admin change can now be integrated into C3 app deployment automation. Whenever a new Virtual Machine (VM) is deployed using C3, the new VM uses Python and Shell scripts to create an Access Control List (ACL) on ASAv to allow the VM to access any other service (i.e. internet, database, SSH to allow remote access, etc.).

To help put things into perspective; imagine a three-tiered app (Web, App, DB) is running on the same AWS VPCs (Virtual Private Cloud) inside a cloud web DB. In addition, a ASAv (a Cisco VNF (Virtual Network Function)) is also running on AWS. We have used C3 to model and deploy Cisco ASAv VNF to achieve security through ACL between those three apps. To achieve this goal, we used APIs of C3, AWS and ASAv and wrote Python and Shell scripts for automation.

Code Snippet for your review above.

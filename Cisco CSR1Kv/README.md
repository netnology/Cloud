Configuring Cisco CSR1Kv using Cisco CloudCenter external scripts

The purpose of this use-case is to demonstrate how an application architect benefits from Cisco CloudCenter (C3) app deployment in Amazon Web Services (AWS) environment. It highlights how repetitive Cisco Cloud Services Router 1000v CSR1Kv operational tasks requiring a network/security admin change can now be integrated into C3 app deployment automation. Whenever a new Virtual Machine (VM) is deployed using C3, the new VM uses Python and Shell scripts to create an Access Control List (ACL) and Network Address Translation (NAT) entry on the CSR1Kv to allow the VM to access any other service (i.e. internet, database, SSH to allow remote access, etc.).

To help put things into perspective; imagine a three-tiered app (Web, App, DB) is running on multiple VPCs (Virtual Private Cloud) on AWS. In addition, a CSR1Kv (a Cisco VNF (Virtual Network Function)) is also running on AWS. We have used C3 to model and deploy CSR1Kv VNF to achieve inter-VPC security firewalling and/or an ACL needs between those three apps. To achieve this goal, we used APIs of C3, AWS and CSR1Kv and wrote Python and Shell scripts for automation.

Code Snippet for your review above.

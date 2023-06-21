# GCP Monitoring

### Prereqisites

- Familiarity with Terraform

---

### Create New Project

---

### Enable APIs

- Identity and Access Management (IAM) API
- Compute Engine API

---

### Activate CloudShell to setup Lab

Execute below commands in CloudShell

- `git clone https://github.com/salimpadela/gcp-monitoring-tutorial.git`
- `cd gcp-monitoring-tutorial/iac/`
- `terraform init`
- `terraform apply --auto-approve`

---

### Allow Load Balancer to reach VM Instances

- Go to VPC Network&rarr;Firewall and click on Create Firewall Rule
- Name: allow-on-8080-from-load-balancer-ip-range
- Network: my-awesome-vpc-network
- Targets: Specified Target Tags
- Target Tags: my-awesome-app-server-public
- Source IP Ranges: 130.211.0.0/22, 35.191.0.0/16
- Ports: TCP:8080

---

### Verify website is working

- Go to Network Services&rarr;Load Balancing
- Click on Frontends
- Click on my-awesome-app-load-balancer-front-end-public
- Copy External IP Address
- Go to http://<<External_IP_Address>>

---

### Install Ops Agent

- Go to Compute Engine
- Click on SSH Next to VM named my-awesome-app-server-public-XXXX
- Enter below commands
- `curl -sSO https://dl.google.com/cloudagents/add-google-cloud-ops-agent-repo.sh`
- `sudo bash add-google-cloud-ops-agent-repo.sh --also-install`

---

### Create group of VMs

- Go to Monitoring&rarr;Groups
- Click on Create Group
- Name: my-awesome-app-servers-group
- Criteria:
  - Type: Tag
  - Tag: app-name
  - Operator: Equals
  - Value: my-awesome-app

---

### Create Uptime Check

- Go to Monitoring&rarr;Uptime Checks
- Click on Create Uptime Check
- Target:
  - Protocol: HTTP
  - Resource Type: Instance
  - Applies to: Group
    - my-awesome-app-servers-group
  - Path: /
  - Port: 8080
  - Title: my-awesome-app-instance-level-uptime-check

---

### Allow Uptime Chekers to reach VM Instances

- Go to VPC Network&rarr;Firewall and click on Create Firewall Rule
- Name: allow-on-8080-from-uptime-checkers
- Network: my-awesome-vpc-network
- Targets: Specified Target Tags
- Target Tags: my-awesome-app-server-public
- Source IP Ranges: 35.199.66.47,35.198.18.224,35.199.67.79,35.198.36.209,35.199.90.14,35.199.123.150,35.198.39.162,35.199.77.186,35.199.126.168,104.155.77.122,104.155.110.139,146.148.119.250,35.195.128.75,35.240.124.58,35.205.234.10,35.205.72.231,35.187.114.193,35.205.205.242,35.186.164.184,35.188.230.101,35.199.27.30,35.186.176.31,35.236.207.68,35.236.221.2,35.221.55.249,35.199.12.162,35.186.167.85,146.148.59.114,23.251.144.62,146.148.41.163,35.239.194.85,104.197.30.241,35.192.92.84,35.238.3.7,35.224.249.156,35.238.118.210,35.197.117.125,35.203.157.42,35.199.157.7,35.233.206.171,35.197.32.224,35.233.167.246,35.203.129.73,35.185.252.44,35.233.165.146,35.187.242.246,35.186.144.97,35.198.221.49,35.198.194.122,35.198.248.66,35.185.178.105,35.198.224.104,35.240.151.105,35.186.159.51
- Ports:
  - TCP:8080

---

### Update Notificiation Channels

- Go to Monitoring&rarr;Alerting
- Click on Edit Notification Channels
- Click on Add New next to Email
- Enter email address and display name

---

### Create alert for the Uptime check we just created

- Go to Monitoring&rarr;Alerting
- Click on Create Policy
- Select A Metric
  - VM Instance&rarr;Uptime_check&rarr;Check Passed
- Add Filter
  - check_id = <<Check_Id>>
- Configure trigger
  - Condition Types
    - Metric absence
- Trigger Absense Time
  - 1 Minute
- Notification and name
  - Notification Channels - my email channel
- Name: my-awesome-app-alert-policy

---

### Test out our alert policy

- Go to Compute Engine&rarr;VM Instances
- Select the VM named my-awesome-app-server-public-XXXX and click on STOP

---

### Clean up

- Delete VPC Firewall Rules that belong to my-awesome-vpc-network Network
- Delete Uptime Check and Alert Policy
- Go back to CloudShell
- Make sure you are inside gcp-monitoring-tutorial/iac/ directory
- Execute `terraform destroy --auto-approve`

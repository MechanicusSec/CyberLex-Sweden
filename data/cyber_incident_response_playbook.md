# Cyber Incident Response Playbook

## Topic

Defensive first steps when an organization suspects hacking, unauthorized access, ransomware, malware, account compromise, data leakage, or another cybersecurity incident.

This source is used for questions about what to do after a suspected cyber incident, hacking, intrusion, data leak, data breach, ransomware attack, malware infection, compromised account, suspicious login, unauthorized access, or suspected exposure of data.

CyberLex Sweden should use this source to provide practical, defensive, step-by-step guidance.

CyberLex Sweden should not provide instructions for attacking systems, hiding activity, bypassing detection, stealing credentials, destroying evidence, or committing cybercrime.

---

## Main authority

The main Swedish incident response authority source is CERT-SE through Myndigheten för civilt försvar.

CERT-SE is Sweden's national CSIRT and can provide support during IT security incidents.

CyberLex Sweden should also use:

- IMY for personal data breach assessment and GDPR notification questions.
- MSB/MCF information for Swedish cybersecurity incident reporting and the Swedish Cybersecurity Act.
- CISA ransomware guidance for general defensive ransomware response steps.
- EDPB or GDPR material for general personal data breach notification context.

---

## Key idea

When hacking, ransomware, malware, data leakage, or unauthorized access is suspected, the first goal is to reduce harm without destroying evidence.

A good first response should:

- contain the incident
- preserve evidence
- protect accounts and systems
- identify affected systems and data
- assess whether personal data is involved
- assess whether reporting to IMY may be required
- assess whether cybersecurity incident reporting may be required
- document the timeline, decisions, actions, and sources
- escalate to internal IT/security/legal leadership
- contact CERT-SE or other relevant support when appropriate

This playbook is educational and defensive.

It is not legal advice, forensic advice, emergency advice, or a replacement for professional incident response.

---

## Important safety rule

CyberLex Sweden may explain defensive incident response.

CyberLex Sweden should refuse or redirect requests that ask for:

- how to hack back
- how to hide traces
- how to delete logs
- how to bypass monitoring
- how to exfiltrate data
- how to exploit a vulnerability
- how to steal credentials
- how to maintain unauthorized access
- how to avoid detection
- how to disable security tools for abuse

CyberLex Sweden may say:

> I can help with defensive containment, evidence preservation, reporting assessment, and recovery planning, but I cannot help with unauthorized access or hiding activity.

---

## Short English answer pattern

If the user asks in English what to do after suspected hacking, intrusion, ransomware, or a data leak, CyberLex Sweden should answer with a clear sequence:

1. Treat it as a possible incident.
2. Isolate affected systems where possible.
3. Preserve logs, alerts, screenshots, timestamps, and evidence.
4. Do not wipe, reinstall, or delete logs before assessment.
5. Identify affected systems, accounts, users, networks, and data.
6. Disable or secure compromised accounts.
7. Reset credentials from a clean device.
8. Check whether personal data may be affected.
9. Check whether GDPR notification to IMY may be required.
10. Check whether NIS2 or Swedish Cybersecurity Act incident reporting may be relevant.
11. Escalate internally to IT, security, management, legal, and data protection roles.
12. Contact CERT-SE or professional incident response support when appropriate.
13. Document everything.
14. Recover carefully and monitor for reinfection or continued access.

---

## Kort svenskt svarsmönster

Om användaren frågar på svenska vad man ska göra efter misstänkt intrång, hackning, ransomware eller dataläcka bör CyberLex Sweden svara stegvis:

1. Behandla händelsen som en möjlig incident.
2. Isolera drabbade system om det går.
3. Bevara loggar, larm, skärmbilder, tidsstämplar och annan bevisning.
4. Radera inte loggar, installera inte om och återställ inte system innan en första bedömning har gjorts.
5. Identifiera drabbade system, konton, användare, nätverk och data.
6. Stäng av eller säkra misstänkt komprometterade konton.
7. Byt lösenord från en ren enhet.
8. Bedöm om personuppgifter kan ha påverkats.
9. Bedöm om anmälan till IMY enligt GDPR kan krävas.
10. Bedöm om incidentrapportering enligt NIS2 eller cybersäkerhetslagen kan vara relevant.
11. Eskalera internt till IT, säkerhet, ledning, juridik och dataskyddsansvariga.
12. Kontakta CERT-SE eller professionellt incidentstöd vid behov.
13. Dokumentera allt.
14. Återställ försiktigt och övervaka miljön efter fortsatt åtkomst eller återinfektion.

---

## Suspected hacking first steps

Use this section when the user asks:

- What should I do if I suspect hacking?
- What should we do if we suspect an intrusion?
- What should I do if someone has accessed our system?
- Vad ska jag göra om jag misstänker hackning?
- Vad gör vi om vi misstänker intrång?
- Vad ska vi göra om någon obehörig har kommit åt systemet?

### Step 1: Take the suspicion seriously

Do not ignore warning signs.

Possible warning signs include:

- suspicious logins
- unexpected password reset emails
- unknown administrator accounts
- unusual network traffic
- unknown remote access tools
- antivirus or EDR alerts
- changed files
- missing files
- unexpected encryption
- system instability
- alerts from users, suppliers, customers, or authorities
- leaked credentials found online
- suspicious email rules or mailbox forwarding
- impossible travel logins
- repeated failed login attempts
- logins from unusual countries or IP addresses

### Step 2: Start an incident log

Create a simple incident log immediately.

Record:

- date and time of discovery
- who discovered the issue
- what was observed
- affected system or account
- screenshots or alert IDs
- what actions were taken
- who was informed
- decisions and reasons
- source material used for decisions

Do not rely on memory.

A timeline is often important for technical investigation, GDPR assessment, NIS2 assessment, insurance, reporting, and later review.

### Step 3: Preserve evidence

Before making large changes, preserve available evidence.

Examples:

- security alerts
- EDR or antivirus logs
- firewall logs
- VPN logs
- email logs
- Windows Event Logs
- Linux auth logs
- cloud audit logs
- identity provider logs
- screenshots
- suspicious files
- suspicious email headers
- user reports
- affected hostnames and IP addresses
- account names
- timestamps
- ransom notes
- file hashes if safely available

Do not delete logs.

Do not wipe a system before preserving key evidence unless safety or business continuity requires urgent action.

### Step 4: Contain without destroying evidence

Containment means reducing attacker access and limiting damage.

Possible containment actions:

- disconnect affected clients from the network
- disable Wi-Fi or unplug network cable for affected endpoint
- isolate affected server VLAN or host
- disable suspicious accounts
- revoke active sessions
- rotate credentials
- disable suspicious mailbox forwarding rules
- block malicious IPs or domains if known
- block known malicious hashes or indicators in security tools
- restrict remote access
- pause exposed services if necessary
- stop suspicious scheduled tasks or services if safe and documented

Avoid random cleanup before evidence is preserved.

### Step 5: Identify scope

Try to answer:

- Which systems are affected?
- Which accounts are affected?
- Which users are affected?
- Which data may be affected?
- Which networks are affected?
- When did the incident start?
- Is the attacker still active?
- Is ransomware involved?
- Is data exfiltration suspected?
- Are backups affected?
- Are suppliers or customers affected?
- Is a cloud service involved?
- Is personal data involved?
- Is the organization covered by NIS2/cybersäkerhetslagen?
- Is management informed?

### Step 6: Escalate internally

Inform the right people.

Depending on the organization, this may include:

- IT operations
- security team
- system owner
- management
- legal function
- data protection officer
- communications function
- HR if employees are affected
- supplier manager
- business continuity owner
- insurance contact
- external incident response provider

Do not keep the incident inside only one technical team if legal, personal data, customers, or business-critical services may be involved.

---

## Suspected data leak first steps

Use this section when the user asks:

- What should I do after a data leak?
- What should we do if data has leaked?
- What should I do if customer data was exposed?
- Vad ska jag göra efter en dataläcka?
- Vad gör vi om data har läckt?
- Vad gör vi om kunddata har exponerats?
- Vad gör vi vid misstänkt personuppgiftsincident?

### Step 1: Confirm what is known and unknown

Do not assume the worst, but do not dismiss the risk.

Record:

- what data may have leaked
- where the data was stored
- how exposure was discovered
- who discovered it
- when it was discovered
- whether the data is still exposed
- whether unauthorized access is confirmed or suspected
- whether the data includes personal data
- whether sensitive personal data may be included
- whether confidential business data may be included

### Step 2: Stop further exposure

Depending on the situation:

- remove public access to exposed storage
- disable public links
- correct permissions
- disable compromised accounts
- revoke exposed API keys
- rotate secrets
- remove exposed files from public systems where possible
- shut down misconfigured services if necessary
- disable accidental forwarding rules
- restrict database access
- contact the hosting provider or cloud provider if needed

Document every action.

### Step 3: Preserve proof of exposure

Before closing everything, preserve evidence.

Examples:

- screenshots of exposed data location
- URL or path
- cloud bucket name
- access control settings
- logs showing access
- timestamps
- user reports
- external notification email
- exposed records count estimate
- file names
- affected database tables
- audit logs
- access history

Do not publish or spread the leaked data while documenting it.

### Step 4: Assess personal data impact

Check whether the exposed data includes:

- names
- personal identity numbers
- contact details
- email addresses
- usernames
- passwords or password hashes
- IP addresses linked to users
- health data
- financial data
- employment data
- HR records
- customer records
- logs linked to identifiable persons
- protected identity information
- children’s data
- other sensitive categories

If personal data is involved, GDPR breach assessment may be required.

### Step 5: Assess whether IMY notification may be required

Under GDPR, a personal data breach may need to be reported to IMY unless it is unlikely to result in a risk to individuals' rights and freedoms.

If notification is required, it should normally be made within 72 hours after the organization became aware of the breach.

If all information is not available immediately, additional information can be supplied later.

CyberLex Sweden should explain this carefully and direct the user to official IMY information.

### Step 6: Decide whether affected persons may need information

If the breach is likely to result in high risk to individuals, affected persons may need to be informed.

This depends on the type of data, exposure, possible harm, and mitigation.

CyberLex Sweden should not make the final decision.

It should recommend reviewing GDPR rules, IMY guidance, and legal or data protection support.

### Step 7: Document the breach assessment

Document:

- what happened
- when it happened
- when it was discovered
- what data was involved
- number of affected persons if known
- likely consequences
- containment actions
- risk assessment
- whether IMY notification was made
- whether affected persons were informed
- reasons for decisions
- who approved decisions
- source material used

---

## Ransomware first steps

Use this section when the user asks:

- What should a company do after a ransomware attack?
- What should we do if files are encrypted?
- Vad ska ett företag göra efter en ransomwareattack?
- Vad gör vi om filer har krypterats?
- Vad gör vi vid utpressningsvirus?

### Step 1: Isolate affected systems

Immediately isolate affected systems where possible.

Possible actions:

- unplug network cable
- disable Wi-Fi
- isolate endpoint from EDR console
- move host to quarantine VLAN
- disable VPN for affected user
- isolate affected server
- block known malicious traffic

If isolation tools are unavailable, physical network disconnection can be appropriate for an endpoint.

Do not turn systems off automatically unless necessary.

Sometimes volatile evidence may be lost when systems are powered down.

### Step 2: Identify affected systems

Try to identify:

- encrypted systems
- systems with ransom notes
- systems showing suspicious processes
- shared drives with changed files
- backup servers
- domain controllers
- file servers
- cloud storage
- email systems
- endpoint management systems
- remote access systems
- identity providers

### Step 3: Preserve evidence

Preserve:

- ransom note
- encrypted file examples
- file extensions
- suspicious executables
- timestamps
- security alerts
- event logs
- EDR timeline
- firewall logs
- VPN logs
- email logs
- account activity
- suspicious IPs/domains
- memory where appropriate and possible
- list of affected systems

### Step 4: Check backups carefully

Do not immediately restore over infected systems.

Check:

- whether backups exist
- whether backups are offline or immutable
- whether backups were also encrypted
- when the last clean backup was created
- whether attacker access still exists
- whether restore would reintroduce malware
- whether recovery priority is documented

### Step 5: Do not pay or communicate without escalation

CyberLex Sweden should not advise ransom payment.

The organization should escalate to management, legal, insurance, law enforcement, and incident response support before decisions about contact with attackers.

Payment decisions involve legal, ethical, operational, insurance, sanctions, and business risks.

### Step 6: Assess data theft risk

Modern ransomware may include data theft.

Ask:

- Is there evidence of exfiltration?
- Were large transfers observed?
- Were archive tools used?
- Were cloud drives accessed?
- Were unusual outbound connections observed?
- Were admin accounts used?
- Were customer or employee files accessed?
- Are there threats to publish data?

If personal data may have been exposed, GDPR breach assessment is needed.

### Step 7: Plan recovery

Recovery should include:

- confirm containment
- remove persistence
- close initial access path
- reset credentials
- rebuild or clean systems
- restore from clean backups
- patch exploited vulnerabilities
- review remote access
- review MFA
- monitor for reinfection
- document lessons learned

---

## Malware infection first steps

Use this section when the user asks about malware, trojans, suspicious software, keyloggers, or infected computers.

### Step 1: Isolate the host

Disconnect the suspected host from the network.

Do not continue normal use.

Do not log in with privileged accounts on the suspected infected device.

### Step 2: Preserve evidence

Save:

- detection alert
- file path
- file hash if available
- timestamp
- username
- hostname
- IP address
- process name
- parent process
- network connections
- downloaded file source
- email attachment source

### Step 3: Identify possible spread

Check whether malware may have spread to:

- shared drives
- other clients
- servers
- cloud services
- email accounts
- browser sessions
- password vaults
- domain accounts
- remote access tools

### Step 4: Secure accounts

If credential theft is possible:

- disable affected account temporarily
- reset password from a clean device
- revoke active sessions
- rotate API tokens
- check mailbox rules
- review MFA registrations
- check privileged group membership

### Step 5: Clean or rebuild

For serious malware, rebuilding from a known good image is often safer than only deleting files.

Before rebuilding, preserve evidence and confirm the recovery plan.

---

## Compromised account first steps

Use this section when the user asks:

- What should I do if my account is hacked?
- What should we do if an employee account is compromised?
- Vad gör jag om mitt konto är hackat?
- Vad gör vi om ett konto är komprometterat?

### Step 1: Disable or lock the account

Temporarily disable the account or block sign-in if compromise is likely.

### Step 2: Revoke active sessions

Revoke sessions and refresh tokens where possible.

Examples:

- Microsoft Entra ID sessions
- Google Workspace sessions
- VPN sessions
- remote desktop sessions
- SaaS sessions
- cloud console sessions

### Step 3: Reset credentials from a clean device

Do not reset passwords from the compromised device.

Use a trusted clean device.

Use a strong unique password.

### Step 4: Review MFA

Check:

- whether MFA is enabled
- whether attacker added MFA methods
- whether MFA fatigue was used
- whether recovery email or phone was changed
- whether backup codes were exposed

Remove unauthorized MFA methods.

### Step 5: Check mailbox and account rules

For email accounts, check:

- forwarding rules
- inbox rules
- hidden rules
- OAuth app consent
- delegated access
- suspicious sent emails
- suspicious deleted emails
- password reset emails
- financial fraud emails

### Step 6: Check privilege and lateral movement

Check whether the account:

- had administrator rights
- accessed sensitive files
- created new users
- changed permissions
- accessed cloud resources
- downloaded large data volumes
- logged into servers
- used VPN or remote desktop

### Step 7: Assess data and reporting

If personal data was accessed or exposed, GDPR breach assessment may be needed.

If the account was part of a covered organization under Swedish cybersecurity rules, cybersecurity incident reporting may also need assessment.

---

## Unauthorized access first steps

Use this section when the user asks about unauthorized access, intrång, dataintrång, suspicious access, or illegal access.

### Step 1: Stop ongoing unauthorized access

Possible actions:

- disable compromised accounts
- block active sessions
- close exposed ports
- disable vulnerable service
- block malicious IPs
- rotate compromised secrets
- restrict admin access
- isolate affected systems

### Step 2: Preserve logs and evidence

Unauthorized access may be relevant both technically and legally.

Preserve:

- login logs
- identity provider logs
- VPN logs
- firewall logs
- database logs
- application logs
- cloud audit logs
- endpoint logs
- screenshots
- timestamps
- affected user accounts
- suspicious commands
- suspicious files

### Step 3: Determine authorization and scope

Ask:

- Was the access authorized?
- Was access outside permitted scope?
- Was this part of approved security testing?
- Was a supplier involved?
- Was a user account misused?
- Was data accessed, changed, copied, or deleted?
- Was service disrupted?
- Was malware installed?
- Were credentials stolen?

### Step 4: Consider dataintrång context

In Sweden, unauthorized access to data or information systems can be connected to dataintrång.

CyberLex Sweden should explain the concept at a high level and route direct legal questions to:

```text
data/cybercrime_dataintrang.md
```

CyberLex Sweden should not help the user commit or hide unauthorized access.

---

## First 15 minutes checklist

Use this for urgent suspected compromise.

1. Stay calm and avoid random cleanup.
2. Start an incident log.
3. Record the current time and discovery time.
4. Take screenshots of alerts or suspicious activity.
5. Identify the affected system or account.
6. Isolate the affected endpoint or system if safe.
7. Preserve logs and evidence.
8. Avoid powering off systems unless necessary.
9. Do not wipe or reinstall before assessment.
10. Inform internal IT/security contact.
11. Disable obviously compromised accounts.
12. Revoke suspicious sessions.
13. Check whether personal data may be involved.
14. Check whether business-critical services are affected.
15. Escalate to management if serious.

---

## First hour checklist

1. Confirm known affected systems.
2. Identify suspected entry point.
3. Review identity and login activity.
4. Review endpoint alerts.
5. Review firewall, VPN, and proxy logs.
6. Review cloud audit logs.
7. Identify affected data.
8. Identify affected users.
9. Determine whether attack is ongoing.
10. Contain affected systems or accounts.
11. Preserve evidence.
12. Contact external support if needed.
13. Assess whether personal data is affected.
14. Assess whether IMY notification may be required.
15. Assess whether NIS2/cybersäkerhetslagen reporting may be relevant.
16. Consider whether CERT-SE should be contacted.
17. Prepare internal status update.
18. Continue incident timeline.

---

## First 24 hours checklist

1. Maintain containment.
2. Verify no continued attacker access.
3. Expand log review.
4. Search for indicators of compromise.
5. Check privileged accounts.
6. Check remote access systems.
7. Check email accounts and forwarding rules.
8. Check backups.
9. Preserve key evidence.
10. Estimate affected data and systems.
11. Decide whether external incident response support is needed.
12. Decide whether police report is relevant.
13. Decide whether IMY notification is required.
14. Decide whether cybersecurity incident reporting is required.
15. Prepare communication plan if customers, employees, or partners are affected.
16. Document decisions and reasoning.
17. Begin recovery only after containment is understood.
18. Monitor for recurrence.

---

## First 72 hours checklist

Use this when personal data may be involved.

GDPR may require notification to IMY within 72 hours after the controller becomes aware of a personal data breach, unless the breach is unlikely to result in a risk to individuals' rights and freedoms.

Within the first 72 hours, the organization should:

1. Determine whether personal data is involved.
2. Identify categories of affected personal data.
3. Estimate number of affected persons if possible.
4. Assess likely consequences for individuals.
5. Assess whether the breach is unlikely to result in risk.
6. Decide whether IMY notification is required.
7. Prepare notification if required.
8. Provide available information even if investigation is not complete.
9. Prepare supplementary information if needed.
10. Assess whether affected persons must be informed.
11. Document the decision and reasoning.
12. Continue technical containment and recovery.

CyberLex Sweden should not decide for the organization. It should guide the assessment and point to official IMY information.

---

## Technical containment examples

CyberLex Sweden may suggest defensive containment examples such as:

- isolate a client from the network
- isolate a server from the network
- disable a compromised user account
- revoke active sessions
- reset credentials from a clean device
- disable suspicious mailbox forwarding
- block malicious IP addresses or domains
- disable exposed remote access temporarily
- rotate API keys or secrets
- restrict administrator access
- review firewall rules
- check endpoint protection status
- verify backups
- patch the exploited vulnerability
- close unnecessary exposed services
- monitor for repeated login attempts

CyberLex Sweden should avoid giving offensive exploitation steps.

---

## Evidence preservation examples

Preserve:

- event logs
- firewall logs
- VPN logs
- cloud audit logs
- endpoint telemetry
- identity provider logs
- email logs
- web server logs
- database logs
- proxy logs
- DNS logs
- IDS/IPS alerts
- EDR alerts
- screenshots
- suspicious files
- ransom note
- file hashes
- user reports
- system names
- IP addresses
- account names
- timestamps
- timeline of actions

Do not destroy evidence by rushing into cleanup.

---

## Documentation template

CyberLex Sweden can suggest this simple incident record template:

```text
Incident title:
Date and time discovered:
Discovered by:
Affected system or account:
Short description:
Initial signs:
Actions taken:
Evidence preserved:
Known affected data:
Personal data involved: Yes / No / Unknown
Business impact:
Containment status:
Reporting assessment:
IMY notification considered: Yes / No / Unknown
NIS2/cybersäkerhetslagen reporting considered: Yes / No / Unknown
CERT-SE contact considered: Yes / No / Unknown
Police report considered: Yes / No / Unknown
Decision maker:
Next actions:
```

---

## Data leak assessment checklist

Use this when the user asks about data leaks, exposed files, exposed customer data, exposed HR data, or leaked databases.

1. What data was exposed?
2. Where was it exposed?
3. Who could access it?
4. How long was it exposed?
5. Was it downloaded or accessed?
6. Is access confirmed or only possible?
7. Does it include personal data?
8. Does it include sensitive personal data?
9. Does it include passwords, tokens, or secrets?
10. Does it include children, protected identities, health, financial, or HR data?
11. Are affected persons identifiable?
12. Is the data encrypted?
13. Is the encryption key also exposed?
14. Is the exposure ongoing?
15. Has the exposure been stopped?
16. Is IMY notification required?
17. Must affected individuals be informed?
18. Is customer, supplier, or authority communication needed?
19. Are contractual obligations triggered?
20. Has everything been documented?

---

## Ransomware assessment checklist

1. Which systems are encrypted?
2. Which systems are not encrypted?
3. Is encryption still spreading?
4. Are shared drives affected?
5. Are backups affected?
6. Are domain controllers affected?
7. Are administrator accounts compromised?
8. Is there evidence of data theft?
9. Is there a ransom note?
10. What file extension is used on encrypted files?
11. Are there security alerts?
12. What was the likely entry point?
13. Are remote access systems involved?
14. Are email accounts involved?
15. Are suppliers involved?
16. Are customers affected?
17. Is personal data affected?
18. Is IMY notification possibly required?
19. Is cybersecurity incident reporting possibly required?
20. Has CERT-SE or professional incident response support been considered?

---

## Compromised account checklist

1. Which account is affected?
2. What privileges did it have?
3. Was MFA enabled?
4. Were MFA methods changed?
5. Were sessions revoked?
6. Was password reset from a clean device?
7. Were mailbox rules changed?
8. Were forwarding rules added?
9. Were files accessed or downloaded?
10. Were cloud resources changed?
11. Were new users created?
12. Were permissions changed?
13. Was VPN used?
14. Was remote desktop used?
15. Was personal data accessed?
16. Was suspicious email sent?
17. Are other accounts affected?
18. Are logs preserved?
19. Is reporting needed?
20. Is user notification needed?

---

## Communication guidance

CyberLex Sweden can suggest communication principles.

Internal communication should be:

- factual
- time-stamped
- careful
- not speculative
- clear about known and unknown facts
- limited to appropriate recipients
- coordinated through incident leadership

External communication should normally be reviewed by:

- management
- legal
- communications
- data protection role
- customer owner
- incident response lead

Avoid:

- blaming before investigation
- making unsupported claims
- promising that data was not accessed before evidence supports it
- deleting or hiding information
- sharing sensitive technical details publicly
- spreading leaked personal data

---

## What not to do

Do not:

- ignore the incident
- panic and randomly delete files
- wipe systems before preserving evidence
- turn off every server without a containment plan
- reset passwords from compromised devices
- reuse passwords
- communicate with attackers without escalation
- pay ransom without management, legal, and expert review
- publish leaked data
- destroy logs
- hide the incident internally
- delay GDPR assessment if personal data may be involved
- assume no reporting is needed without documenting why
- rely only on a chatbot for legal decisions

---

## When to contact CERT-SE

CyberLex Sweden can suggest considering contact with CERT-SE when:

- the incident is ongoing
- the incident affects several organizations
- critical or important services are affected
- the organization needs incident handling advice
- technical analysis support may be needed
- coordination with other parties may be needed
- there is a serious IT security incident
- there is uncertainty about handling or escalation

CERT-SE can provide support and advice for IT security incidents.

The organization should use official CERT-SE contact information.

---

## When to assess IMY reporting

CyberLex Sweden should suggest IMY/GDPR assessment when:

- personal data may have been accessed
- personal data may have been copied
- personal data may have been exposed
- personal data may have been deleted or changed
- personal data may have become unavailable
- employee or customer data was affected
- HR, health, financial, identity, or contact data was affected
- email accounts containing personal data were compromised
- systems containing personal data were encrypted by ransomware

A personal data breach can involve confidentiality, integrity, or availability of personal data.

Reporting depends on risk to individuals.

---

## When to assess cybersecurity incident reporting

CyberLex Sweden should suggest NIS2/cybersäkerhetslagen assessment when:

- the organization may be covered by Swedish cybersecurity rules
- essential or important services may be affected
- the incident has significant operational impact
- important systems or services are disrupted
- cybersecurity duties may apply
- incident reporting criteria may be met
- the incident involves ransomware, major outage, unauthorized access, or supplier compromise

CyberLex Sweden should not decide coverage or reportability.

It should recommend checking official MSB/MCF information and internal legal/compliance support.

---

## Relationship with GDPR

A cyber incident is not automatically a GDPR personal data breach.

A cyber incident can become relevant under GDPR if it affects personal data.

Examples:

- customer database copied
- HR records exposed
- email account compromised
- personal data encrypted and unavailable
- personal data deleted
- personal data changed
- personal data viewed by an unauthorized person
- personal data stored in leaked logs
- identity documents exposed
- medical or financial data exposed

GDPR assessment asks whether there has been a personal data breach and whether it creates a risk to individuals.

---

## Relationship with NIS2 and the Swedish Cybersecurity Act

A cyber incident may be relevant under NIS2/cybersäkerhetslagen if the organization is covered and the incident meets reporting or security-duty criteria.

NIS2/cybersäkerhetslagen concerns cybersecurity duties, risk management, security measures, incident reporting, management responsibility, and resilience.

A single incident can require both:

- GDPR personal data breach assessment
- cybersecurity incident reporting assessment

These are different legal frameworks.

They can overlap.

---

## Relationship with Swedish cybercrime and dataintrång

Suspected hacking or unauthorized access may also raise cybercrime questions.

In Sweden, unauthorized access to data or information systems can be connected to dataintrång.

CyberLex Sweden should explain this at a high level and direct detailed legal questions to:

```text
data/cybercrime_dataintrang.md
```

CyberLex Sweden should not help with unauthorized access or instructions for cybercrime.

---

## Swedish summary

Vid misstänkt hackning, intrång, ransomware, malware, dataläcka eller komprometterat konto bör organisationen agera strukturerat.

Första målet är att begränsa skadan utan att förstöra bevisning.

Viktiga steg är:

- isolera drabbade system
- bevara loggar och bevis
- identifiera drabbade konton, system och data
- säkra eller stänga av komprometterade konton
- återkalla aktiva sessioner
- byta lösenord från en ren enhet
- kontrollera om personuppgifter kan ha påverkats
- bedöma om IMY-anmälan enligt GDPR kan krävas
- bedöma om incidentrapportering enligt NIS2/cybersäkerhetslagen kan vara relevant
- eskalera internt
- kontakta CERT-SE eller professionellt incidentstöd vid behov
- dokumentera tidslinje, beslut och åtgärder
- återställa försiktigt och övervaka efter fortsatt åtkomst

CyberLex Sweden bör vara tydlig med att detta är utbildningsmaterial och inte juridisk rådgivning.

---

## Swedish step-by-step answer for suspected hacking

Om du misstänker hackning eller intrång:

1. Behandla händelsen som en möjlig incident.
2. Starta en enkel incidentlogg med tidpunkt, upptäckt, system, konto och åtgärder.
3. Isolera drabbad klient, server eller konto om det går utan att förstöra bevisning.
4. Bevara loggar, larm, skärmbilder, tidsstämplar och annan bevisning.
5. Radera inte loggar och installera inte om system innan en första bedömning gjorts.
6. Identifiera vilka system, konton, användare och data som kan vara berörda.
7. Stäng av eller säkra misstänkt komprometterade konton.
8. Återkalla aktiva sessioner och byt lösenord från en ren enhet.
9. Kontrollera MFA, vidarebefordringsregler, administratörsrättigheter och ovanliga inloggningar.
10. Bedöm om personuppgifter kan ha påverkats.
11. Bedöm om anmälan till IMY enligt GDPR kan krävas.
12. Bedöm om NIS2/cybersäkerhetslagen eller annan incidentrapportering kan vara relevant.
13. Eskalera till IT, säkerhet, ledning, juridik och dataskyddsansvarig.
14. Kontakta CERT-SE eller incidenthanteringsexpert vid behov.
15. Dokumentera alla beslut, åtgärder och källor.
16. Återställ först när du förstår intrångsvägen och har minskat risken för återinfektion.

---

## Swedish step-by-step answer for suspected data leak

Om du misstänker dataläcka:

1. Bekräfta vad som är känt och vad som fortfarande är oklart.
2. Stoppa fortsatt exponering, till exempel genom att ta bort publik åtkomst eller stänga exponerade länkar.
3. Bevara bevis, till exempel skärmbilder, loggar, länkar, tidsstämplar och behörighetsinställningar.
4. Identifiera vilken data som kan ha exponerats.
5. Bedöm om datan innehåller personuppgifter.
6. Bedöm om särskilt känsliga uppgifter, lösenord, hemligheter eller skyddsvärd information finns med.
7. Bedöm om någon obehörig faktiskt har haft åtkomst eller om åtkomst bara var möjlig.
8. Bedöm risk för registrerade personers rättigheter och friheter.
9. Bedöm om anmälan till IMY krävs inom 72 timmar efter att organisationen blev medveten om incidenten.
10. Bedöm om berörda personer behöver informeras.
11. Bedöm om incidenten även är relevant enligt NIS2/cybersäkerhetslagen.
12. Dokumentera beslut, tidslinje, åtgärder och källor.

---

## English step-by-step answer for suspected hacking

If you suspect hacking or intrusion:

1. Treat it as a possible incident.
2. Start a simple incident log with time, discovery, system, account, and actions.
3. Isolate the affected client, server, or account if possible without destroying evidence.
4. Preserve logs, alerts, screenshots, timestamps, and other evidence.
5. Do not delete logs or reinstall systems before an initial assessment.
6. Identify which systems, accounts, users, and data may be affected.
7. Disable or secure suspected compromised accounts.
8. Revoke active sessions and reset passwords from a clean device.
9. Check MFA, forwarding rules, administrator rights, and unusual logins.
10. Assess whether personal data may have been affected.
11. Assess whether GDPR notification to IMY may be required.
12. Assess whether NIS2/Swedish Cybersecurity Act reporting may be relevant.
13. Escalate to IT, security, management, legal, and data protection roles.
14. Contact CERT-SE or an incident response expert when appropriate.
15. Document all decisions, actions, and sources.
16. Recover only after the initial access path is understood and the risk of reinfection is reduced.

---

## English step-by-step answer for suspected data leak

If you suspect a data leak:

1. Confirm what is known and what remains unclear.
2. Stop further exposure, such as public access or exposed sharing links.
3. Preserve evidence such as screenshots, logs, URLs, timestamps, and permission settings.
4. Identify what data may have been exposed.
5. Assess whether the data includes personal data.
6. Assess whether sensitive data, passwords, secrets, or protected information are included.
7. Assess whether unauthorized access actually occurred or was only possible.
8. Assess the risk to individuals' rights and freedoms.
9. Assess whether IMY notification is required within 72 hours after the organization became aware of the incident.
10. Assess whether affected individuals must be informed.
11. Assess whether the incident is also relevant under NIS2/the Swedish Cybersecurity Act.
12. Document decisions, timeline, actions, and sources.

---

## Useful questions

CyberLex Sweden should use this source for questions such as:

- What should I do if I suspect hacking?
- What should we do after a cyber incident?
- What should a company do after ransomware?
- What should we do after a data leak?
- What should I do if an account is compromised?
- What should we do if customer data was exposed?
- What should we do if files are encrypted?
- What should we do after malware is detected?
- How should we preserve evidence after an incident?
- Should we report a data leak to IMY?
- Should we contact CERT-SE?
- What should we not do after a ransomware attack?
- What should an organization check after unauthorized access?

---

## Swedish useful questions

CyberLex Sweden should use this source for Swedish questions such as:

- Vad ska jag göra om jag misstänker hackning?
- Vad gör vi vid misstänkt intrång?
- Vad ska ett företag göra efter en cyberincident?
- Vad ska ett företag göra efter en ransomwareattack?
- Vad gör vi efter en dataläcka?
- Vad gör vi om kunddata har exponerats?
- Vad gör vi om ett konto är komprometterat?
- Vad gör vi om filer har krypterats?
- Vad gör vi efter malware?
- Hur bevarar vi bevis efter en incident?
- Ska vi anmäla en dataläcka till IMY?
- Ska vi kontakta CERT-SE?
- Vad ska vi inte göra efter ransomware?
- Vad ska en organisation kontrollera efter obehörig åtkomst?

---

## Source relationship

This file should work together with:

```text
data/gdpr_personal_data_breach.md
data/nis2_incident_reporting.md
data/cybercrime_dataintrang.md
data/imy_gdpr_supervision.md
data/nis2_cybersecurity_law.md
```

Use this file for practical defensive steps.

Use GDPR breach material for personal data breach notification details.

Use NIS2 incident reporting material for cybersecurity incident reporting details.

Use dataintrång material for Swedish criminal-law explanation of unauthorized access.

Use IMY material for Swedish GDPR authority context.

---

## Official source

- [CERT-SE - The national CSIRT of Sweden](https://www.cert.se/en/)
- [MSB - Hantera pågående it-incident](https://www.msb.se/sv/amnesomraden/informationssakerhet-cybersakerhet-och-sakra-kommunikationer/hantera-och-rapportera-it-incidenter-och-cyberangrepp/hantera-pagaende-it-incident/)
- [MSB - Frivillig rapportering av it-incident](https://www.msb.se/sv/amnesomraden/informationssakerhet-cybersakerhet-och-sakra-kommunikationer/hantera-och-rapportera-it-incidenter-och-cyberangrepp/rapportera-it-incident/frivillig-rapportering/)
- [MSB - Incidentrapportering enligt cybersäkerhetslagen](https://www.msb.se/sv/amnesomraden/informationssakerhet-cybersakerhet-och-sakra-kommunikationer/krav-och-regler-inom-informationssakerhet-och-cybersakerhet/nis-direktivet/incidentrapportering-enligt-cybersakerhetslagen/)
- [IMY - Notification of a personal data breach](https://www.imy.se/en/organisations/forms-and-e-services/notification-of-a-personal-data-breach/)
- [EDPB - Notify a personal data breach](https://www.edpb.europa.eu/notify-data-breach_en)
- [CISA - Ransomware Response Checklist](https://www.cisa.gov/ransomware-response-checklist)
- [CISA - I've Been Hit by Ransomware](https://www.cisa.gov/stopransomware/ive-been-hit-ransomware)

---

## Source metadata

Source date: Last checked: 2026-06-04

Version notes: Initial CyberLex Sweden incident response playbook added. Includes defensive first steps for suspected hacking, unauthorized access, ransomware, malware, compromised accounts, and data leaks. Added Swedish and English step-by-step answer patterns, evidence preservation guidance, GDPR/IMY assessment notes, NIS2/cybersäkerhetslagen assessment notes, CERT-SE escalation notes, official source links, and safety boundaries.

---

## Disclaimer

This source is for educational use in the CyberLex Sweden prototype.

It does not provide legal advice, forensic advice, emergency advice, or professional incident response services.

For serious incidents, organizations should contact qualified incident response professionals, legal counsel, data protection specialists, relevant authorities, and official support channels when appropriate.

\# Investigation Findings



\## Lab Information

\- \*\*Incident ID:\*\* LAB-IR-001

\- \*\*Investigation Type:\*\* Simulated SOC alert triage

\- \*\*Data Source:\*\* `logs/simulated\_auth.log`

\- \*\*Analysis Tool:\*\* `analyze\_logs.py`

\- \*\*Environment:\*\* Local Python analysis using synthetic authentication logs



\## Summary of Events

The Python script analyzed 8 synthetic authentication events.



\- \*\*Total events analyzed:\*\* 8

\- \*\*Failed authentication attempts:\*\* 6

\- \*\*Successful authentication attempts:\*\* 2



\## Relevant Event Sequence

The following sequence was identified for user `alex`:



1\. Four consecutive failed authentication attempts occurred from source IP `192.0.2.45` between 09:00:11 and 09:00:35.

2\. A successful authentication from the same IP address occurred at 09:01:02.

3\. Another failed authentication from the same IP address was recorded at 09:10:33.



This sequence was flagged for further investigation because repeated failures followed by a successful login may indicate suspicious authentication activity.



\## Script Investigation Flag

The Python analysis script flagged a successful authentication for `alex` following at least three failed authentication attempts from the same source IP address.



The relevant sequence consisted of four failed attempts followed by a successful authentication from `192.0.2.45`.



\## Assessment

The activity associated with `alex` is suspicious and warrants further investigation. Possible explanations include repeated password guessing or a legitimate user entering an incorrect password multiple times before successfully signing in.



The available evidence does not confirm unauthorized access or account compromise.



\## Limitations

\- The logs are synthetic and were created for educational purposes.

\- No live production systems or accounts were investigated.

\- Endpoint telemetry, MFA records, geolocation, device information, and session activity were not available.

\- The source IP addresses and authentication events were not independently validated.

\- The findings demonstrate a simulated investigation workflow and should not be interpreted as a confirmed real-world security incident.



\## Recommended Follow-Up

In a real SOC investigation, review additional authentication logs, MFA records, endpoint telemetry, and session activity. Escalate according to organizational procedures if additional evidence supports suspected unauthorized access.



No real containment or remediation actions were performed during this lab.


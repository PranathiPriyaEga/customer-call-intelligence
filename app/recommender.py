RECOMMENDATIONS = {
    "Hardware Issue": {
        "action": "Collect device and asset details, perform basic hardware diagnostics, and escalate to endpoint support if the issue persists.",
        "queue": "Endpoint / Desktop Support"
    },

    "Password / Account Access": {
        "action": "Verify the employee's identity, unlock the account or initiate a password reset, and confirm successful login.",
        "queue": "Identity & Access Management"
    },

    "Email / Outlook": {
        "action": "Check Outlook credentials and connectivity, restart Outlook, recreate the Outlook profile if needed, and escalate to messaging support.",
        "queue": "Messaging / Email Support"
    },

    "VPN Issue": {
        "action": "Verify VPN credentials and MFA, restart the VPN client, check network connectivity, and escalate to network support if the issue continues.",
        "queue": "Network Support"
    },

    "Network / Wi-Fi": {
        "action": "Check Wi-Fi connection and network adapter settings, reconnect to the corporate network, and escalate if connectivity remains unavailable.",
        "queue": "Network Support"
    },

    "Access / Permissions": {
        "action": "Verify the employee's business need and manager approval, check access-group membership, and submit an access request if required.",
        "queue": "Identity & Access Management"
    },

    "Software Installation": {
        "action": "Verify that the requested software is approved, then install it through the organization's approved software distribution process.",
        "queue": "Software / Endpoint Support"
    },

    "MFA / Authentication": {
        "action": "Verify the employee's authentication methods, troubleshoot MFA enrollment, and re-enroll the authentication method if necessary.",
        "queue": "Identity & Access Management"
    },

    "Performance Issue": {
        "action": "Check CPU, memory, storage, startup applications, and pending updates, then escalate to endpoint support if performance remains degraded.",
        "queue": "Endpoint / Desktop Support"
    },

    "General IT Support": {
        "action": "Collect additional details about the issue and route the ticket to the appropriate IT support team.",
        "queue": "IT Service Desk"
    }
}


def get_recommendation(intent):
    return RECOMMENDATIONS.get(
        intent,
        RECOMMENDATIONS["General IT Support"]
    )

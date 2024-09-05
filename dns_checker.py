import dns.resolver

# List of domains
domains = [
    "btg-apac.com", "artisanrec.com.au", "bayside.it", "bayside.technology",
    "baysidetechnology.com.au", "btg-apac.com.au", "btgapac.com.au",
    "citricdev.com", "citric.digital", "citricdigital.com",
    "citricdigital.com.au", "free-websites.com.au"
]

def check_spf(domain):
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        for rdata in answers:
            if 'v=spf1' in str(rdata):
                print(f"SPF record for {domain}: {rdata}")
    except Exception as e:
        print(f"Error fetching SPF for {domain}: {e}")

def check_dmarc(domain):
    try:
        dmarc_domain = "_dmarc." + domain
        answers = dns.resolver.resolve(dmarc_domain, 'TXT')
        for rdata in answers:
            if 'v=DMARC1' in str(rdata):
                print(f"DMARC record for {domain}: {rdata}")
    except Exception as e:
        print(f"Error fetching DMARC for {domain}: {e}")

def check_dkim(domain, selector):
    try:
        dkim_domain = f"{selector}._domainkey.{domain}"
        answers = dns.resolver.resolve(dkim_domain, 'TXT')
        for rdata in answers:
            if 'v=DKIM1' in str(rdata):  # Look for DKIM record
                print(f"DKIM record for {domain} with selector {selector}: {rdata}")
    except Exception as e:
        print(f"Error fetching DKIM for {domain} with selector {selector}: {e}")


# Check SPF and DMARC for each domain
for domain in domains:
    check_spf(domain)
    check_dmarc(domain)
    
def check_dkim(domain, selector):
    try:
        dkim_domain = f"{selector}._domainkey.{domain}"
        answers = dns.resolver.resolve(dkim_domain, 'TXT')
        for rdata in answers:
            if 'v=DKIM1' in str(rdata):  # Look for DKIM record
                print(f"DKIM record for {domain} with selector {selector}: {rdata}")
    except Exception as e:
        print(f"Error fetching DKIM for {domain} with selector {selector}: {e}")

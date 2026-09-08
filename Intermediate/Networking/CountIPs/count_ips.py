import ipaddress

def ips_between(start, end):
    def ip_to_int(ip):
        parts = ip.split('.')
        return (
            int(parts[0]) * 256**3 +
            int(parts[1]) * 256**2 +
            int(parts[2]) * 256 +
            int(parts[3])
        )

    return ip_to_int(end) - ip_to_int(start)


# Test
print(ips_between("10.0.0.0", "10.0.0.50"))   # 50
print(ips_between("10.0.0.0", "10.0.1.0"))    # 256
print(ips_between("20.0.0.10", "20.0.1.0"))   # 246

# Pass all tests (v2):
def ips_between_2(start, end):
    return int(ipaddress.ip_address(end)) - int(ipaddress.ip_address(start))
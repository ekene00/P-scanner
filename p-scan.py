import socket
import sys

def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def scan_ports(ip, start_port, end_port):
    print(f"\nScanning {ip} from port {start_port} to {end_port}...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)  # Short timeout
                result = s.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
        except KeyboardInterrupt:
            print("\nScan interrupted by user.")
            sys.exit()
        except socket.error:
            print("Could not connect to server.")
            break

    if open_ports:
        print("✅ Open ports:")
        for port in open_ports:
            print(f" - Port {port}")
    else:
        print("❌ No open ports found in the given range.")

def main():
    print("=== Port Scanner ===")

    ip = input("Enter IP address to scan: ").strip()
    if not is_valid_ip(ip):
        print("❌ Invalid IP address.")
        return

    try:
        port_range = input("Enter port range (e.g. 20-80): ").strip()
        start_port, end_port = map(int, port_range.split('-'))

        if not (0 <= start_port <= 65535 and 0 <= end_port <= 65535):
            raise ValueError

        if start_port > end_port:
            print("❌ Start port cannot be greater than end port.")
            return

        scan_ports(ip, start_port, end_port)

    except ValueError:
        print("❌ Invalid port range. Use format like 20-80.")

if __name__ == "__main__":
    main()

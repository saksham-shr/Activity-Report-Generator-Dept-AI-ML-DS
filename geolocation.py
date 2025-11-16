"""
IP Geolocation functions using free IP-API service
"""
import requests
import time

def get_location_from_ip(ip_address):
    """
    Get location information from IP address using ip-api.com
    Returns dict with location data or None if failed
    """
    # Skip localhost/private IPs
    if ip_address in ['127.0.0.1', 'localhost', '::1'] or ip_address.startswith('192.168.') or ip_address.startswith('10.') or ip_address.startswith('172.'):
        return {
            'city': 'Local',
            'region': 'Local Network',
            'country': 'Local',
            'lat': None,
            'lon': None,
            'isp': 'Local Network'
        }
    
    try:
        # Using ip-api.com free service (no API key needed, 45 requests/minute limit)
        url = f"http://ip-api.com/json/{ip_address}?fields=status,message,country,regionName,city,lat,lon,isp,query"
        
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('status') == 'success':
                return {
                    'city': data.get('city', 'Unknown'),
                    'region': data.get('regionName', 'Unknown'),
                    'country': data.get('country', 'Unknown'),
                    'lat': data.get('lat'),
                    'lon': data.get('lon'),
                    'isp': data.get('isp', 'Unknown'),
                    'ip': data.get('query', ip_address)
                }
            else:
                print(f"IP-API error: {data.get('message', 'Unknown error')}")
                return None
        else:
            print(f"IP-API HTTP error: {response.status_code}")
            return None
            
    except requests.exceptions.Timeout:
        print(f"Timeout getting location for IP: {ip_address}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error getting location for IP {ip_address}: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error getting location: {e}")
        return None

def format_location_string(location_data):
    """Format location data into a readable string"""
    if not location_data:
        return "Location unknown"
    
    parts = []
    if location_data.get('city'):
        parts.append(location_data['city'])
    if location_data.get('region'):
        parts.append(location_data['region'])
    if location_data.get('country'):
        parts.append(location_data['country'])
    
    if parts:
        return ", ".join(parts)
    return "Location unknown"


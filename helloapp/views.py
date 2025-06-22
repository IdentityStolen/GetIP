from django.shortcuts import render
from django.http import HttpRequest

def get_client_ip(request: HttpRequest):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def ask_name_and_show_ip(request):
    name = None
    ip_address = None
    ipv4 = None
    ipv6 = None
    if request.method == 'POST':
        name = request.POST.get('name')
        ip_address = get_client_ip(request)
        # Simple check for IPv4 vs IPv6
        if ip_address:
            if ':' in ip_address:
                ipv6 = ip_address
            else:
                ipv4 = ip_address
    return render(request, 'helloapp/ask_name_and_show_ip.html', {
        'name': name,
        'ipv4': ipv4,
        'ipv6': ipv6,
    })

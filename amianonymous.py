#!/usr/bin/env python3

from ip2geotools.databases.noncommercial import DbIpCity
import requests

def fetch_public_ip():
    fetch_adress = 'https://checkip.amazonaws.com'
    return requests.get(fetch_adress).text.strip()

def resolve_city(ip):
    response = DbIpCity.get(ip, api_key='free')
    return response.city

def resolve_country(ip):
    response = DbIpCity.get(ip, api_key='free')
    return response.country

def main():
    public_ip = fetch_public_ip()
    city = resolve_city(public_ip)
    country = resolve_country(public_ip)

    print('///////////////////////////////////////////////')
    print('Public IP:   {}'.format(public_ip))
    print('Location:    {}, {}'.format(city, country))
    print('\n')

    if country != 'DE':
        print('It seems, that you\'re safe!')
    else:
        print('Hmmm... Check the VPN one more time!')
    
    print('///////////////////////////////////////////////')
    
if __name__ == '__main__':
    main()
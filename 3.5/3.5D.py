from sys import stdin

sites = stdin.read()
sites = sites.split('\n')
for site in sites[:-2]:
    if sites[-2].lower() in site.lower():
        print(site)

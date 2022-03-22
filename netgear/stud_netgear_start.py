# -*- coding: utf-8 -*-
""" A Python class/program that can query and setup certain Netgear routers"""
#
# https://github.com/roblandry/pynetgear_enhanced
# pip3 install pynetgear_enhanced
#
# Since we are mocking (fakeing) the pynetgear_enhanced lib we don not need
# and should NOT install anything for this examination program to work!
#

from stud_netgear_lib import NetgearEnhanced
import pandas as pd
def main():
    """main function"""
    
    
    #
    # 1. First task is to let Python write a static web page with stats according to the attached index.html page
    #    Connected devices to router should be sorted by IP-adress, Name, Type or not sorted when no parameter is given
    #    Traffic Volume in Megabytes | (Week or Month / Average) should be formatted according to the attached html page
    #    html. Header and footer should be present so one can style the page if neccessary
    #
    # 2. Second task is similar to first task and can share code
    #    but we generate the web page as a dynamic web page with real-time stats when a client is browsing a specific URL
    #    Connected devices to router should be sorted by IP-adress, Name or Type from a given URL parameter or not sorted when no param is given
    #    You should create a new python file for this task
    #
    netgear = NetgearEnhanced(user='admin', password='admin', ssl=True)

    # info är routerinfo
    info = netgear.get_info()
    
    # statistics är de anslutna enheterna som skall gå att sortera på: IP, namn, typ eller inte alls.

    # trafic är trafikstatistik
    trafic = netgear.get_traffic_meter_statistics()
    df_info=pd.DataFrame.from_dict(info, orient="index")
    # droppa header
    info_html=df_info.to_html(header=False)

    df_trafic=pd.DataFrame.from_dict(trafic,orient="index")
    trafic_html=df_trafic.to_html(header=False)
    
    df_stats=pd.DataFrame.from_dict(netgear.get_attached_devices())
    stats_html=df_stats.to_html()
    
    # page = info_html, trafic_html...
    # page.to_html("page")
    htmlpage="<!doctype html>\n<html lang='en'>\n<head>\n<link rel='stylesheet' href='style.css'/>\n<meta charset='utf-8'/>\n<meta name='viewport' content='width=device-width, initial-scale=1'>\n<title>Netgear router info</title>\n</head>\n<body>\n<h1>Poor network admins info</h1>\n<p>"
    htmlpage+="\n<h3>Netgear router information</h3>\n"
    htmlpage+=info_html
    htmlpage+="\n<h3>Traffic Volume in Megabytes | (Week or Month / Average)</h3>\n"
    htmlpage+=trafic_html
    htmlpage+="\n<h3>Connected devices to router</h3>\n"
    htmlpage+=stats_html
    htmlpage+="</p></body></html>"
    with open("test.html","w") as file:
        file.write(htmlpage)
    

# def generate_stats_page(netgear_router,sort=None):
#     df_stats=pd.DataFrame.from_dict(netgear_router.get_attached_devices())
#     if not sort==None:
#         df_stats.sort_values(by=sort)
#     return df_stats.to_html()

if __name__ == "__main__":
    main()

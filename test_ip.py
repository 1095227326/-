def test_ip(ip):
    flag = True
    cookies = {
        '_ntes_nnid': '7c60b7e502d4b945849a374d53e61605,1677921475910',
        '_ntes_nuid': '7c60b7e502d4b945849a374d53e61605',
        'WEVNSM': '1.0.0',
        'WNMCID': 'yaonxv.1677921475978.01.0',
        'NMTID': '00OROSqgwVMm5e35UlDqoMnbxX4CtoAAAGGq-ndnA',
        'JSESSIONID-WYYY': 'ckOp6FKhiy4yVchP5CnE8W1jVGqbxcTO%2B3ulGhemNAOw9WvIi89zY1%2F6BmKc%2B7%2FdgVuWWg1qJQv3Axa4pNuJ5BrbE082%2BsUn4g%2FVdfTJcgCfmtb4vV0OJbpckm9j9zM7ux6Jgh2f%2BDSee%2BkZE98TcMXqTs2xD4ZXJcyPaWadOm75rYzj%3A1677938083522',
        '_iuqxldmzr_': '33',
    }
    headers = {
        'authority': 'music.163.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        # 'cookie': '_ntes_nnid=7c60b7e502d4b945849a374d53e61605,1677921475910; _ntes_nuid=7c60b7e502d4b945849a374d53e61605; WEVNSM=1.0.0; WNMCID=yaonxv.1677921475978.01.0; NMTID=00OROSqgwVMm5e35UlDqoMnbxX4CtoAAAGGq-ndnA; JSESSIONID-WYYY=ckOp6FKhiy4yVchP5CnE8W1jVGqbxcTO%2B3ulGhemNAOw9WvIi89zY1%2F6BmKc%2B7%2FdgVuWWg1qJQv3Axa4pNuJ5BrbE082%2BsUn4g%2FVdfTJcgCfmtb4vV0OJbpckm9j9zM7ux6Jgh2f%2BDSee%2BkZE98TcMXqTs2xD4ZXJcyPaWadOm75rYzj%3A1677938083522; _iuqxldmzr_=33',
        'referer': 'https://music.163.com/',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }
    try:
        response = requests.get('https://music.163.com/discover/toplist', cookies=cookies, headers=headers,timeout = (2,2),proxies = ip)

    except Exception :
        #print("error")
        flag =False


        #print("success")
    return flag

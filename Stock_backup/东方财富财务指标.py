from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from fake_useragent import UserAgent
#伪装浏览器头部
ua = UserAgent()
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (ua.random)
SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
# browser = webdriver.PhantomJS(service_args=SERVICE_ARGS,desired_capabilities=dcap)
wait = WebDriverWait(browser, 10)

browser.get('http://emweb.securities.eastmoney.com/f10_v2/FinanceAnalysis.aspx?type=web&code=SZ300676#zcfzb-0')
print(browser.page_source)
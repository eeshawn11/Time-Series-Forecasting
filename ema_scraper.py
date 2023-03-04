import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def retrieve_files(
            years: list[str],
            months: list[str],
            filetype: list[str]=["xls", "xlsx"],
            save_directory: str=os.path.join(os.getcwd(), "data"),
            page: str="https://www.ema.gov.sg/statistic.aspx?sta_sid=20140826Y84sgBebjwKV"
        ):
    """
    Helper function using Selenium and ChromeDriver to scrape through the EMA website and download the required files to save_directory.
    Based on the specified years and months, the scraper will download files matching filetype.

    Return
        Dictionary of files that did not download successfully.
    """
    print(f"Downloading to {save_directory}")
    chrome_options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory" : save_directory,
        "download.prompt_for_download": False
        }
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(
        options=chrome_options
    )

    # default landing page for the page
    driver.get(page)

    # keep list of failed downloads for subsequent validation
    failed = {}

    # iterate through year and months to download all xls files
    for year in years:
        year_filter = Select(driver.find_element(By.NAME, "cmStatistic1$uiFilYear"))
        year_filter.select_by_visible_text(year)
        failed[year] = {}
        for month in months:
            failed[year][month] = []
            month_filter = Select(driver.find_element(By.NAME, "cmStatistic1$uiFilMonth"))
            month_filter.select_by_visible_text(month)
            links = driver.find_elements(By.CLASS_NAME, "downloadlink")
            counter = 0
            for link in links:
                if link.get_attribute("href").split(".")[-1] in filetype:
                    filename = link.get_attribute("href").split("/")[-1]
                    link.click()
                    time.sleep(2) # buffer time for file download before checking status
                    if os.path.isfile(os.path.join(save_directory, filename)):
                        counter += 1
                    else:
                        failed[year][month].append(filename)
            print(f"{counter} files downloaded for {month}-{year}")
            print(f"{len(failed[year][month])} failed downloads")
            print(35*'-')
    driver.quit()

    print("Failed downloads:")
    print(failed)

    return failed

if __name__ == "__main__":
    failed_files = retrieve_files(years=["2022"], months=["Dec"], filetype=["xls", "xlsx"])

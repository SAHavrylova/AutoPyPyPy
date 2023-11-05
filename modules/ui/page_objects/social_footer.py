from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class SocialFooter(BasePage):
    URL = "https://novaposhta.ua/"

    def __init__(self) -> None:
        super().__init__()

    def move_to(self):
        self.driver.get(SocialFooter.URL)
    
    def footer(self):
        # Scroll to footer element
        footer_elem = self.driver.find_element(By.ID, "footer")

        self.driver.execute_script("arguments[0].scrollIntoView(true);", footer_elem)
    
    def get_facebook_url(self, facebook_url):
        facebook_element = self.driver.find_element(By.CLASS_NAME, "fb")
        facebook_url = facebook_element.get_attribute("href")
        return facebook_url == facebook_url
    
    def get_twitter_url(self, twitter_url):
        twitter_element = self.driver.find_element(By.CLASS_NAME, "tw")
        twitter_url = twitter_element.get_attribute("href")
        return twitter_url == twitter_url
    
    def get_instagram_url(self, instagram_url):
        instagram_element = self.driver.find_element(By.CLASS_NAME, "instagram")
        instagram_url = instagram_element.get_attribute("href")
        return instagram_url == instagram_url
    
    def get_youtube_url(self, youtube_url):
        youtube_element = self.driver.find_element(By.CLASS_NAME, "youtube")
        youtube_url = youtube_element.get_attribute("href")
        return youtube_url == youtube_url
    
    def get_linkedin_url(self, linkedin_url):
        linkedin_element = self.driver.find_element(By.CLASS_NAME, "linkedin")
        linkedin_url = linkedin_element.get_attribute("href")
        return linkedin_url == linkedin_url
    
    def get_tiktok_url(self, tiktok_url):
        tiktok_element = self.driver.find_element(By.CLASS_NAME, "tiktok")
        tiktok_url = tiktok_element.get_attribute("href")
        return tiktok_url == tiktok_url
    






    
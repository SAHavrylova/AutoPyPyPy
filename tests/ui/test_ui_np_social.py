from modules.ui.page_objects.social_footer import SocialFooter
import pytest

@pytest.mark.ui
def test_check_social_url():
    social_footer = SocialFooter()

    # Go to https://novaposhta.ua/
    social_footer.move_to()

    #Scroll down to footer
    social_footer.footer()

    #Check social url
    assert social_footer.get_facebook_url("http://facebook.com/nova.poshta.official")
    assert social_footer.get_twitter_url("http://twitter.com/NP_official_ua")
    assert social_footer.get_instagram_url("http://instagram.com/novaposhta.official")
    assert social_footer.get_youtube_url("https://www.youtube.com/channel/UCUgNSjGSiSdJBTjGG2IA4JA")
    assert social_footer.get_linkedin_url("https://www.linkedin.com/company/novaposhta/mycompany/?viewAsMember=true")
    assert social_footer.get_tiktok_url("https://www.tiktok.com/@novaposhta.official")

    social_footer.close()
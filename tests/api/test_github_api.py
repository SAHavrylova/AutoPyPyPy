import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("butenkosergii")
    assert r["message"] == "Not Found"

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    print(r)
    assert r["total_count"] == 50
    assert "become-qa-auto" in r["items"][0]["name"]

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert r["total_count"] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] !=0

@pytest.mark.myapi
def test_branches_exist(github_api):
    branches = github_api.list_branches("SAHavrylova", "AutoPyPyPy")
    assert branches

@pytest.mark.myapi
def test_emoji_exist(github_api):
    emoji = github_api.emojis()
    assert emoji

@pytest.mark.myapi 
def test_emoji_giraffe_exist(github_api):
    emoji = github_api.emojis()
    assert "giraffe" in emoji




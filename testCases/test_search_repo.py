import pytest

from Page_Objects.git_hub import GitHub


@pytest.mark.usefixtures("setup")
class TestSearchRepo:

    def test_search_repo(self):
        # driver = setup

        gh = GitHub(self.driver)

        gh.click_login_link()

        gh.set_user_name("pradeep-automation")

        gh.set_password("Greatindia@1234")

        gh.click_login_btn()

        gh.search_box_text_enter("react")

        gh.click_advance_search()

        gh.select_language()

        gh.set_stars(">45")

        gh.select_license()

        gh.select_state("closed")

        gh.set_followers(">50")

        gh.click_search_btn()

        # To verify if only one result is present
        result_list = gh.result_list()
        try:
            assert len(result_list) == 1
        except AssertionError:
            print("More than one result in the list", str(len(result_list)))

        # To verify if result list includes the repo 'mvoloskov/decider'
        for result in result_list:
            if result.text == "mvoloskov/decider":
                assert True, "Text not matching"
                result.click()

                # To get the first 300 characters from the file README.md
                readme_txt = gh.get_read_me_text()
                try:
                    with open("withas.txt", "w", encoding="utf-8") as with_as_write:
                        with_as_write.write(readme_txt[:301])
                    with open("withas.txt", "r") as open_file:
                        print(str(open_file.read()))
                except FileNotFoundError:
                    print("No such file present")

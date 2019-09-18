import allure


class TestGen:

    @allure.step("测试步骤")
    def test_001(self):
        allure.attach('我是','描述')
        assert True

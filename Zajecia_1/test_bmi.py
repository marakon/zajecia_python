from bmi import count_bmi

class TestCount:
    # def test_count_bmi(self):
    #     count_bmi.input = lambda: ''
    #     output = count_bmi(60, 1.7)  
    #     assert output == '20.76'

    def test_count_bmi(monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x, y: "60", "1.7")
        i = input("Your mass: ")
        i1 = input("Your height: ")
        assert i == "60"
        assert i1 == "1.7"
        assert count_bmi(i, i1) == '20.76'
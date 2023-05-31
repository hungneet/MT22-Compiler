for i in range(1,101):
    f = open("CodeGenSuite.py", "a")
    f.write("""
    def test{}(self):
        \"\"\" \"\"\"
        input = \"\"\"
        
        \"\"\"
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, {}))
    """.format(i, 500 + i))
    f.close()

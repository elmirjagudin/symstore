import util


class TestNewStore(util.CliTester):
    """
    Test publishing files to a new symstore.
    """
    initial_dir_zip = "empty.zip"

    def test_add_pdb(self):
        self.run_add_command(["--product", "dummyprod"],
                             ["dummyprog.pdb"])
        self.assertSymstoreDir("new_store.zip")


class TestExistingStore(util.CliTester):
    initial_dir_zip = "new_store.zip"

    def test_add_pdb(self):
        self.run_add_command(["--product", "dummylib"],
                             ["dummylib.pdb"])
        self.assertSymstoreDir("existing_store.zip")


class TestPublishPE(util.CliTester):
    initial_dir_zip = "existing_store.zip"

    def test_add_pdb(self):
        self.run_add_command(["--product", "peprods", "--version", "1.0.1"],
                             ["dummyprog.exe", "dummylib.dll"])
        self.assertSymstoreDir("pe_store.zip")
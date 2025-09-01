import shutil
import pytest
import os
import webbrowser
from conf.setting import REPORT_TYPE
import sys

if __name__ == '__main__':


    print(f"(sys.argv): {sys.argv}")

    if REPORT_TYPE == 'allure':
        pytest.main(
            ['-s', '-v', '--alluredir=./report/temp', './testcase',
             '--junitxml=./report/results.xml'])

        shutil.copy('./environment.xml', './report/temp')
        os.system(f'allure serve ./report/temp')

    elif REPORT_TYPE == 'tm':
        pytest.main(['-vs', '--pytest-tmreport-name=testReport.html', '--pytest-tmreport-path=./report/tmreport'])
        webbrowser.open_new_tab(os.getcwd() + '/report/tmreport/testReport.html')

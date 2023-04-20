# from working_with_files_different_formats import seminar_task_1 as st1
# from working_with_files_different_formats import seminar_task_2 as st2
# from working_with_files_different_formats import seminar_task_3 as st3
# from working_with_files_different_formats import seminar_task_4 as st4
# from pathlib import Path
# from working_with_files_different_formats import seminar_task_5 as st5
# from working_with_files_different_formats import seminar_task_6 as st6
# from working_with_files_different_formats import seminar_task_7 as st7
import os
from working_with_files_different_formats import home_work_task_2 as hwt2

# st1.txt_to_json('seminar_7_task_3.txt', 'result_task_1.json')
# st2.add_users('result_task_2.json')
# st3.json_to_csv('result_task_2.json')
# st4.csv_to_json('result_task_2.csv', 'result_task_4.json')
# st5.json_to_pickle(str(Path().cwd()))
# st6.pickle_to_csv('result_task_4.pickle', 'result_task_6.csv')
# st7.csv_to_pickle_str('result_task_6.csv')
hwt2.directory_scan(os.getcwd(), 'result_home_work_task_2')
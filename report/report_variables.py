from settings.dirs import DIR_REPORT

fields = {
    'parsing': ['link_current_vacancy', 'title', 'body', 'check_link', 'found_id_by_link', 'found_title',
                     'found_body', 'found_id', 'found_vacancy_link', 'has_been_added_to_db', 'error', 'not_contacts',
                     'not_vacancy', 'profession', 'ma', 'mex'],
    'shorts': ['in_admin_channel', 'in_id_admin', 'in_title', 'in_body',
               'out_admin_channel', 'out_id_admin', 'out_title', 'out_body'],
    'digest': ['channel', 'message_id', 'link_current_vacancy', 'status', 'site'],
}

report_file_path = {
    'parsing': f'{DIR_REPORT / "excel" / "parsing_report.xlsx"}',
    'shorts': f'{DIR_REPORT / "excel" / "shorts_report.xlsx"}',
    'digest': f'{DIR_REPORT / "excel" / "digest_report.xlsx"}'
}

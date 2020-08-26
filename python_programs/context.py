import os
import logging


class Monitor:
    pass


def monitor_base_config(logdir, ip, db_name):
    monitor_logger.info("monitoring base configurations")
    global temp_path, report_path, influx_db_config, telegraf_template_file_edges, telegraf_template_file_managers
    try:
        monitor_logdirectory = "{}/monitor".format(logdir)
        temp_path = monitor_logdirectory
        report_path = "{}/report".format(monitor_logdirectory)
        influx_db_config["ip"] = ip
        influx_db_config["database"] = db_name
        monitor_logger.info("value of temp_path is {}".format(temp_path))
        telegraf_template_file_edges = "{}/telegraf_config_for_edges".format(temp_path)
        telegraf_template_file_managers = "{}/telegraf_config_for_managers".format(temp_path)
    except Exception as e:
        monitor_logger.info("monitor_base_config failed {}".format(e))


def initialize_monitor_logger(logdirpath):
    global monitor_logger
    monitor_logdirectory = "{}/monitor".format(logdirpath)
    report_path = "{}/report".format(monitor_logdirectory)
    os.system("rm -rf {}/monitor".format(logdirpath))
    os.system("rm -rf {}/report".format(monitor_logdirectory))
    os.makedirs(monitor_logdirectory)
    os.makedirs(report_path)
    formatter = logging.Formatter('%(asctime)s::%(levelname)s::%(module)s::'
                                  '%(lineno)d [%(thread)d] %(message)s')
    monitor_log_file_hanlder = logging.FileHandler(os.path.join(monitor_logdirectory, "monitor.log"))
    monitor_logger = logging.getLogger("monitor")
    for handler in monitor_logger.handlers[:]:
        monitor_logger.removeHandler(handler)
    monitor_log_file_hanlder.setFormatter(formatter)
    monitor_log_file_hanlder.setLevel(logging.DEBUG)
    monitor_logger.addHandler(monitor_log_file_hanlder)
    monitor_logger.setLevel(logging.DEBUG)


monitor_logger = logging.getLogger("monitor")
temp_path = "/tmp"
report_path = "/tmp"
report_sever_url = None
launcher_ip = None

in_memory_operation = True
mail_config = {
    "mail_from": "monitoring-support@vmware.com",
    "mail_to": None,
    "subject": "Monitoring Analysis Report",
    "bcc": "monitoring-support@vmware.com",
    "description": ""
}
db_type = "INFLUX"
influx_db_config = {
    "ip": "",
    "port": 8086,
    "database": ""
}
mysql_db_config = {
    "ip": "",
    "port": 80,
    "database": ""
}
monitor = Monitor()
enable_monitor = True
suite_markers = None
testcase_markers = None
nsx_manager_ips = []
nsx_manager_root_username = ""
nsx_manager_root_password = ""
nsx_edge_ips = []
nsx_edge_root_username = "root"
nsx_edge_root_password = "Admin!23Admin"
telegraf_conf = {
    "influx": {
        "ip": "1.1.1.1",
        "port": "8086",
        "database": "Local_run",
    },
    "memory": {
        "enabled": True,
    },
    "cpu": {
        "enabled": True,
    }
}
alarm_json_input = {
    "target_type": "EDGE",
    "target": "edge1",
    "database_name": "db_name",
    "severity": "CRITICAL",
    "description": "alarm to identify memory leak of process",
    "markers": ['START_MARKER', 'END_MARKER'],
    "expression": [
        {
            "field": "measurement.field",
            "normalize": {
                "operation": "percentage",
            },
            "operator": "any_operator",  # Can be <, > , =
            "value": "max value",  # value above which alarm is to be raised
        }
    ],
    "action": {
        "send_mail": True,
        "download_logs": False,
    }
}

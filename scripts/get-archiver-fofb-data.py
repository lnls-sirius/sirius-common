import typing
from datetime import datetime

from siriuscommon.zabbix import ZabbixClient, ZabbixHistory


class Server:
    def __init__(self, hostname: str, appl_metrics: str) -> None:
        self.hostname = hostname
        self.appl_metrics = appl_metrics
        self.cpu_idle_time: typing.List[ZabbixHistory] = []
        self.avalilable_memory: typing.List[ZabbixHistory] = []
        self.net_traffic_in: typing.List[ZabbixHistory] = []
        self.net_traffic_out: typing.List[ZabbixHistory] = []
        self.appl_output_throughput: typing.List[ZabbixHistory] = []
        self.appl_input_throughput: typing.List[ZabbixHistory] = []


def get_server_data(
    client: ZabbixClient,
    srvs: typing.List[Server],
    time_from,
    time_till,
    # trends: bool = False,
):
    # get_data = client.get_item_trends if trends else client.get_item_history

    for srv in srvs:
        srv_items = client.get_items_from_host(srv.hostname)
        appl_items = client.get_items_from_host(srv.appl_metrics)

        for item in srv_items:
            if item.name == "CPI idle time":
                srv.cpu_idle_time = client.get_item_history(
                    item.itemid, time_from, time_till
                )
            elif item.name == "Available memory":
                srv.avalilable_memory = client.get_item_history(
                    item.itemid, time_from, time_till
                )
            elif item.name == "Incoming network traffic on eno1":
                srv.net_traffic_in = client.get_item_history(
                    item.itemid, time_from, time_till
                )
            elif item.name == "Outgoing network traffic on eno1":
                srv.net_traffic_out = client.get_item_history(
                    item.itemid, time_from, time_till
                )

        for item in appl_items:
            if item.name == "Benchmark - writing at (MB/sec)":
                srv.appl_output_throughput = client.get_item_history(
                    item.itemid, time_from, time_till
                )
            elif item.name == "Data Rate in (bytes/s)":
                srv.appl_input_throughput = client.get_item_history(
                    item.itemid, time_from, time_till
                )
    return srvs


if __name__ == "__main__":

    srvs = [
        Server("IA-20RaDiag01-CO-IOCSrv-1", "Archiver FOFB Dell 1 - Metrics"),
        Server("IA-20RaDiag02-CO-IOCSrv-1", "Archiver FOFB Dell 2 - Metrics"),
    ]

    time_from = datetime(year=2021, day=26, month=7, hour=0, minute=0)
    time_till = datetime(year=2021, day=7, month=8, hour=0, minute=0)

    client = ZabbixClient(password="", user="")

    data = get_server_data(client, srvs, time_from, time_till)
    print(data)

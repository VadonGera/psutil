import os
import sys
import psutil
from psutil._common import bytes2human as b2h


def main():
    templ = "%-17s %8s %8s %8s %5s%% %9s %s"
    print(templ % ("Device", "Total", "Used", "Free", "Use ", "Type", "Mount"))
    for part in psutil.disk_partitions(all=False):
        if os.name == "nt":
            if "cdrom" in part.opts or part.fstype == "":
                # пропускаем приводы cd-rom, в которых нет диска;
                # они могут вызвать ошибку графического интерфейса
                # Windows для неготового раздела или просто зависнуть
                continue
        usage = psutil.disk_usage(part.mountpoint)
        print(
            templ
            % (
                part.device,
                b2h(usage.total),
                b2h(usage.used),
                b2h(usage.free),
                int(usage.percent),
                part.fstype,
                part.mountpoint,
            )
        )


if __name__ == "__main__":
    sys.exit(main())
